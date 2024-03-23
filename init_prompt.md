fastAPI를 사용하여 아래 목적에 부합하는 서비스를 만들 예정이야. main.py를 어떻게 설계하면 되는지 알려줘.

1. 목적: FE개발자 지망생을 위한 교육 목적의 CRUD가 가능한 API 서비스. 데이터는 블로그, 쇼핑몰, 회원정보, 강의정보를 JSON 형태로 제공하는 서비스

2. 설계: 다만 수백명의 사람들이 접속할 서비스라 1개의 API면 안되고, 같은 데이터가 아래와 같이 100개 정도는 들어가야 함.

/1/blog: 블로그 리스트 데이터
/2/blog: 블로그 리스트 데이터(위와 같은 데이터)
/3/blog: 블로그 리스트 데이터(위와 같은 데이터)
/N/blog: 블로그 리스트 데이터(위와 같은 데이터)

3. 제약사항: 이 서비스는 10분마다 초기화 되어서 다양한 사람들이 CRUD를 연습할 수 있도록 함

###########################

FastAPI를 사용하여 위의 요구사항에 맞는 서비스를 설계하기 위해 `main.py`를 아래와 같이 작성할 수 있습니다:

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import asyncio

app = FastAPI()

# 데이터 모델 정의
class Blog(BaseModel):
    title: str
    content: str

class Product(BaseModel):
    name: str
    price: float

class User(BaseModel):
    username: str
    email: str

class Course(BaseModel):
    title: str
    instructor: str

# 데이터 저장소 (메모리에 저장)
blogs = {}
products = {}
users = {}
courses = {}

# 블로그 리스트 API 엔드포인트
@app.get("/{api_id}/blog")
async def get_blogs(api_id: int):
    if api_id not in blogs:
        raise HTTPException(status_code=404, detail="Blog data not found")
    return blogs[api_id]

@app.post("/{api_id}/blog")
async def create_blog(api_id: int, blog: Blog):
    if api_id not in blogs:
        blogs[api_id] = []
    blogs[api_id].append(blog)
    return {"message": "Blog created successfully"}

# 쇼핑몰 리스트 API 엔드포인트
@app.get("/{api_id}/product")
async def get_products(api_id: int):
    if api_id not in products:
        raise HTTPException(status_code=404, detail="Product data not found")
    return products[api_id]

@app.post("/{api_id}/product")
async def create_product(api_id: int, product: Product):
    if api_id not in products:
        products[api_id] = []
    products[api_id].append(product)
    return {"message": "Product created successfully"}

# 회원정보 API 엔드포인트
@app.get("/{api_id}/user")
async def get_users(api_id: int):
    if api_id not in users:
        raise HTTPException(status_code=404, detail="User data not found")
    return users[api_id]

@app.post("/{api_id}/user")
async def create_user(api_id: int, user: User):
    if api_id not in users:
        users[api_id] = []
    users[api_id].append(user)
    return {"message": "User created successfully"}

# 강의정보 API 엔드포인트
@app.get("/{api_id}/course")
async def get_courses(api_id: int):
    if api_id not in courses:
        raise HTTPException(status_code=404, detail="Course data not found")
    return courses[api_id]

@app.post("/{api_id}/course")
async def create_course(api_id: int, course: Course):
    if api_id not in courses:
        courses[api_id] = []
    courses[api_id].append(course)
    return {"message": "Course created successfully"}

# 10분마다 데이터 초기화
async def reset_data():
    global blogs, products, users, courses
    while True:
        await asyncio.sleep(600)  # 10분 대기
        blogs = {}
        products = {}
        users = {}
        courses = {}

# 백그라운드 작업으로 데이터 초기화 실행
@app.on_event("startup")
async def startup_event():
    asyncio.create_task(reset_data())
```
