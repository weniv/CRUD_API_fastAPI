# CRUD API FastAPI
학습용 비동기 통신을 위한 CRUD 프로젝트입니다.
웹에서 fetch를 통해 비동기 통신을 연습할 수 있도록 CRUD API 서비스를 제공합니다.

## 0. 배포 URL
https://dev.wenivops.co.kr/services/fastapi-crud


## 1. 기술 스택
- FastAPI
- SQLAlchemy
- Uvicorn
- SQLite
- Pydantic

## 2. 설치 및 실행방법
### 1. 저장소 클론
```bash
git clone https://github.com/weniv/CRUD_API_fastAPI.git
cd CRUD_API_fastAPI
```
### 2. 가상환경 생성 및 활성화
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 3. 의존성 설치
```bash
pip install -r requirements.txt
```
### 4. (로컬에서)서버 실행
```bash
uvicorn main:app --reload
```
서버가 실행되면 http://127.0.0.1:8000 에서 API에 접근할 수 있습니다.

### 5. Docker 실행
Docker 이미지 빌드 및 실행
```bash
docker compose up -d --build
```

## 3. API 문서
### 자동 생성 문서
- Swagger UI: /docs
- ReDoc: /redoc


### API 엔드포인트
#### 기본 엔드포인트
- `GET /` - API 안내 및 사용 가능한 모든 엔드포인트 목록
- `GET /healthcheck` - 서버 상태 확인

#### 인증 관련
- `POST /{api_id}/signup` - 회원가입
- `POST /{api_id}/login` - 로그인 (JWT 토큰 발급)
- `GET /{api_id}/login_user_info` - 로그인한 유저 정보 조회
- `POST /login_confirm` - JWT 토큰 유효성 검증

#### 블로그 CRUD
- `GET /{api_id}/blog` - 블로그 목록 조회
- `GET /{api_id}/blog/{blog_id}` - 블로그 상세 조회
- `POST /{api_id}/blog` - 블로그 생성
- `PUT /{api_id}/blog/{blog_id}` - 블로그 수정
- `DELETE /{api_id}/blog/{blog_id}` - 블로그 삭제

#### 상품 CRUD
- `GET /{api_id}/product` - 상품 목록 조회
- `GET /{api_id}/product/{product_id}` - 상품 상세 조회
- `POST /{api_id}/product` - 상품 생성
- `PUT /{api_id}/product/{product_id}` - 상품 수정
- `DELETE /{api_id}/product/{product_id}` - 상품 삭제
- `GET /{api_id}/product/search?keyword={search_key}` - 상품 검색

#### 유저 CRUD
- `GET /{api_id}/user` - 유저 목록 조회
- `GET /{api_id}/user/{user_id}` - 유저 상세 조회
- `POST /{api_id}/user` - 유저 생성
- `PUT /{api_id}/user/{user_id}` - 유저 수정
- `DELETE /{api_id}/user/{user_id}` - 유저 삭제

#### 코스 CRUD
- `GET /{api_id}/course` - 코스 목록 조회
- `GET /{api_id}/course/{course_id}` - 코스 상세 조회
- `POST /{api_id}/course` - 코스 생성
- `PUT /{api_id}/course/{course_id}` - 코스 수정
- `DELETE /{api_id}/course/{course_id}` - 코스 삭제

#### 기타
- `GET /markdownblog` - 마크다운 블로그 조회
- `GET /asset/*` - 정적 파일 접근 (이미지 등)

**참고**: `{api_id}`는 1-1000 사이의 숫자입니다. 각 API ID별로 독립적인 데이터 공간을 제공합니다.


## 4. 사용 예시
JavaScript fetch를 사용한 API 호출
```javascript
// 1. 회원가입
fetch('https://dev.wenivops.co.kr/services/fastapi-crud/100/signup', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    username: 'testuser',
    password: 'testpass123'
  })
})
.then(response => response.json())
.then(data => console.log(data));

// 2. 로그인
fetch('https://dev.wenivops.co.kr/services/fastapi-crud/100/login', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    username: 'testuser',
    password: 'testpass123'
  })
})
.then(response => response.json())
.then(data => {
  console.log(data);
  // JWT 토큰 저장
  const token = data.access_token;
});

// 3. 블로그 목록 조회
fetch('https://dev.wenivops.co.kr/services/fastapi-crud/100/blog')
  .then(response => response.json())
  .then(data => console.log(data));

// 4. 블로그 생성
fetch('https://dev.wenivops.co.kr/services/fastapi-crud/100/blog', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    title: '새로운 블로그 글',
    content: '블로그 내용입니다.',
    author: 'test_user'
  })
})
.then(response => response.json())
.then(data => console.log(data));

// 5. 상품 검색
fetch('https://dev.wenivops.co.kr/services/fastapi-crud/100/product/search?keyword=developer')
  .then(response => response.json())
  .then(data => console.log(data));

// 6. JWT 토큰 인증
fetch('https://dev.wenivops.co.kr/services/fastapi-crud/login_confirm', {
  method: 'POST',
  headers: {
    'Authorization': 'Bearer eyJhbGciOi.weniv.h8t7NJKEiWCh7G3'
  }
})
.then(response => response.json())
.then(data => console.log(data));
```

## 5. 학습 목표
이 프로젝트를 통해 다음을 학습할 수 있습니다:

- 비동기 통신: JavaScript fetch API 사용법
- RESTful API: HTTP 메서드(GET, POST, PUT, DELETE) 이해
- JSON 데이터: JSON 형태의 데이터 송수신
- API 테스팅: Swagger UI를 통한 API 테스트
- CORS 처리: 브라우저에서 API 호출 시 발생하는 CORS 이슈 해결

## 6. 프로젝트 구조
```
CRUD_API_fastAPI/
├── main.py              # FastAPI 애플리케이션 메인 파일
├── requirements.txt     # Python 의존성 목록
├── database.db         # SQLite 데이터베이스 파일 (자동 생성)
└── README.md           # 프로젝트 설명서
```
## 7. 개발 가이드
### 새로운 엔드포인트 추가
main.py 파일에 새로운 라우터 함수를 추가하여 API 엔드포인트를 확장할 수 있습니다.
### 데이터 모델 수정
SQLAlchemy 모델을 수정하여 데이터베이스 스키마를 변경할 수 있습니다.
### 프론트엔드 연동
이 API는 순수 JavaScript, React, Vue.js 등 다양한 프론트엔드 프레임워크와 연동하여 사용할 수 있습니다.

## 8. 문제 해결
### CORS 오류 발생 시
브라우저에서 API 호출 시 CORS 오류가 발생하면, FastAPI 애플리케이션에 CORS 미들웨어가 추가되어 있는지 확인하세요.
### 데이터베이스 초기화
데이터베이스를 초기화하려면 database.db 파일을 삭제하고 서버를 재시작하면 됩니다.

## 9. 라이선스
이 프로젝트는 학습 목적으로 제공됩니다.