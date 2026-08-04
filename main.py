import requests
from bs4 import BeautifulSoup
import json

url = "https://hooshmandyadak.ir/products?ordering=NEWEST"

r = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"}
)

soup = BeautifulSoup(r.text, "html.parser")

next_data = soup.find(
    "script",
    id="__NEXT_DATA__"
)

if next_data:
    print("NEXT DATA FOUND")

    data = json.loads(
        next_data.text
    )

    print(data.keys())

    print(
        json.dumps(
            data,
            ensure_ascii=False
        )[:3000]
    )

else:
    print("NO NEXT DATA")
