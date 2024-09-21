# -*- coding: utf-8 -*-
{
    'name': "Personalizacion del Pedido de Ventas",

    'summary': """
        Agrega un botón que permite crear la factura directamente desde la orden de venta sin necesidad de abrir el wizard.""",

    'description': """
        Este módulo añade un botón en las órdenes de venta que permite crear facturas directamente, evitando el uso del wizard predeterminado de Odoo.
    """,

    'author': "Mario Roberto",
    'website': "https://mrgomezsv.github.io/",

    'category': 'Sales',
    'version': '16.0',

    # Módulos necesarios para el funcionamiento
    'depends': ['base', 'sale'],

    # Archivos de datos siempre cargados
    'data': [
        'views/sale_order.xml',
    ],
}
