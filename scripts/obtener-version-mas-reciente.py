import json
from urllib import request

url = "https://api.github.com/repos/pilas-engine/pilas-engine/releases/latest"
response = request.urlopen(url)

data = response.read().decode("utf-8")
data = json.loads(data)

print()
print("version:", data["tag_name"])
print("fecha de publicacion:", data["published_at"].split("T")[0])
print()

descargas = {}

for x in data["assets"]:
    descargas[x["name"]] = x["browser_download_url"]

print(descargas)

