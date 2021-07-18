import json
from urllib import request

url = "https://api.github.com/repos/pilas-engine/pilas-engine/releases/latest"
response = request.urlopen(url)

data = response.read().decode("utf-8")
data = json.loads(data)

print(data["tag_name"])
print(data["published_at"].split("T")[0])

descargas = {}

for x in data["assets"]:
    descargas[x["name"]] = x["browser_download_url"]

print(descargas)

