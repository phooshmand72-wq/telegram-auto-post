import requests
from bs4 import BeautifulSoup

url = "https://hooshmandyadak.ir/products?ordering=NEWEST"

r = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"}
)

print("STATUS:", r.status_code)

html = r.text

print("PRODUCT COUNT:", html.count("/product/"))

soup = BeautifulSoup(html, "html.parser")

for a in soup.find_all("a", href=True):
    if "product" in a["href"]:
        print("TEXT:", a.get_text(strip=True))
        print("LINK:", a["href"])
        print("----------------")
