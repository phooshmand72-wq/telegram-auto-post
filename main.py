import requests
from bs4 import BeautifulSoup

urls = [
    "https://hooshmandyadak.ir/products?ordering=NEWEST",
    "https://hooshmandyadak.ir/blogs"
]

for url in urls:
    print("\nURL:", url)

    r = requests.get(
        url,
        headers={"User-Agent": "Mozilla/5.0"}
    )

    soup = BeautifulSoup(r.text, "html.parser")

    print("TITLE:", soup.title.text)

    for a in soup.find_all("a", href=True)[:20]:
        print(a.get_text(strip=True), a["href"])
