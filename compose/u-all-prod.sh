#!/bin/bash
###############################################################
# Este comando hace lo siguiente
#  Actualiza los repositorios
#  Actualiza las imágenes
#  Baja el servidor
#  Hace un update all
#  Sube el servidor
###############################################################

set -e

# Cambiar al directorio del script
cd "$(dirname "$0")"

# Cargar variables del .env
source load_env_file.sh
load_env_file_strict .env

# Actualizar imagen y repositorios
oe -i -p

sudo docker compose down odoo

sudo docker run --rm \
    --network odoo-net \
	-v ${base_ar}/config:/opt/odoo/etc/ \
	-v ${base_ar}/data_dir:/opt/odoo/data \
	-v ${base_ar}/sources:/opt/odoo/custom-addons \
	-e ODOO_CONF=/dev/null \
	--user "1100:1100" \
	${ODOO_IMAGE} -- --stop-after-init --logfile=false -d ${cliente}_prod \
	-u all

sudo docker compose up -d odoo
