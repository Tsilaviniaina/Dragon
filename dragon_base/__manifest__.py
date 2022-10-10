# -*- coding: utf-8 -*-
{
    'name': "dragon_base",

    'summary': """
     Description de module""",

    'description': """
       Description longue de module
    """,

    'author': "Kasia",
    'website': "http://Kasia.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/student_base_views.xml',
        'views/student_class_views.xml',
        'views/professor_base_views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
