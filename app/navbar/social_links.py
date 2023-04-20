from dash import html
import dash_bootstrap_components as dbc

social_links = dbc.Nav(
    [
        dbc.NavItem(
            dbc.NavLink(
                html.I(className="bi bi-github"),
                href="https://github.com/tzelleke",
                class_name="text-nowrap",
            ),
        ),
        dbc.NavItem(
            dbc.NavLink(
                html.I(className="bi bi-twitter"),
                href="https://github.com/tzelleke",
                class_name="text-nowrap",
            ),
        ),
    ]
)
