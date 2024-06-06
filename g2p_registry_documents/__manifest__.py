# Part of OpenG2P. See LICENSE file for full copyright and licensing details.
{
    "name": "G2P Registry: Documents",
    "category": "G2P",
    "version": "17.0.1.0.0",
    "sequence": 1,
    "author": "OpenG2P",
    "website": "https://openg2p.org",
    "license": "Other OSI approved licence",
    "development_status": "Alpha",
    "depends": [
        "g2p_documents",
        "g2p_registry_base",
    ],
    "data": [
        "views/registrant_document_views.xml",
    ],
    "assets": {
        "web.assets_backend": [
            "static/src/js/preview_document.js",
        ],
    },
    "external_dependencies": {"python": ["python-magic==0.4.27"]},
    "demo": [],
    "images": [],
    "application": True,
    "installable": True,
    "auto_install": False,
}
