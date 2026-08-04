import requests

url = "https://hooshmandyadak.ir/backend/customer/products/"

headers = {
    "User-Agent": "Mozilla/5.0",
    "accept": "application/json",
    "accept-language": "fa-IR",
    "referer": "https://hooshmandyadak.ir/products?ordering=NEWEST",
    "x-requested-with": "XMLHttpRequest"
}

params = {
    "limit": 20,
    "offset": 0
}

r = requests.get(
    url,
    headers=headers,
    params=params
)

print(r.status_code)
print(r.text[:1000])
