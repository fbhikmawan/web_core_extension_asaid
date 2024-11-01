# -*- coding: utf-8 -*-
# Copyright 2024 ASAid Group Investment - Fatchul Bari Hikmawan
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).
{
    'name': "ASAid Core Extensions",
    'summary': "Customize the core functionalities",
    'description': """
        ASAid Core Extensions is an Odoo 17 module that modifies and extends the core functionalities.
        One of the extension is about Title Customization. It changes the title to include the company name followed by the active module name, 
        enhancing the user experience by providing more context in the browser tab.
    """,
    'author': "ASAid Group Investment",
    'website': "https://www.asaidgroup.com",
    "license": "LGPL-3",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/17.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Website',
    'version': '18.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'web'],

    'assets': {
        'web.assets_backend': [
            'web_core_extension_asaid/static/src/js/title_service_extension.js',
        ],
    },

    # properties
    "application": False,
    "installable": True,
}
