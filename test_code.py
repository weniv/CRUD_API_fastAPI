import requests

url = "https://eduapi.weniv.co.kr/523/product/search/"
params = {"keyword": "keyring"}

response = requests.get(url, params=params)

print(response.status_code)
print(response.text)
