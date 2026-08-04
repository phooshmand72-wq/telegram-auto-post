import requests

urls = [
    "https://hooshmandyadak.ir/backend/customer/products/",
    "https://hooshmandyadak.ir/backend/customer/blogs/articles/"
]

for url in urls:
    print("\nURL:", url)

    r = requests.get(
        url,
        headers={
            "User-Agent": "Mozilla/5.0",
            "accept-language": "fa-IR"
        }
    )

    print("STATUS:", r.status_code)
    print(r.text[:1000])
