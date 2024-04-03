{
    'name' : 'MSP Document ID',
    'author' : 'stevenmorizon (stevenmorizon123@gmail.com)',
    'summary' : 'Module For Documents ID',
    'depends' : ["base","web"],
    'data' : [
                "security/ir.model.access.csv",
                "views/menu_msp_documents_id.xml",
                "views/views_msp_documents_id.xml",

    ],
    'license' : 'LGPL-3',
    'category' : 'Documents',

    'auto_install' : False,
    'application' : True,
    'installable' :True,

}