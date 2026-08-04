import requests

url = "https://hooshmandyadak.ir/products?ordering=NEWEST"

r = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"}
)

print(r.text[:5000])
