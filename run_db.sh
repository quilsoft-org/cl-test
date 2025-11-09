#!/bin/bash
# ejecutar la imagen para debugear con VS

sudo docker run --rm -it --link wdb \
    -p 8069:8069 -p 8072:8072 -p 5678:5678\
    -v /odoo/ar/odoo-16.0/test16/config:/opt/odoo/etc/ \
    -v /odoo/ar/odoo-16.0/test16/data_dir:/opt/odoo/data \
    -v /odoo/ar/odoo-16.0/test16/log:/var/log/odoo \
    -v /odoo/ar/odoo-16.0/test16/sources:/opt/odoo/custom-addons \
    --link pg-test16:db \
    --name test16 -e ODOO_CONF=/dev/null -e WDB_SOCKET_SERVER=wdb -e WDB_NO_BROWSER_AUTO_OPEN=True \
    jobiols/odoo-jeo:16.0.debug python3 -m debugpy --listen 0.0.0.0:5678 --wait-for-client /usr/bin/odoo  \
    --logfile=/dev/stdout


#    -v /odoo/ar/odoo-16.0/test16/backup_dir:/var/odoo/backups/ \
#    -v /odoo/ar/odoo-16.0/dist-packages:/usr/lib/python3/dist-packages \
#    -v /odoo/ar/odoo-16.0/dist-local-packages:/usr/local/lib/python3.9/dist-packages/ \
