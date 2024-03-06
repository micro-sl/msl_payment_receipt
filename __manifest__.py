# -*- coding: utf-8 -*-
{
    'name': "msl_payment_receipt",

    'summary': """
       ----summary---""",

    'description': """
        description
    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Accounting',
    'version': '16.0',

    # any module necessary for this one to work correctly
    'depends': ['base','account'],

    # always loaded
    'data': [
        "data/report_paperformat.xml",
        'views/payment_receipt.xml',
        'report/payment_receipt_report.xml',
    ],
    "external_dependencies": {
        "python": [
            "num2words>=0.5.8",
        ],
    },    
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
}
