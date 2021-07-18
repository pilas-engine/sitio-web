NOMBRE="sitio-de-pilas"
DATE=`date +'%y.%m.%d %H:%M:%S'`

N=[0m
G=[01;32m
Y=[01;33m
B=[01;34m


comandos:
	@echo ""
	@echo "${B}Comandos disponibles para ${Y}${NOMBRE}${N} (versión: ${VERSION})"
	@echo ""
	@echo "  ${Y}Generales de la aplicación${N}"
	@echo ""
	@echo "    ${G}ejecutar${N}                Ejecuta el servidor de desarrollo."
	@echo "    ${G}compilar${N}                Genera todos los .html del sitio."
	@echo "    ${G}actualizar_descargas${N}    Actualiza los links de descarga."
	@echo "    ${G}deploy${N}                  Sube el sitio actualizado a la web."
	@echo ""
	@echo ""


ejecutar:
	@echo "Iniciando el servidor..."
	hugo serve

deploy: compilar

compilar:
	@echo "Compilando"
	hugo -d docs

actualizar_descargas:
	python3 scripts/obtener-version-mas-reciente.py


