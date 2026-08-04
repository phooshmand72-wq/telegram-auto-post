import requests
from bs4 import BeautifulSoup
import json

url = "https://hooshmandyadak.ir/products?ordering=NEWEST"

r = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"}
)

soup = BeautifulSoup(r.text, "html.parser")

data = json.loads(
    soup.find("script", id="__NEXT_DATA__").text
)

queries = data["props"]["dehydratedState"]["queries"]

print("QUERY COUNT:", len(queries))

for q in queries:
    print("----------------")
    print(q.keys())
    print("QUERY KEY:")
    print(q.get("queryKey"))
