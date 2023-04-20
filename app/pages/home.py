from dash import html, register_page
import dash_bootstrap_components as dbc

register_page(__name__, path="/")

layout = dbc.Container(
    [
        html.H1("This is our Home page"),
        html.Div(
            """
            This is our Home page content.
        """
        ),
    ],
    fluid=True,
)
