# -*- coding: utf-8 -*-
# Big Boss is watching you! OHM v1.1
{
    'name': 'Outer Heaven Management',
    'version': '1.1',
    'summary': 'Mother Base Administration',
    'sequence': -100,
    'description': """Manage your MB members and configure your MB""",
    'category': 'Productivity',
    'website': 'https://metalgear.fandom.com/wiki/Outer_Heaven',
    # 'images' : ['images/accounts.jpeg'],
    'license': 'LGPL-3',
    'depends': [
        'sale',
        'mail'
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/member_view.xml',
        'views/kids_view.xml',
        'views/sale.xml'
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
