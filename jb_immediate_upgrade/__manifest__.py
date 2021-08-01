{
    'name': 'Immediate Upgrade Module',
    'summary': 'This Module Help to Upgrade Module Immediately',
    'author': 'Joyanto Barmon',
    'license': 'AGPL-3',
    'website': 'http://examples.com.bd/',
    'category': 'Tools',
    'sequence': 1,
    'version': '13.0.1.0.0',
    'depends': [
        'base'
    ],
    'data': [
        # 'data/sale_order_mail_template.xml',
        'security/res_groups.xml',
        'views/ir_inherit_module_view.xml'
    ],
    'images': ['static/description/icon.png'],
    'installable': True,
    'application': True,
    'auto_install': False,
}