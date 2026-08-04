import requests
import re

url = "https://digifycdn.com/front-statics/digitheme/production/_next/static/chunks/pages/_app-deb46a1d53eec79b.js"

js = requests.get(url).text

for match in re.finditer("customer/products", js):
    start = max(0, match.start()-300)
    end = match.start()+300
    print("---------")
    print(js[start:end])
