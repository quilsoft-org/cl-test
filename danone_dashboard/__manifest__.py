# -*- coding: utf-8 -*-
{
    'name': "Dashboard de Monitoreo SAP (Mockup)",

    'summary': """
        Muestra un dashboard con gráficos tipo Grafana para monitorear datos.
        Mockup desarrollado con OWL.
    """,

    'description': """
        Este módulo es un mockup que demuestra cómo construir un dashboard interactivo
        con el Odoo Web Library (OWL). Muestra gráficos de series temporales para
        diferentes entidades y permite cambiar el rango de tiempo de visualización.
    """,

    'author': "Gemini",
    'website': "https://www.google.com",
    'category': 'Productivity',
    'version': '17.0.1.0.0',

    'depends': ['web'],

    'assets': {
        'web.assets_backend': [
            # Inclusión de la librería Chart.js y su adaptador de fechas
            'https://cdn.jsdelivr.net/npm/chart.js/dist/chart.umd.min.js',
            'https://cdn.jsdelivr.net/npm/chartjs-adapter-date-fns/dist/chartjs-adapter-date-fns.bundle.min.js',

            # Archivos JS del módulo
            'sap_monitoring_dashboard/static/src/services/mock_data_service.js',
            'sap_monitoring_dashboard/static/src/components/chart_renderer/chart_renderer.js',
            'sap_monitoring_dashboard/static/src/components/dashboard/dashboard.js',
            'sap_monitoring_dashboard/static/src/main.js',

            # Archivos XML (templates OWL) del módulo
            'sap_monitoring_dashboard/static/src/components/chart_renderer/chart_renderer.xml',
            'sap_monitoring_dashboard/static/src/components/dashboard/dashboard.xml',
        ],
    },
    'installable': True,
    'application': True,
}