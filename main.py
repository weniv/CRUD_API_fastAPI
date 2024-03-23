from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
import asyncio
from data import (
    user_jwt_token,
    initial_blogs,
    initial_products,
    initial_users,
    initial_courses,
)
from uuid import UUID, uuid4
from datetime import date, time
from typing import Optional


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def genUUID():
    # random하게 UUID 생성
    return uuid4()


class User(BaseModel):
    name: str
    email: str
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


# 데이터 저장소 (메모리에 저장)
# 초기 데이터 로드
blogs = {i: initial_blogs[:] for i in range(1, 101)}
products = {i: initial_products[:] for i in range(1, 101)}
users_info = {i: initial_users[:] for i in range(1, 101)}
courses = {i: initial_courses[:] for i in range(1, 101)}
users = {i + 1: User(**user) for i, user in enumerate(initial_users)}


# login API 엔드포인트
@app.post("/login")
async def login(email: str, password: str):
    if email == "hojun@gmail.com" and password == "1234":
        return {"token": user_jwt_token}


# 회원가입 API 엔드포인트
@app.post("/signup")
async def signup(user: User):
    # 이메일 중복 확인
    for existing_user in users.values():
        if user.email == existing_user.email:
            raise HTTPException(status_code=400, detail="Email already exists")

    # 사용자 추가
    user_id = len(users) + 1
    users[user_id] = user

    return {"message": "User created successfully"}


# 블로그 리스트 API 엔드포인트
@app.get("/{api_id}/blog")
async def get_blogs(api_id: int):
    if api_id not in blogs:
        raise HTTPException(status_code=404, detail="Blog data not found")
    return blogs[api_id]


# 블로그 상세 API 엔드포인트
@app.get("/{api_id}/blog/{blog_id}")
async def get_blogs(api_id: int, blog_id: int):
    if api_id not in blogs:
        raise HTTPException(status_code=404, detail="Blog data not found")
    return blogs[api_id][blog_id - 1]


# 블로그 생성 API 엔드포인트
@app.post("/{api_id}/blog")
async def create_blog(api_id: int, blog: Blog):
    if api_id not in blogs:
        blogs[api_id] = []
    blogs[api_id].append(blog)
    return {"message": "Blog created successfully"}


# 블로그 수정 API 엔드포인트
@app.put("/{api_id}/blog/{blog_id}")
async def update_blog(api_id: int, blog_id: int, blog: Blog):
    if api_id not in blogs:
        raise HTTPException(status_code=404, detail="Blog data not found")
    if blog_id > len(blogs[api_id]):
        raise HTTPException(status_code=404, detail="Blog data not found")
    blogs[api_id][blog_id - 1] = blog
    return {"message": "Blog updated successfully"}


# 블로그 삭제 API 엔드포인트
@app.delete("/{api_id}/blog/{blog_id}")
async def delete_blog(api_id: int, blog_id: int):
    if api_id not in blogs:
        raise HTTPException(status_code=404, detail="Blog data not found")
    if blog_id > len(blogs[api_id]):
        raise HTTPException(status_code=404, detail="Blog data not found")
    del blogs[api_id][blog_id - 1]
    return {"message": "Blog deleted successfully"}


# 10분마다 데이터 초기화
async def reset_data():
    global blogs, products, users, courses
    while True:
        await asyncio.sleep(600)  # 10분 대기
        blogs = {i: initial_blogs[:] for i in range(1, 101)}
        products = {i: initial_products[:] for i in range(1, 101)}
        users_info = {i: initial_users[:] for i in range(1, 101)}
        courses = {i: initial_courses[:] for i in range(1, 101)}
        users = {i + 1: User(**user) for i, user in enumerate(initial_users)}


# 백그라운드 작업으로 데이터 초기화 실행
@app.on_event("startup")
async def startup_event():
    asyncio.create_task(reset_data())
