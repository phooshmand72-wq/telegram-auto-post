import requests
from bs4 import BeautifulSoup
import re

url = "https://hooshmandyadak.ir/products?ordering=NEWEST"

r = requests.get(
    url,
    headers={"User-Agent": "Mozilla/5.0"}
)

soup = BeautifulSoup(r.text, "html.parser")

scripts = [
    s["src"] for s in soup.find_all("script", src=True)
]

for src in scripts:
    try:
        js = requests.get(src).text

        if "product" in js.lower() or "api" in js.lower():
            print("\nFILE:", src)
            print("SIZE:", len(js))

            for x in re.findall(
                r'.{0,80}(?:product|api).{0,120}',
                js,
                re.I
            )[:5]:
                print(x)

    except:
        pass
