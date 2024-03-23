// test를 위한 js 파일

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