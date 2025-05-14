{
    'name': 'TrackPOS Installation',
    'version': '1.0',
    'summary': 'Registro de órdenes de instalación GPS',
    'author': 'Tu Nombre o Empresa',
    'category': 'Sales',
    'depends': ['base', 'sale', 'hr', 'contacts'],
    'data': [
        'security/ir.model.access.csv',
        'views/installation_order_views.xml',
    ],
    'installable': True,
    'application': True,
}
