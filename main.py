import requests
import re

url = "https://digifycdn.com/front-statics/digitheme/production/_next/static/chunks/pages/_app-deb46a1d53eec79b.js"

js = requests.get(url).text

for x in re.findall(r'https?://[^"\']+', js):
    print(x)
