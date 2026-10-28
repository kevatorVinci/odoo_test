{
    "name": "Ma Bibliotheque",
    "version": "18.0.2.0.0",
    "summary": "Gestion simple de produits",
    "depends": ["base"],
    "data": [
        "security/ir.model.access.csv",
        "views/livre_views.xml",
        "wizard/reading_progress_wizard_views.xml",
        "demo/demo_data.xml",
    ],
    "demo": [
        "demo/demo_data.xml",
    ],
    "installable": True,
    "application": True,
}
