import requests
from bs4 import BeautifulSoup
import json

url = "https://hooshmandyadak.ir/products?ordering=NEWEST"

r = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"}
)

soup = BeautifulSoup(r.text, "html.parser")

next_data = soup.find("script", id="__NEXT_DATA__")

data = json.loads(next_data.text)

text = json.dumps(data, ensure_ascii=False)

for word in ["products", "items", "title", "price", "image"]:
    print(word, text.find(word))

print("LENGTH:", len(text))
