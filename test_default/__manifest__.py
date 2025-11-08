##############################################################################
#
#    Copyright (C) 2025
#    All Rights Reserved.
#
##############################################################################

{
    "name": "test18",
    "version": "18.0.1.0.0",
    "category": "Tools",
    "summary": "Test for v18 CE",
    "author": "Quilsoft",
    "website": "http://github.com/jobiols/cl-test",
    "license": "AGPL-3",
    "depends": [],
    "installable": True,
    # manifest version, if omitted it is backward compatible
    "env-ver": "2",
    # if Enterprise it installs in a different directory than community
    "odoo-license": "CE",

    'config': [

        # dbfilter = pattern to filter databases (default: None)

        # Conexiones a la base de datos solo usar en caso de base de datos externa
        # 'db_host = db',
        # 'db_port = 5432',
        # 'db_user = odoo',
        # 'db_password = odoo',
        # 'db_name = odoo',

        # Try to enable the unaccent extension when creating new databases. (default: False).
        'unaccent = True',

        # Directory where to store filestore and other data (default: ~/.local/share/Odoo)
        'data_dir = /opt/odoo/data',

        # Admin password for database management (create, duplicate, drop, backup, restore)
        'admin_passwd = template',

        # Enable the Odoo proxy mode (default: False). Should be set to True when Odoo is behind a
        # reverse proxy (like Nginx) to ensure correct url generation.
        'proxy_mode = True',

        # WORKERS EJEMPLO DE CONFIGURACION DE WORKERS
        # Regla general Nro de workers = (2 x #CPU) + 1
        # 1 worker puede manejar 6 usuarios concurrentes de backend. segun la doc odoo 18

        # Dado una servidor con 2 CPU y 8GB de RAM
        # Workers = (2*2)+1 = 5 seria la cantidad de workers para ese servidor el cual
        # soportaria 5 * 6 = 30 usuarios concurrentes
        # Esto es aproximadamente 3 workers por cpu tener en cuenta que tambien hay un worker cron

        # if ommited oe will calculate workers and cron´s based on # of cpu
        # 'workers = 0',
        # 'max_cron_threads = 1',

        # Maximum allowed virtual memory per worker (in bytes), when reached, any memory allocation
        # will fail Defaults to 2560MiB = 2560 * 1024 * 1024 bytes.
        #'limit_memory_hard = 2684354560'

        # Maximum allowed virtual memory per worker (in bytes), when reached the worker be reset
        # after the current request (default 2048MiB) = 2048 * 1024 * 1024 bytes.
        #'limit_memory_soft = 2147483648',

        # Number of requests a worker will process before being recycled and
        # restarted. Defaults to 2**16 = 65536 if ommited
        #'limit_request = 65536',

        # Maximum allowed CPU time per request (default 60)..
        #'limit_time_cpu = 60',

        # Maximum allowed Real time per request (default 120)..
        #'limit_time_real = 120',

        # Maximum allowed Real time per cron job. (default: --limit-time-real). Set to 0 for no limit.
        #'limit_time_real_cron = 120',

        # Force a limit on the maximum number of records kept in the virtual osv_memory tables. By default there is no limit. default=0,
        #'osv_memory_count_limit = 0',

        # Disable the ability to obtain or view the list of databases Default True
        'list_db = False',

        # Maximum time a cron thread/worker stays alive before it is restarted. Set to 0 to disable. (default: 0)
        #'limit-time-worker-cron = 0',
    ],

    # Config to write in odoo.conf
    "config_local": [
        "workers = 0",
        "admin_password = admin",
    ],

    "port": "8069",
    "git-repos": [
        "git@github.com:quilsoft-org/cl-test.git",
    ],

    # list of images to use in the form 'name image-url'
    "docker-images": [
        "odoo jobiols/odoo-jeo:18.0",
        "postgres postgres:16.0-alpine",
    ],
}
