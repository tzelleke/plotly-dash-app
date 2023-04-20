from dash import html, register_page
import dash_bootstrap_components as dbc

from app.components.breadcrumb import breadcrumb

register_page(__name__, path="/settings")

layout = dbc.Container(
    [
        breadcrumb,
        html.H1("This is the Settings page"),
        html.Div(
            """
            This is Settings content.
        """
        ),
    ],
    fluid=True,
)
