#!/bin/sh
# #####################################################################################
# Generar base de test con datos de prueba y opcionalmente instalarle módulos a testear
#
# Este script requiere en la carpeta backup_dir una subcarpeta bkp_test en la que debe
# haber un backup llamado test.zip que contiene un backup de una base vacia con datos
# de prueba credenciales admin / admin y sin modificar pais y lenguaje de los valores
# por defecto.
# #####################################################################################

set -ex

CLIENT="test17e"
IMAGE="jobiols/odoo-ent:17.0e.debug"
DB="pg-$CLIENT:db"
BASE=$(readlink -f "../../..")

# restaurar la base de test vacia
cp $BASE/$CLIENT/backup_dir/bkp_test/test.zip $BASE/$CLIENT/backup_dir/
oe --restore -d ${CLIENT}_test --no-deactivate -f test.zip
rm $BASE/$CLIENT/backup_dir/test.zip

sudo docker run --rm -it \
    --link wdb \
    --link $DB \
    -v $BASE/$CLIENT/config:/opt/odoo/etc/ \
    -v $BASE/$CLIENT/data_dir:/opt/odoo/data \
    -v $BASE/$CLIENT/log:/var/log/odoo \
    -v $BASE/$CLIENT/sources:/opt/odoo/custom-addons \
    -v $BASE/$CLIENT/backup_dir:/var/odoo/backups/ \
    -v $BASE/extra-addons:/opt/odoo/extra-addons \
    -v $BASE/dist-packages:/usr/lib/python3/dist-packages \
    -v $BASE/dist-local-packages:/usr/local/lib/python3.7/dist-packages \
    -e ODOO_CONF=/dev/null \
    -e WDB_SOCKET_SERVER=wdb $IMAGE --stop-after-init -d "${CLIENT}_test" \
    -i contacts # --test-enable
