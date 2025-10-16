#!/bin/bash
# ##############################################################
# Hace un backup de la base de produccion al OBS que está en backup_dir
# Se usa en un crontab para ejecutar este comando en forma diaria
# ##############################################################

set -e

# Cambiar al directorio del script
cd "$(dirname "$0")"

# Cargar variables del .env
source load_env_file.sh
load_env_file_strict .env

# --------------------------------------------------------------------------------------
# Hacer un backup de la base de produccion
# Se le pasa el id 1100:1100 bkp con los permisos correctos
# --------------------------------------------------------------------------------------
sudo docker run --rm \
    --network odoo-net \
    --user "1100:1100" \
    --volume ${base_ar}:/base \
    ${DBTOOLS_IMAGE} --days-to-keep ${days_to_keep} \
    --backup | tee | > /var/log/backup_prod.log 2>&1
