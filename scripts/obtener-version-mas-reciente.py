import json
from urllib import request

print("Consultando api de github...")
url = "https://api.github.com/repos/pilas-engine/pilas-engine/releases/latest"
response = request.urlopen(url)


data = response.read().decode("utf-8")
data = json.loads(data)

print("Listo, la versión más reciente es", data["tag_name"])

template = open("content/descargas_template.md", "rt")

fecha = data["published_at"].split("T")[0]
descargas = {}

for x in data["assets"]:
    descargas[x["name"]] = x["browser_download_url"]


contenido = template.read()
contenido = contenido.replace("__VERSION__", data["tag_name"])
contenido = contenido.replace("__FECHA__", fecha)
contenido = contenido.replace("__NOTA__", "<!-- CUIDADO: ESTE ARCHIVO SE GENERA A PARTIR DEL ARCHIVO 'descargas_template.md' -->")
contenido = contenido.replace("__WIN64__", descargas["pilas-engine-windows-64_bits.zip"])

archivo = open("content/descargas.md", "wt")
archivo.write(contenido)
archivo.close()

print("Generando el archivo 'content/descargas.md'")

