import requests
from bs4 import BeautifulSoup

url = "https://hooshmandyadak.ir/products?ordering=NEWEST"

r = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"}
)

soup = BeautifulSoup(r.text, "html.parser")

for script in soup.find_all("script", src=True):
    src = script["src"]
    print(src)
