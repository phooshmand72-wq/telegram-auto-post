import requests
import re

url = "https://digifycdn.com/front-statics/digitheme/production/_next/static/chunks/pages/products/%5B%5B...categoryNames%5D%5D-88e4f3df83f780d8.js"

r = requests.get(url)

text = r.text

print("LENGTH:", len(text))

for word in ["product", "products", "api", "queryKey", "getProducts"]:
    print(word, text.find(word))

# قسمت‌هایی که api دارند
for match in re.findall(r'.{0,80}api.{0,120}', text):
    print("----")
    print(match)
