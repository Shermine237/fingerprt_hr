{
    'name': 'Pointeur HR',
    'version': '14.0.1.0.0',
    'summary': 'Extension du module de présences',
    'description': """
        Ce module étend les fonctionnalités du module de présences d'Odoo 14.
        Il permet d'ajouter des fonctionnalités supplémentaires pour la gestion des présences.
    """,
    'category': 'Human Resources',
    'author': 'Shermine237',
    'website': '',
    'depends': [
        'hr_attendance',
        'hr',
        'mail',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/pointeur_attendance_type_data.xml',
        'views/pointeur_location_views.xml',
        'views/pointeur_import_views.xml',
        'views/pointeur_attendance_type_views.xml',
        'views/hr_attendance_views.xml',
        'views/hr_employee_views.xml',
        'views/hr_attendance_report_views.xml',
        'views/pointeur_hr_menus.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
