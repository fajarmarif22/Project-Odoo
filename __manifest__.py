# -*- coding: utf-8 -*-
{
    'name': "odoo_training",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """
Long description of module's purpose
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mail', 'stock', 'sale_management'],

    # always loaded
    'data': [
        'report/report_action.xml',
        'report/report_training_session.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        # 'views/views.xml',
        # 'views/templates.xml',
        'data/sequence_data.xml',
        'data/scheduler_data.xml', 
        'views/view_training.xml',
        'views/partner_view.xml',
        'wizard/training_wizard_view.xml',
        'views/menuitem_view.xml',
        'data/data.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
}

