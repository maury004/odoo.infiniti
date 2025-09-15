{
    "name": "Support Ticket ITIL",
    "version": "1.0",
    "category": "Support",
    "summary": "Module for managing support tickets based on ITIL best practices.",
    "author": "Your Name",
    "depends": ["base"],
    "data": [
        "security/ir.model.access.csv",
        "views/menu_views.xml",
        "views/incident_views.xml",
        "views/service_request_views.xml",
        "views/problem_views.xml",
        "views/change_control_views.xml",
        "data/ticket_sequence.xml"
    ],
    "installable": True,
    "application": True,
    "auto_install": False
}