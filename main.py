import requests
from bs4 import BeautifulSoup

url = "https://hooshmandyadak.ir/products?ordering=NEWEST"

r = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"}
)

soup = BeautifulSoup(r.text, "html.parser")

for a in soup.find_all("a", href=True):
    href = a["href"]

    if "/product/" in href:
        print(
            a.get_text(strip=True),
            href
        )
