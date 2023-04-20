from dash import html
import dash_bootstrap_components as dbc

user_settings = dbc.Nav(
    dbc.DropdownMenu(
        [
            dbc.DropdownMenuItem("demo@example.com", header=True),
            dbc.DropdownMenuItem("Settings", active=False, href="/settings"),
            dbc.DropdownMenuItem("Logout", active=False, href="#"),
        ],
        nav=True,
        in_navbar=True,
        label=html.I(className="bi bi-person-circle"),
        caret=True,
        align_end=True,
        # toggle_style=dict(lineHeight=1),
    ),
)
