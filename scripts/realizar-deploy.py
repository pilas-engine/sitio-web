import os


if not os.path.exists("00-sitio-web-de-pilas-engine"):
    print("Consiguiendo el repositorio del sitio web...")
    os.system("git clone dokku@pilas-engine.com.ar:00-sitio-web-de-pilas-engine")

print("Copiando archivos ...")
os.system("cp -r docs/* 00-sitio-web-de-pilas-engine/")

print("Realizando deploy ...")
os.system("cd 00-sitio-web-de-pilas-engine/; git add .; git commit -am 'actualizando'; git push origin master;")


