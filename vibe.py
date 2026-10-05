"""
바이브 코딩 실습용 DB (/vibe)

- 가입·키 발급 없이 /vibe/{space}/{collection} 으로 바로 사용합니다.
- 스키마를 정하지 않습니다. 처음 POST하는 컬렉션은 자동으로 만들어집니다.
- 데이터는 메모리에만 저장되고 매일 새벽 4시(KST)에 초기화됩니다.
- /vibe/{space}/_sheet 에서 누구나 데이터를 표(시트) 형식으로 볼 수 있습니다.

주의: 메모리에 저장하므로 gunicorn 워커는 반드시 1개여야 합니다.
"""

import datetime
import json
import re
from collections import deque
from pathlib import Path

from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import HTMLResponse, JSONResponse

KST = datetime.timezone(datetime.timedelta(hours=9))
RESET_HOUR = 4  # 매일 초기화 시각 (KST)

# 같은 프로세스의 교안 API를 보호하기 위한 제한
MAX_SPACES = 3000
MAX_COLLECTIONS_PER_SPACE = 20
MAX_DOCS_PER_COLLECTION = 500
MAX_DOC_BYTES = 10 * 1024
MAX_LOGS = 50
MAX_LOG_BODY = 500

NAME_PATTERN = re.compile(r"^[A-Za-z0-9][A-Za-z0-9_-]{0,39}$")
RESERVED_FIELDS = ("id", "createdAt", "updatedAt")
# 단어 카드·className 같은 평범한 필드가 막히지 않도록, 부분 일치는 확실한 단어만 씁니다.
BLOCKED_FIELD_WORDS = ("password", "passwd", "비밀번호", "주민", "cardnum", "card_num", "card-num", "카드번호")
BLOCKED_FIELD_NAMES = {"pw", "pwd", "ssn"}

SHEET_HTML = (Path(__file__).parent / "vibe_sheet.html").read_text(encoding="utf-8")


class SensitiveFieldError(HTTPException):
    """개인정보 필드 거부. 요청 로그에도 body를 남기지 않습니다."""


router = APIRouter(prefix="/vibe", tags=["Vibe Coding Endpoint"])

# space 이름 → {"collections": {컬렉션 이름: {"next_id": int, "docs": {id: 문서}}}, "logs": deque}
spaces: dict = {}


def next_reset_time() -> datetime.datetime:
    now = datetime.datetime.now(KST)
    reset = now.replace(hour=RESET_HOUR, minute=0, second=0, microsecond=0)
    if reset <= now:
        reset += datetime.timedelta(days=1)
    return reset


def reset_vibe():
    spaces.clear()


def _now() -> str:
    return datetime.datetime.now(KST).isoformat(timespec="seconds")


def _check_name(value: str, label: str):
    if not NAME_PATTERN.match(value):
        raise HTTPException(
            status_code=400,
            detail=f"{label} 이름은 영문·숫자·-·_ 로 40자 이내여야 합니다. (입력값: {value})",
        )


def _get_space(name: str, create: bool):
    if name not in spaces and create:
        if len(spaces) >= MAX_SPACES:
            raise HTTPException(
                status_code=503,
                detail="오늘 만들 수 있는 실습 공간이 가득 찼습니다. 내일 새벽 4시 초기화 후 다시 시도해 주세요.",
            )
        spaces[name] = {"collections": {}, "logs": deque(maxlen=MAX_LOGS)}
    return spaces.get(name)


def _get_collection(space: dict, name: str, create: bool):
    collections = space["collections"]
    if name not in collections and create:
        if len(collections) >= MAX_COLLECTIONS_PER_SPACE:
            raise HTTPException(
                status_code=400,
                detail=f"한 공간에는 컬렉션을 {MAX_COLLECTIONS_PER_SPACE}개까지만 만들 수 있습니다.",
            )
        collections[name] = {"next_id": 1, "docs": {}}
    return collections.get(name)


def _find_doc(collection, doc_id: str):
    try:
        key = int(doc_id)
    except ValueError:
        key = None
    if collection is None or key not in collection["docs"]:
        raise HTTPException(status_code=404, detail=f"id가 {doc_id}인 데이터가 없습니다.")
    return key


def _parse_body(raw: bytes) -> dict:
    try:
        data = json.loads(raw.decode("utf-8") if raw else "null")
    except UnicodeDecodeError:
        raise HTTPException(status_code=400, detail="body는 UTF-8로 인코딩된 JSON이어야 합니다.")
    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="body가 올바른 JSON 형식이 아닙니다.")
    if not isinstance(data, dict):
        raise HTTPException(
            status_code=400,
            detail='body는 { "필드": 값 } 형태의 JSON 객체여야 합니다.',
        )
    for field in data:
        lowered = str(field).lower()
        if lowered in BLOCKED_FIELD_NAMES or any(word in lowered for word in BLOCKED_FIELD_WORDS):
            raise SensitiveFieldError(
                status_code=400,
                detail=f"'{field}' 같은 개인정보 필드는 실습 DB에 저장할 수 없습니다.",
            )
    return {key: value for key, value in data.items() if key not in RESERVED_FIELDS}


def _check_size(doc: dict):
    if len(json.dumps(doc, ensure_ascii=False).encode("utf-8")) > MAX_DOC_BYTES:
        raise HTTPException(
            status_code=413,
            detail=f"데이터 하나는 {MAX_DOC_BYTES // 1024}KB를 넘을 수 없습니다.",
        )


async def _run(request: Request, space_name: str, action):
    """요청을 처리하고, 성공·실패와 관계없이 시트에서 볼 수 있도록 요청 로그를 남깁니다."""
    raw = await request.body()
    log_body = raw[:MAX_LOG_BODY].decode("utf-8", "replace")
    status = 500
    try:
        _check_name(space_name, "공간(space)")
        status, payload = action(raw)
        return JSONResponse(payload, status_code=status)
    except HTTPException as error:
        status = error.status_code
        if isinstance(error, SensitiveFieldError):
            log_body = "(개인정보 필드가 있어 내용을 기록하지 않았습니다)"
        raise
    finally:
        # 시트 화면이 주기적으로 보내는 조회 요청은 로그에 남기지 않습니다.
        space = spaces.get(space_name)
        if space is not None and "x-vibe-sheet" not in request.headers:
            path = request.url.path
            path = path[path.find("/vibe/"):]
            if request.url.query:
                path += "?" + request.url.query
            space["logs"].append(
                {
                    "time": _now(),
                    "method": request.method,
                    "path": path,
                    "status": status,
                    "body": log_body,
                }
            )


def _sort_key(value):
    # 값이 없는 문서는 뒤로, 숫자는 숫자끼리, 나머지는 문자열로 비교합니다.
    if value is None:
        return (1, 0, "")
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        return (0, 0, value)
    return (0, 1, str(value))


def _sorted_docs(docs: list, sort, limit, offset) -> list:
    if sort:
        reverse = sort.startswith("-")
        field = sort.lstrip("-")
        docs = sorted(docs, key=lambda doc: _sort_key(doc.get(field)), reverse=reverse)
    start = max(offset or 0, 0)
    end = start + limit if limit and limit > 0 else None
    return docs[start:end]


####################### 시트 보기 #######################


@router.get("/{space}/_sheet", response_class=HTMLResponse, description="데이터를 표 형식으로 보는 페이지")
async def vibe_sheet(space: str):
    _check_name(space, "공간(space)")
    return HTMLResponse(SHEET_HTML)


@router.get("/{space}/_logs", description="최근 요청 로그 (최대 50건)")
async def vibe_logs(space: str):
    _check_name(space, "공간(space)")
    found = spaces.get(space)
    return list(reversed(found["logs"])) if found else []


####################### 공간 정보 #######################


@router.get("/{space}", description="공간의 컬렉션 목록과 다음 초기화 시각")
async def vibe_space_info(space: str):
    _check_name(space, "공간(space)")
    found = spaces.get(space)
    collections = found["collections"] if found else {}
    return {
        "space": space,
        "collections": {name: len(col["docs"]) for name, col in collections.items()},
        "resetAt": next_reset_time().isoformat(timespec="seconds"),
    }


####################### 컬렉션 CRUD #######################


@router.get("/{space}/{collection}", description="목록 조회 (?sort=필드, ?sort=-필드, ?limit=, ?offset=)")
async def vibe_list(
    request: Request,
    space: str,
    collection: str,
    sort: str = None,
    limit: int = None,
    offset: int = None,
):
    def action(raw):
        _check_name(collection, "컬렉션")
        found = spaces.get(space)
        col = found["collections"].get(collection) if found else None
        docs = list(col["docs"].values()) if col else []
        return 200, _sorted_docs(docs, sort, limit, offset)

    return await _run(request, space, action)


@router.get("/{space}/{collection}/{doc_id}", description="하나 조회")
async def vibe_get(request: Request, space: str, collection: str, doc_id: str):
    def action(raw):
        _check_name(collection, "컬렉션")
        found = spaces.get(space)
        col = found["collections"].get(collection) if found else None
        return 200, col["docs"][_find_doc(col, doc_id)]

    return await _run(request, space, action)


@router.post("/{space}/{collection}", description="생성 (처음 쓰는 컬렉션은 자동 생성)")
async def vibe_create(request: Request, space: str, collection: str):
    def action(raw):
        _check_name(collection, "컬렉션")
        found = _get_space(space, create=True)
        data = _parse_body(raw)
        col = _get_collection(found, collection, create=True)
        if len(col["docs"]) >= MAX_DOCS_PER_COLLECTION:
            raise HTTPException(
                status_code=400,
                detail=f"컬렉션 하나에는 데이터를 {MAX_DOCS_PER_COLLECTION}개까지만 저장할 수 있습니다.",
            )
        now = _now()
        doc = {"id": col["next_id"], **data, "createdAt": now, "updatedAt": now}
        _check_size(doc)
        col["docs"][doc["id"]] = doc
        col["next_id"] += 1
        return 201, doc

    return await _run(request, space, action)


def _update(space: str, collection: str, doc_id: str, raw: bytes, replace: bool):
    _check_name(collection, "컬렉션")
    found = _get_space(space, create=True)
    data = _parse_body(raw)
    col = _get_collection(found, collection, create=False)
    key = _find_doc(col, doc_id)
    old = col["docs"][key]
    base = {} if replace else {k: v for k, v in old.items() if k not in RESERVED_FIELDS}
    doc = {"id": key, **base, **data, "createdAt": old["createdAt"], "updatedAt": _now()}
    _check_size(doc)
    col["docs"][key] = doc
    return 200, doc


@router.put("/{space}/{collection}/{doc_id}", description="전체 수정 (보내지 않은 필드는 사라짐)")
async def vibe_replace(request: Request, space: str, collection: str, doc_id: str):
    return await _run(request, space, lambda raw: _update(space, collection, doc_id, raw, replace=True))


@router.patch("/{space}/{collection}/{doc_id}", description="부분 수정 (보낸 필드만 바뀜)")
async def vibe_patch(request: Request, space: str, collection: str, doc_id: str):
    return await _run(request, space, lambda raw: _update(space, collection, doc_id, raw, replace=False))


@router.delete("/{space}/{collection}/{doc_id}", description="삭제")
async def vibe_delete(request: Request, space: str, collection: str, doc_id: str):
    def action(raw):
        _check_name(collection, "컬렉션")
        found = _get_space(space, create=True)
        col = _get_collection(found, collection, create=False)
        doc = col["docs"].pop(_find_doc(col, doc_id))
        return 200, {"message": "삭제되었습니다.", "id": doc["id"]}

    return await _run(request, space, action)
