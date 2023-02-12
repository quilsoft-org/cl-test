.. |company| replace:: jeo Soft

.. |company_logo| image:: https://gist.github.com/jobiols/74e6d9b7c6291f00ef50dba8e68123a6/raw/fa43efd45f08a2455dd91db94c4a58fd5bd3d660/logo-jeo-150x68.jpg
   :alt: jeo Soft
   :target: https://www.jeosoft.com.ar

.. image:: https://img.shields.io/badge/license-AGPL--3-blue.png
   :target: https://www.gnu.org/licenses/agpl
   :alt: License: AGPL-3

==========
TEST V13.1
==========

Esta es una version especial de odoo con un hack en el core que al arrancar lee
un archivo dbdata.yml con la informacion de los dominios y bases de datos que
tiene que levantar.

Ejemplo de archivo


..  code-block:: yaml

    version: '1.0'
    domains:
      - database1: ['domainA.database1.com.ar', 'domainB.database1.com.ar', 'pp.com']
      - testeo13: ['testeo13.potenciarsgr.com.ar']
      - ppooiiuu: ['ppoolol11.potenciarsgr.com.ar', 'miweb.com.ar']

Este archivo haría que por ejemplo los dominios

   - domainA.database1.com.ar
   - domainB.database1.com.ar
   - pp.com

   vayan a la base database1

   y asi con los demás





|company_logo|

This module is maintained by |company|.

To contribute to this module, please
contact Jorge Obiols <jorge.obiols@gmail.com>
