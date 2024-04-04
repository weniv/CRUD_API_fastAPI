import datetime
import time

from fastapi import FastAPI, HTTPException, Header
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field
import asyncio
from data import (
    user_jwt_token,
    initial_login,
    initial_blogs,
    initial_products,
    initial_users,
    initial_courses,
    initial_markdown_blog,
)
from uuid import UUID, uuid4
from typing import Optional
from starlette_prometheus import metrics, PrometheusMiddleware


version_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
app = FastAPI(title="WENIV EDU API", description="WENIV EDU API", version=version_time)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.add_middleware(PrometheusMiddleware)

app.mount("/asset", StaticFiles(directory="asset"), name="asset")

app.add_route("/metrics/", metrics)


def genUUID():
    # random하게 UUID 생성
    return uuid4()


class LoginUser(BaseModel):
    username: str
    password: str


# 데이터 모델 정의
class Blog(BaseModel):
    title: str
    content: str
    id: Optional[UUID] = Field(default_factory=genUUID)
    index: Optional[str] = None
    email: Optional[str] = None
    author: Optional[str] = None
    views_count: int = Field(default=0, readonly=True)
    time: Optional[str] = None
    date: Optional[str] = None


class Product(BaseModel):
    id: int
    productName: str
    price: int
    stockCount: int
    thumbnailImg: str
    option: list
    discountRate: int
    shippingFee: int
    detailInfoImage: list
    viewCount: int = 0
    pubDate: str
    modDate: str


class User(BaseModel):
    id: Optional[UUID] = Field(default_factory=genUUID)
    index: Optional[str] = None
    name: str
    email: str
    phone: Optional[str] = None
    country: Optional[str] = None
    address: Optional[str] = None
    job: Optional[str] = None
    int: Optional[str] = None


class Course(BaseModel):
    title: str
    url: str
    price: int
    discount: int
    students: int = 0
    thumbnail: str
    rating: float
    reviews: int
    level: str
    category: str
    published: str


# 데이터 저장소 (메모리에 저장)
# 초기 데이터 로드
blogs = {i: initial_blogs[:] for i in range(1, 1001)}
products = {i: initial_products[:] for i in range(1, 1001)}
users = {i: initial_users[:] for i in range(1, 1001)}
courses = {i: initial_courses[:] for i in range(1, 1001)}
login_user = {i: initial_login[:] for i in range(1, 1001)}


####################### API 안내 #######################


# API 안내
@app.get("/")
async def maininfo():
    return {
        "message": "Welcome to WENIV API",
        "API": {
            "Signup": "POST /{api_id}/signup",
            "Login": "POST /{api_id}/login",
            "Login User Info": "GET /{api_id}/login_user_info",
            "Login Confirm": "POST /login_confirm",
            "Blog": {
                "Get Blogs": "GET /{api_id}/blog",
                "Get Blog Detail": "GET /{api_id}/blog/{blog_id}",
                "Create Blog": "POST /{api_id}/blog",
                "Update Blog": "PUT /{api_id}/blog/{blog_id}",
                "Delete Blog": "DELETE /{api_id}/blog/{blog_id}",
            },
            "Product": {
                "Get Products": "GET /{api_id}/product",
                "Get Product Detail": "GET /{api_id}/product/{product_id}",
                "Create Product": "POST /{api_id}/product",
                "Update Product": "PUT /{api_id}/product/{product_id}",
                "Delete Product": "DELETE /{api_id}/product/{product_id}",
                "Search Product": "GET /{api_id}/product/search?keyword={search_key}",
            },
            "User": {
                "Get Users": "GET /{api_id}/user",
                "Get User Detail": "GET /{api_id}/user/{user_id}",
                "Create User": "POST /{api_id}/user",
                "Update User": "PUT /{api_id}/user/{user_id}",
                "Delete User": "DELETE /{api_id}/user/{user_id}",
            },
            "Course": {
                "Get Courses": "GET /{api_id}/course",
                "Get Course Detail": "GET /{api_id}/course/{course_id}",
                "Create Course": "POST /{api_id}/course",
                "Update Course": "PUT /{api_id}/course/{course_id}",
                "Delete Course": "DELETE /{api_id}/course/{course_id}",
            },
            "Markdown Blog": {"Get Markdown Blog": "GET /markdownblog"},
        },
    }


"""
URL 패턴의 순서를 고려하여 함수를 선언하는 것이 좋습니다. 일반적으로는 더 구체적인 패턴을 먼저 선언하고, 그 다음에 더 일반적인 패턴을 선언하는 것이 좋습니다. 이렇게 하면 URL 패턴 간의 충돌을 방지할 수 있습니다.

위의 API 엔드포인트 목록을 기준으로 함수를 선언하는 순서를 제안하면 다음과 같습니다.

* maininfo: 루트 경로 ("/")에 대한 엔드포인트
* login_confirm: "/login_confirm" 경로에 대한 엔드포인트
* get_markdown_blog: "/markdownblog" 경로에 대한 엔드포인트
* signup: "/{api_id}/signup" 경로에 대한 엔드포인트
* login: "/{api_id}/login" 경로에 대한 엔드포인트
* get_login_user_info: "/{api_id}/login_user_info" 경로에 대한 엔드포인트
* search_product: "/{api_id}/product/search" 경로에 대한 엔드포인트
* get_product_detail: "/{api_id}/product/{product_id}" 경로에 대한 엔드포인트
* create_product, update_product, delete_product: "/{api_id}/product" 및 "/{api_id}/product/{product_id}" 경로에 대한 엔드포인트
* get_products: "/{api_id}/product" 경로에 대한 엔드포인트
블로그, 사용자, 코스 관련 엔드포인트들: 위와 유사한 순서로 선언

이 순서는 URL 패턴의 구체성을 고려하여 결정되었습니다. 더 구체적인 패턴을 먼저 선언하고, 그 다음에 더 일반적인 패턴을 선언합니다.
"""


####################### 서버 활성화 체크 #######################


@app.get("/healthcheck", deprecated=True)
async def healthcheck():
    return {"message": "healthcheck success"}


####################### 마크다운 데이터 #######################


# 코스 리스트 API 엔드포인트
@app.get("/markdownblog", tags=["Course List Endpoint"], description="코스 리스트 API")
async def get_markdown_blog():
    return initial_markdown_blog


####################### 회원가입 #######################


# login confirm API 엔드포인트(Bearer에서 jwt token(eyJhbGciOi.weniv.h8t7NJKEiWCh7G3) 확인)
@app.post("/login_confirm", tags=["Auth Endpoint"], description="로그인 확인 API")
async def login_confirm(authorization: str = Header(None)):
    # Authorization 헤더 확인
    if authorization is None or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid token")

    # JWT 토큰 확인
    token = authorization.split("Bearer ")[1]
    if token != user_jwt_token["access_token"]:
        raise HTTPException(status_code=401, detail="Invalid token")
    return {"message": "Token is valid"}


# 회원가입 API 엔드포인트
@app.post("/{api_id}/signup", tags=["Auth Endpoint"], description="회원가입 API")
async def signup(api_id: int, user: LoginUser):
    # 이메일 중복 확인
    if login_user[api_id] == []:
        login_user[api_id].append(
            {"username": user.username, "password": user.password}
        )
        return {"message": "User created successfully"}
    else:
        user_id_value = map(lambda x: x["username"], login_user[api_id])
        if user.username in user_id_value:
            return {"message": "User already exists"}
        else:
            login_user[api_id].append(
                {"username": user.username, "password": user.password}
            )
            return {"message": "User created successfully"}


# login API 엔드포인트
@app.post("/{api_id}/login", tags=["Auth Endpoint"], description="로그인 API")
async def login(api_id: int, user: LoginUser):
    username = user.username
    password = user.password
    if api_id not in login_user:
        raise HTTPException(status_code=404, detail="User data not found")
    for i in login_user[api_id]:
        if i["username"] == username and i["password"] == password:
            return {"message": "Login success"} | user_jwt_token
    return {"message": "Login failed"}


# 회원 정보 API 엔드포인트
@app.get("/{api_id}/login_user_info", tags=["Auth Endpoint"], description="로그인 유저 정보 API")
async def get_users(api_id: int):
    if api_id not in login_user:
        raise HTTPException(status_code=404, detail="User data not found")
    return login_user[api_id]


####################### 블로그 #######################


# 블로그 상세 API 엔드포인트
@app.get("/{api_id}/blog/{blog_id}", tags=["Blog Endpoint"], description="블로그 상세 API")
async def get_blogs(api_id: int, blog_id: int):
    if api_id not in blogs:
        raise HTTPException(status_code=404, detail="Blog data not found")
    return blogs[api_id][blog_id - 1]


# 블로그 생성 API 엔드포인트
@app.post("/{api_id}/blog", tags=["Blog Endpoint"], description="블로그 생성 API")
async def create_blog(api_id: int, blog: Blog):
    if api_id not in blogs:
        blogs[api_id] = []
    blogs[api_id].append(blog)
    return {"message": "Blog created successfully"}


# 블로그 수정 API 엔드포인트
@app.put("/{api_id}/blog/{blog_id}", tags=["Blog Endpoint"], description="블로그 수정 API")
async def update_blog(api_id: int, blog_id: int, blog: Blog):
    if api_id not in blogs:
        raise HTTPException(status_code=404, detail="Blog data not found")
    if blog_id > len(blogs[api_id]):
        raise HTTPException(status_code=404, detail="Blog data not found")
    blogs[api_id][blog_id - 1] = blog
    return {"message": "Blog updated successfully"}


# 블로그 삭제 API 엔드포인트
@app.delete("/{api_id}/blog/{blog_id}", tags=["Blog Endpoint"], description="블로그 삭제 API")
async def delete_blog(api_id: int, blog_id: int):
    if api_id not in blogs:
        raise HTTPException(status_code=404, detail="Blog data not found")
    if blog_id > len(blogs[api_id]):
        raise HTTPException(status_code=404, detail="Blog data not found")
    blogs[api_id][blog_id - 1] = {}
    return {"message": "Blog deleted successfully"}


# 블로그 리스트 API 엔드포인트
@app.get("/{api_id}/blog", tags=["Blog Endpoint"], description="블로그 리스트 API")
async def get_blogs(api_id: int):
    if api_id not in blogs:
        raise HTTPException(status_code=404, detail="Blog data not found")
    return blogs[api_id]


####################### 상품 #######################


# 상품 검색 API 엔드포인트
@app.get("/{api_id}/product/search", tags=["Product Endpoint"], description="상품 검색 API")
async def search_product(api_id: int, keyword: str):
    if api_id not in products:
        raise HTTPException(status_code=404, detail="Product data not found")
    result = []
    for product in products[api_id]:
        if keyword in product["productName"]:
            result.append(product)
    return result


# 상품 상세 API 엔드포인트
@app.get("/{api_id}/product/{product_id}", tags=["Product Endpoint"], description="상품 상세 API")
async def get_product_detail(api_id: int, product_id: int):
    if api_id not in products:
        raise HTTPException(status_code=404, detail="Product data not found")
    if product_id < 1 or product_id > len(products[api_id]):
        raise HTTPException(status_code=404, detail="Product not found")
    return products[api_id][product_id - 1]


# 상품 생성 API 엔드포인트
@app.post("/{api_id}/product", tags=["Product Endpoint"], description="상품 생성 API")
async def create_product(api_id: int, product: Product):
    if api_id not in products:
        products[api_id] = []
    products[api_id].append(product)
    return {"message": "Product created successfully"}


# 상품 수정 API 엔드포인트
@app.put("/{api_id}/product/{product_id}", tags=["Product Endpoint"], description="상품 수정 API")
async def update_product(api_id: int, product_id: int, product: Product):
    if api_id not in products:
        raise HTTPException(status_code=404, detail="Product data not found")
    if product_id < 1 or product_id > len(products[api_id]):
        raise HTTPException(status_code=404, detail="Product not found")
    products[api_id][product_id - 1] = product
    return {"message": "Product updated successfully"}


# 상품 삭제 API 엔드포인트
@app.delete("/{api_id}/product/{product_id}", tags=["Product Endpoint"], description="상품 삭제 API")
async def delete_product(api_id: int, product_id: int):
    if api_id not in products:
        raise HTTPException(status_code=404, detail="Product data not found")
    if product_id < 1 or product_id > len(products[api_id]):
        raise HTTPException(status_code=404, detail="Product not found")
    products[api_id][product_id - 1] = {}
    return {"message": "Product deleted successfully"}


# 상품 리스트 API 엔드포인트
@app.get("/{api_id}/product", tags=["Product Endpoint"], description="상품 리스트 API")
async def get_products(api_id: int):
    if api_id not in products:
        raise HTTPException(status_code=404, detail="Product data not found")
    return products[api_id]


####################### 유저 #######################


# 유저 상세 API 엔드포인트
@app.get("/{api_id}/user/{user_id}", tags=["User Endpoint"], description="유저 상세 API")
async def get_user_detail(api_id: int, user_id: int):
    if api_id not in users:
        raise HTTPException(status_code=404, detail="User data not found")
    if user_id < 1 or user_id > len(users[api_id]):
        raise HTTPException(status_code=404, detail="User not found")
    return users[api_id][user_id - 1]


# 유저 생성 API 엔드포인트
@app.post("/{api_id}/user", tags=["User Endpoint"], description="유저 생성 API")
async def create_user(api_id: int, user: User):
    if api_id not in users:
        users[api_id] = []
    users[api_id].append(user)
    return {"message": "User created successfully"}


# 유저 수정 API 엔드포인트
@app.put("/{api_id}/user/{user_id}", tags=["User Endpoint"], description="유저 수정 API")
async def update_user(api_id: int, user_id: int, user: User):
    if api_id not in users:
        raise HTTPException(status_code=404, detail="User data not found")
    if user_id < 1 or user_id > len(users[api_id]):
        raise HTTPException(status_code=404, detail="User not found")
    users[api_id][user_id - 1] = user
    return {"message": "User updated successfully"}


# 유저 삭제 API 엔드포인트
@app.delete("/{api_id}/user/{user_id}", tags=["User Endpoint"], description="유저 삭제 API")
async def delete_user(api_id: int, user_id: int):
    if api_id not in users:
        raise HTTPException(status_code=404, detail="User data not found")
    if user_id < 1 or user_id > len(users[api_id]):
        raise HTTPException(status_code=404, detail="User not found")
    users[api_id][user_id - 1] = {}
    return {"message": "User deleted successfully"}


# 유저 리스트 API 엔드포인트
@app.get("/{api_id}/user", tags=["User Endpoint"], description="유저 리스트 API")
async def get_users(api_id: int):
    if api_id not in users:
        raise HTTPException(status_code=404, detail="User data not found")
    return users[api_id]


####################### 코스 #######################


# 코스 상세 API 엔드포인트
@app.get("/{api_id}/course/{course_id}", tags=["Course Endpoint"], description="코스 상세 API")
async def get_course_detail(api_id: int, course_id: int):
    if api_id not in courses:
        raise HTTPException(status_code=404, detail="Course data not found")
    if course_id < 1 or course_id > len(courses[api_id]):
        raise HTTPException(status_code=404, detail="Course not found")
    return courses[api_id][course_id - 1]


# 코스 생성 API 엔드포인트
@app.post("/{api_id}/course", tags=["Course Endpoint"], description="코스 생성 API")
async def create_course(api_id: int, course: Course):
    if api_id not in courses:
        courses[api_id] = []
    courses[api_id].append(course)
    return {"message": "Course created successfully"}


# 코스 수정 API 엔드포인트
@app.put("/{api_id}/course/{course_id}", tags=["Course Endpoint"], description="코스 수정 API")
async def update_course(api_id: int, course_id: int, course: Course):
    if api_id not in courses:
        raise HTTPException(status_code=404, detail="Course data not found")
    if course_id < 1 or course_id > len(courses[api_id]):
        raise HTTPException(status_code=404, detail="Course not found")
    courses[api_id][course_id - 1] = course
    return {"message": "Course updated successfully"}


# 코스 삭제 API 엔드포인트
@app.delete("/{api_id}/course/{course_id}", tags=["Course Endpoint"], description="코스 삭제 API")
async def delete_course(api_id: int, course_id: int):
    if api_id not in courses:
        raise HTTPException(status_code=404, detail="Course data not found")
    if course_id < 1 or course_id > len(courses[api_id]):
        raise HTTPException(status_code=404, detail="Course not found")
    courses[api_id][course_id - 1] = {}
    return {"message": "Course deleted successfully"}


# 코스 리스트 API 엔드포인트
@app.get("/{api_id}/course", tags=["Course Endpoint"], description="코스 리스트 API")
async def get_courses(api_id: int):
    if api_id not in courses:
        raise HTTPException(status_code=404, detail="Course data not found")
    return courses[api_id]


####################### 데이터 초기화 #######################


# 30분마다 데이터 초기화
async def reset_data():
    global blogs, products, users, courses
    while True:
        await asyncio.sleep(1800)  # 30분 대기
        blogs = {i: initial_blogs[:] for i in range(1, 1001)}
        products = {i: initial_products[:] for i in range(1, 1001)}
        users = {i: initial_users[:] for i in range(1, 1001)}
        courses = {i: initial_courses[:] for i in range(1, 1001)}
        login_user = {i: initial_login[:] for i in range(1, 1001)}


# 백그라운드 작업으로 데이터 초기화 실행
@app.on_event("startup")
async def startup_event():
    asyncio.create_task(reset_data())
