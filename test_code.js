// test를 위한 js 파일

// 회원 가입 fetch를 이용한 POST 요청
fetch('http://127.0.0.1:8000/1/signup/', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({
        username: 'test1',
        password: 'test1234',
    }),
})
    .then(response => response.json())
    .then(json => console.log(json))
    .catch(error => console.error(error));

fetch('http://127.0.0.1:8000/1/signup/', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({
        username: 'test2',
        password: 'test1234',
    }),
})
    .then(response => response.json())
    .then(json => console.log(json))
    .catch(error => console.error(error));

// 회원가입이 제대로 되었는지 확인하기 위한 GET 요청
fetch('http://127.0.0.1:8000/1/login_user_info/')
    .then(response => response.json())
    .then(json => console.log(json))
    .catch(error => console.error(error));

// 로그인 fetch를 이용한 POST 요청
fetch('http://127.0.0.1:8000/1/login/', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({
        username: 'test1',
        password: 'test1234',
    }),
})
    .then(response => response.json())
    .then(json => console.log(json))
    .catch(error => console.error(error));

// 로그인이 제대로 되었는지 확인하기 위한 POST 요청(Bearer Token 필요)
fetch('http://127.0.0.1:8000/login_confirm/', {
    method: 'POST',
    headers: {
        'Authorization': 'Bearer eyJhbGciOi.weniv.h8t7NJKEiWCh7G3',
    },
})
    .then(response => response.json())
    .then(json => console.log(json))
    .catch(error => console.error(error));


////////////////////////// 블로그 관련 fetch 요청 //////////////////////////
// 블로그 리스트 fetch를 이용한 GET 요청
fetch('http://127.0.0.1:8000/1/blog/')
    .then(response => response.json())
    .then(json => console.log(json))
    .catch(error => console.error(error));

// 블로그 상세 fetch를 이용한 GET 요청
fetch('http://127.0.0.1:8000/1/blog/1')
    .then(response => response.json())
    .then(json => console.log(json))
    .catch(error => console.error(error));

// 블로그 생성 fetch를 이용한 POST 요청
fetch('http://127.0.0.1:8000/1/blog/', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({
        title: 'test',
        content: 'test',
    }),
})
    .then(response => response.json())
    .then(json => console.log(json))
    .catch(error => console.error(error));


// 블로그 수정 fetch를 이용한 PUT 요청
fetch('http://127.0.0.1:8000/1/blog/1', {
    method: 'PUT',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({
        title: 'test put',
        content: 'test put',
    }),
})
    .then(response => response.json())
    .then(json => console.log(json))
    .catch(error => console.error(error));


// 블로그 삭제 fetch를 이용한 DELETE 요청
fetch('http://127.0.0.1:8000/1/blog/1', {
    method: 'DELETE',
})
    .then(response => response.json())
    .then(json => console.log(json))
    .catch(error => console.error(error));


////////////////////////// 상품 관련 fetch 요청 //////////////////////////
// 상품 리스트 fetch를 이용한 GET 요청
fetch('http://127.0.0.1:8000/1/product/')
    .then(response => response.json())
    .then(json => console.log(json))
    .catch(error => console.error(error));

// 상품 상세 fetch를 이용한 GET 요청
fetch('http://127.0.0.1:8000/1/product/1')
    .then(response => response.json())
    .then(json => console.log(json))
    .catch(error => console.error(error));

// 상품 생성 fetch를 이용한 POST 요청
fetch('http://127.0.0.1:8000/1/product/', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({
        id: 1,
        productName: 'New Product',
        price: 10000,
        stockCount: 100,
        thumbnailImg: 'asset/products/img/new/1.jpg',
        option: [],
        discountRate: 0,
        shippingFee: 2500,
        detailInfoImage: ['asset/products/img/new/1.jpg'],
        viewCount: 0,
        pubDate: '2023-06-01',
        modDate: '2023-06-01',
    }),
})
    .then(response => response.json())
    .then(json => console.log(json))
    .catch(error => console.error(error));

// 상품 수정 fetch를 이용한 PUT 요청
fetch('http://127.0.0.1:8000/1/product/1', {
    method: 'PUT',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({
        id: 1,
        productName: 'Updated Product',
        price: 15000,
        stockCount: 50,
        thumbnailImg: 'asset/products/img/new/1.jpg',
        option: [],
        discountRate: 10,
        shippingFee: 3000,
        detailInfoImage: ['asset/products/img/new/1.jpg'],
        viewCount: 0,
        pubDate: '2023-06-01',
        modDate: '2023-06-02',
    }),
})
    .then(response => response.json())
    .then(json => console.log(json))
    .catch(error => console.error(error));

// 상품 삭제 fetch를 이용한 DELETE 요청
fetch('http://127.0.0.1:8000/1/product/1', {
    method: 'DELETE',
})
    .then(response => response.json())
    .then(json => console.log(json))
    .catch(error => console.error(error));


////////////////////////// 유저 관련 fetch 요청 //////////////////////////
// 유저 리스트 fetch를 이용한 GET 요청
fetch('http://127.0.0.1:8000/1/user/')
    .then(response => response.json())
    .then(json => console.log(json))
    .catch(error => console.error(error));

// 유저 상세 fetch를 이용한 GET 요청
fetch('http://127.0.0.1:8000/1/user/1')
    .then(response => response.json())
    .then(json => console.log(json))
    .catch(error => console.error(error));

// 유저 생성 fetch를 이용한 POST 요청
fetch('http://127.0.0.1:8000/1/user/', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({
        name: 'New User',
        email: 'newuser@example.com',
        phone: '010-12134-56178',
        country: 'Korea',
        address: 'Seoul, South Korea',
        job: 'Developer',
        int: '30',
    }),
})
    .then(response => response.json())
    .then(json => console.log(json))
    .catch(error => console.error(error));

// 유저 수정 fetch를 이용한 PUT 요청
fetch('http://127.0.0.1:8000/1/user/1', {
    method: 'PUT',
    headers: {
        'Content-Type': 'application/json',
    },
    body: JSON.stringify({
        name: 'Updated User',
        email: 'updateduser@example.com',
        phone: '010-9876-5432',
        country: 'USA',
        address: 'New York, USA',
        job: 'Designer',
        int: '35',
    }),
})
    .then(response => response.json())
    .then(json => console.log(json))
    .catch(error => console.error(error));

// 유저 삭제 fetch를 이용한 DELETE 요청
fetch('http://127.0.0.1:8000/1/user/1', {
    method: 'DELETE',
})
    .then(response => response.json())
    .then(json => console.log(json))
    .catch(error => console.error(error));