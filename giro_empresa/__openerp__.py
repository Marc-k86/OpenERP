# -*- encoding: utf-8 -*-
 
{
    "name": "Giro de la empresa",
    "version": "1.0",
    "description": """
        Permite agregar al formulario producto el campo color
    """,
    "author": "Ing. Mauricio Lopez",
    "website": "http://marck86.wordpress.com/",
    "category": "Tools",
    "depends": [
                   #"product",
            "base",#Este modulo para instalarse debe tener el modulo base y product instalado
                ],
    "data":[
            "giro_empresa_view.xml", #todos los archivos xml que posea nuestro modulo se debe de agregarse aqui
                ],
    "demo_xml": [
                        ],
    "update_xml": [
                        ],
    "active": False,
    "installable": True,
    "certificate" : "",
}
