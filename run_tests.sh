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

CLIENT="test17"
IMAGE="jobiols/odoo-jeo:17.0.debug"
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
    -i sale_management,pos_restaurant,account,crm,website,stock,purchase,point_of_sale,project,website_sale,mrp,mass_mailing,hr_expense,hr_holidays,hr_recruitment,hr,data_recycle,maintenance,website_slides,website_event,mail,contacts,calendar,fleet,im_livechat,survey,repair,hr_attendance,ass_mailing_sms,project_todo,hr_skills,lunch,website_hr_recruitment,r_contract,pos_epson_printer,pos_mrp,pos_sale,pos_self_order_epson_printer,stock_account,ebsite_crm,website_crm_sms,website_sms,purchase_stock,account_check_printing,ccount_edi_ubl_cii,account_fleet,ccount_payment,account_payment_term,analytic,attachment_indexation,auth_signup,auth_totp,auth_totp_mail,auth_totp_portal,barcodes,arcodes_gs1_nomenclature,base,ase_import,base_import_module,base_install_request,base_setup,bus,alendar_sms,crm_iap_enrich,crm_iap_mine,crm_livechat,crm_sms,delivery,igest,event,event_crm,event_crm_sale,vent_sale,event_sms,gamification_sale_crm,google_gmail,google_recaptcha,hr_fleet,hr_gamification,hr_holidays_attendance \
    --test-enable
