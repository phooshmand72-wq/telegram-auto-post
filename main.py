import requests
import re

url = "https://digifycdn.com/front-statics/digitheme/production/_next/static/chunks/pages/_app-deb46a1d53eec79b.js"

js = requests.get(url).text

for word in ["baseURL", "backend-service", "axios", "apiURL"]:
    print("\nWORD:", word)

    for m in re.finditer(word, js):
        print(js[m.start()-200:m.start()+300])
        break
