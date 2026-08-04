import requests

url = "https://digifycdn.com/front-statics/digitheme/production/_next/static/chunks/pages/_app-deb46a1d53eec79b.js"

js = requests.get(url).text

start = js.find("getCategories")

print(js[start:start+2000])
