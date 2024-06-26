user_jwt_token = {
    "access_token": "eyJhbGciOi.weniv.h8t7NJKEiWCh7G3",
    "refresh_token": "eyJhbGciOi.weniv.h8t7NJKEiWCh7G3",
}

initial_login = []


"""
https://datagenerator.co.kr/ 활용

[
    "<iter(5)>",
    {
        "_id": "<uuid()>",
        "index": "<index()>",
        "title": "<lorem(10, word)>",
        "content": "<lorem(10, paragraph)>",
        "email": "<email()>",
        "author": "<name()>",
        "views_count": "<int(1, 50000)>",
        "created_time": "<time()>",
        "created_date": "<date(2024-01-01, 2024-12-30, YYYY-MM-DD)>",
    }
]
"""

initial_blogs = [
    {
        "_id": "16118968-7332-4d5d-B815-1741bc01d43c",
        "index": "1",
        "thumbnail": "asset/blogs/1.webp",
        "title": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt",
        "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        "email": "user-ww0qnop@Eu.com",
        "author": "licat",
        "views_count": "10527",
        "time": "19:54:55",
        "date": "2024-02-01",
    },
    {
        "_id": "829b151c-fa81-4b14-B389-32c77b18b21b",
        "index": "2",
        "thumbnail": "asset/blogs/2.webp",
        "title": "consectetur adipiscing elit, sed do eiusmod tempor incididunt",
        "content": "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        "email": "user-tu8b2y7@sollicitudin.net",
        "author": "gary",
        "views_count": "39231",
        "time": "20:46:34",
        "date": "2024-04-29",
    },
    {
        "_id": "6041712a-9978-42e4-B08a-dd26b7831539",
        "index": "3",
        "thumbnail": "asset/blogs/3.webp",
        "title": "sed do eiusmod tempor incididunt",
        "content": "sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam. quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident. sunt in culpa qui officia deserunt mollit anim id est laborum.",
        "email": "user-pj3kxn2@Proin.com",
        "author": "hati",
        "views_count": "11528",
        "time": "05:02:41",
        "date": "2024-07-19",
    },
    {
        "_id": "b4170277-1d32-4189-A59e-358e325f2863",
        "index": "4",
        "thumbnail": "asset/blogs/4.webp",
        "title": "Lorem ipsum dolor",
        "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        "email": "user-trd2ao1@facilisi.biz",
        "author": "izzy",
        "views_count": "8906",
        "time": "01:23:21",
        "date": "2024-12-18",
    },
    {
        "_id": "842973be-f584-48db-A71f-15a6ac0f41b2",
        "index": "5",
        "thumbnail": "asset/blogs/5.webp",
        "title": "exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat",
        "content": "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
        "email": "user-xfvwfns@dictum.biz",
        "author": "max",
        "views_count": "38331",
        "time": "12:22:57",
        "date": "2024-01-07",
    },
]

# https://test.api.weniv.co.kr/mall
initial_products = [
    {
        "id": 1,
        "productName": "Developer Gary's bug-catching metal keyring",
        "price": 12500,
        "stockCount": 100,
        "thumbnailImg": "asset/products/img/1/thumbnailImg.jpg",
        "option": [],
        "discountRate": 0,
        "shippingFee": 1500,
        "detailInfoImage": [
            "asset/products/detail/2/detail1.png",
            "asset/products/detail/2/detail2.png",
        ],
        "viewCount": 0,
        "pubDate": "2022-02-28",
        "modDate": "2022-02-28",
    },
    {
        "id": 2,
        "productName": "U-dangtangtang licat's Laboratory Sticker Pack",
        "price": 3500,
        "stockCount": 1000,
        "thumbnailImg": "asset/products/img/2/thumbnailImg.jpg",
        "option": [],
        "discountRate": 0,
        "shippingFee": 1500,
        "detailInfoImage": [
            "asset/products/detail/2/detail1.png",
            "asset/products/detail/2/detail2.png",
        ],
        "viewCount": 0,
        "pubDate": "2022-02-28",
        "modDate": "2022-02-28",
    },
    {
        "id": 3,
        "productName": "Deep Learning Developer Lap Blanket",
        "price": 17500,
        "stockCount": 0,
        "thumbnailImg": "asset/products/img/3/thumbnailImg.jpg",
        "option": [],
        "discountRate": 0,
        "shippingFee": 1500,
        "detailInfoImage": [
            "asset/products/detail/3/detail1.png",
            "asset/products/detail/3/detail2.png",
            "asset/products/detail/3/detail3.png",
        ],
        "viewCount": 0,
        "pubDate": "2022-02-28",
        "modDate": "2022-02-28",
    },
    {
        "id": 4,
        "productName": "Yes, it's a development job. developer metal keyring",
        "price": 13500,
        "stockCount": 100,
        "thumbnailImg": "asset/products/img/4/thumbnailImg.jpg",
        "option": [],
        "discountRate": 0,
        "shippingFee": 1500,
        "detailInfoImage": [
            "asset/products/detail/4/detail1.png",
            "asset/products/detail/4/detail2.png",
        ],
        "viewCount": 0,
        "pubDate": "2022-02-28",
        "modDate": "2022-02-28",
    },
    {
        "id": 5,
        "productName": "Hack Your Life Developer Laptop Pouch",
        "price": 36000,
        "stockCount": 230,
        "thumbnailImg": "asset/products/img/5/thumbnailImg.jpg",
        "option": [
            {"id": 1, "optionName": "13 inches", "additionalFee": 0},
            {"id": 2, "optionName": "15 inches", "additionalFee": 1000},
        ],
        "discountRate": 19,
        "shippingFee": 1500,
        "detailInfoImage": [
            "asset/products/detail/5/detail1.png",
            "asset/products/detail/5/detail2.png",
        ],
        "viewCount": 0,
        "pubDate": "2022-02-28",
        "modDate": "2022-02-28",
    },
    {
        "id": 6,
        "productName": "[NEW] WENIV developer, 2 types of character sticker packs",
        "price": 5500,
        "stockCount": 1000,
        "thumbnailImg": "asset/products/img/6/thumbnailImg.jpg",
        "option": [
            {"id": 1, "optionName": "WENIV Developer Sticker Pack", "additionalFee": 0},
            {"id": 2, "optionName": "WENIV Friends Sticker Pack", "additionalFee": 0},
            {
                "id": 3,
                "optionName": "Sticker pack set (developer + friends)",
                "additionalFee": 5000,
            },
        ],
        "discountRate": 0,
        "shippingFee": 1500,
        "detailInfoImage": [
            "asset/products/detail/6/detail1.png",
            "asset/products/detail/6/detail2.png",
            "asset/products/detail/6/detail3.png",
            "asset/products/detail/6/detail4.png",
            "asset/products/detail/6/detail5.png",
        ],
        "viewCount": 0,
        "pubDate": "2022-02-28",
        "modDate": "2022-02-28",
    },
    {
        "id": 7,
        "productName": "Jeju Coding Base Camp Coding Workbook Set",
        "price": 8000,
        "stockCount": 1000,
        "thumbnailImg": "asset/products/img/7/thumbnailImg.jpg",
        "option": [],
        "discountRate": 0,
        "shippingFee": 1500,
        "detailInfoImage": [
            "asset/products/detail/7/detail1.png",
            "asset/products/detail/7/detail2.png",
        ],
        "viewCount": 0,
        "pubDate": "2022-02-28",
        "modDate": "2022-02-28",
    },
]

"""
[
    "<iter(5)>",
    {
        "_id": "<uuid()>",
        "index": "<index()>",
        "name": "<name()>",
        "email": "<email()>",
        "phone": "<phone()>",
        "country": "<country()>",
        "address": "<address()>",
        "job": "<job()>",
        "int": "<int(20, 60)>",
    }
]
"""

initial_users = [
    {
        "_id": "c1ef8c20-e32d-4999-A9e5-d4ae30f27c7f",
        "index": "1",
        "name": "allosa",
        "email": "user-t513r6o@Sed.biz",
        "phone": "010-55176-69215",
        "country": "korea",
        "address": "jeju Hallasan 44-6",
        "job": "designer",
        "int": "42",
    },
    {
        "_id": "2fb51aff-2db1-4703-B788-93efa57be923",
        "index": "2",
        "name": "gray",
        "email": "user-08ldeac@pretium.com",
        "phone": "010-39949-18494",
        "country": "korea",
        "address": "jeju Hallasan 44-7",
        "job": "developer",
        "int": "23",
    },
    {
        "_id": "35683987-6de1-425a-Aeb3-16bde3bc6d02",
        "index": "3",
        "name": "hati",
        "email": "user-xy44poy@etiam.biz",
        "phone": "010-46285-11294",
        "country": "korea",
        "address": "jeju Hallasan 44-8",
        "job": "front-end developer",
        "int": "54",
    },
    {
        "_id": "3e45cbaf-fe06-41cb-A2db-487263fe5663",
        "index": "4",
        "name": "izzy",
        "email": "user-1hvf7l6@vitae.co.kr",
        "phone": "010-95816-14213",
        "country": "korea",
        "address": "jeju Hallasan 44-6",
        "job": "front-end developer",
        "int": "38",
    },
    {
        "_id": "34d64ff0-3922-4751-Cf7a-e6466bda33b9",
        "index": "5",
        "name": "licat",
        "email": "user-nny2fu5@velit.net",
        "phone": "010-65937-00377",
        "country": "hello world",
        "address": "we are the universe",
        "job": "WENIV CEO and Developer",
        "int": "44",
    },
]

initial_courses = [
    {
        "title": "HTML/CSS Basecamp",
        "url": "Instructor 1",
        "price": 22000,
        "discount": 20,
        "students": 0,
        "thumbnail": "asset/courses/1.png",
        "rating": 4.5,
        "reviews": 100,
        "level": "Beginner",
        "category": "Web Development",
        "published": "2022-02-28",
    },
    {
        "title": "JavaScript Basecamp",
        "url": "Instructor 2",
        "price": 22000,
        "discount": 15,
        "students": 0,
        "thumbnail": "asset/courses/2.png",
        "rating": 4.5,
        "reviews": 100,
        "level": "Beginner",
        "category": "Web Development",
        "published": "2022-02-28",
    },
    {
        "title": "Python Basecamp",
        "url": "Instructor 3",
        "price": 22000,
        "discount": 25,
        "students": 500,
        "thumbnail": "asset/courses/3.png",
        "rating": 4.7,
        "reviews": 200,
        "level": "Beginner",
        "category": "Programming",
        "published": "2022-03-15",
    },
    {
        "title": "Python advanced course",
        "url": "Instructor 4",
        "price": 22000,
        "discount": 10,
        "students": 300,
        "thumbnail": "asset/courses/4.png",
        "rating": 4.6,
        "reviews": 150,
        "level": "Intermediate",
        "category": "Programming",
        "published": "2022-04-10",
    },
    {
        "title": "Django Basecamp",
        "url": "Instructor 5",
        "price": 44000,
        "discount": 30,
        "students": 200,
        "thumbnail": "asset/courses/5.png",
        "rating": 4.8,
        "reviews": 80,
        "level": "Intermediate",
        "category": "Web Development",
        "published": "2022-05-01",
    },
]


initial_markdown_blog = [
    {
        "_id": "16118968-7332-4d5d-B815-1741bc01d43c",
        "index": "1",
        "thumbnail": "asset/blogs/1.webp",
        "title": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt",
        "content": "",
        "email": "user-ww0qnop@Eu.com",
        "author": "licat",
        "views_count": "10527",
        "time": "19:54:55",
        "date": "2024-02-01",
    },
    {
        "_id": "829b151c-fa81-4b14-B389-32c77b18b21b",
        "index": "2",
        "thumbnail": "asset/blogs/2.webp",
        "title": "consectetur adipiscing elit, sed do eiusmod tempor incididunt",
        "content": "",
        "author": "gary",
        "views_count": "39231",
        "time": "20:46:34",
        "date": "2024-04-29",
    },
]

initial_markdown_blog = [
    {
        "_id": "16118968-7332-4d5d-B815-1741bc01d43c",
        "index": "1",
        "thumbnail": "asset/blogs/1.webp",
        "title": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt",
        "content": "# Lorem ipsum dolor sit amet\n\nLorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. \n\n![Sample Image](https://via.placeholder.com/500x300)\n\nDuis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\n\n| Header 1 | Header 2 | Header 3 |\n|----------|----------|----------|\n| Cell 1   | Cell 2   | Cell 3   |\n| Cell 4   | Cell 5   | Cell 6   |\n\nUt enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.",
        "email": "user-ww0qnop@Eu.com",
        "author": "licat",
        "views_count": "10527",
        "time": "19:54:55",
        "date": "2024-02-01",
    },
    {
        "_id": "829b151c-fa81-4b14-B389-32c77b18b21b",
        "index": "2",
        "thumbnail": "asset/blogs/2.webp",
        "title": "consectetur adipiscing elit, sed do eiusmod tempor incididunt",
        "content": '## consectetur adipiscing elit\n\nConsectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.\n\n```python\ndef hello_world():\n    print("Hello, World!")\n```\n\nDuis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.\n\n![Another Sample Image](https://via.placeholder.com/400x200)\n\nUt enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.',
        "author": "gary",
        "views_count": "39231",
        "time": "20:46:34",
        "date": "2024-04-29",
    },
]
