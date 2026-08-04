import requests

urls = [
    "https://hooshmandyadak.ir/customer/products/",
    "https://hooshmandyadak.ir/customer/products/?limit=20",
]

for url in urls:
    print("\nURL:", url)

    r = requests.get(
        url,
        headers={"User-Agent": "Mozilla/5.0"}
    )

    print("STATUS:", r.status_code)
    print(r.text[:500])
