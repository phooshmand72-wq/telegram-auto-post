import requests
from bs4 import BeautifulSoup

page = "https://hooshmandyadak.ir/products?ordering=NEWEST"

r = requests.get(
    page,
    headers={"User-Agent": "Mozilla/5.0"}
)

soup = BeautifulSoup(r.text, "html.parser")

scripts = [
    s["src"] for s in soup.find_all("script", src=True)
]

for src in scripts:
    try:
        js = requests.get(src).text

        if "customer/product" in js:
            print("\nFOUND IN:", src)

            pos = js.find("customer/product")

            print(
                js[pos-300:pos+300]
            )

    except Exception as e:
        pass
