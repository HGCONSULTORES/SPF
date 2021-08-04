# -*- coding: utf-8 -*-
# Part of GECOERP. See LICENSE file for full copyright and licensing details.

{
    'name': 'Consumo de Materiales en la Orden de Trabajo',
    'currency': 'MXN',
    'license': 'Other proprietary',
    'price': 12500.00,
    'summary': """Consumo de Materiales en la Orden de Trabajor""",
    'description': """
    Consumo de Materiales en la Orden de Trabajo
    """,
    'author': "MASTER CONSULTING RESOURCES & CO. S.C.",
    'website': "https://www.gecoerp.com",
    'support': 'contacto@gecoerp.com.com',
    'version': '4.1.5',
    'category': 'Inventory/Inventory',
    'depends': [
        'gecoerp_job_costing_management',
    ],
    'data':[
        'security/ir.model.access.csv',
        'views/stock_picking_view.xml',
        'views/project_task_view.xml',
        'views/task_report_view.xml',
        'views/consumption_type_view.xml',
        'views/stock_move_views.xml',
    ],
    'installable' : True,
    'application' : False,
}
