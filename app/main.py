from dash import Dash, html, page_container
import dash_bootstrap_components as dbc

from .navbar import navbar

DBC_CSS = (
    "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@V1.0.2/dbc.min.css"
)


def layout():
    return html.Div(
        [
            navbar.navbar,
            page_container,
        ]
    )


def create_dash_app(server=False):
    app = Dash(
        __name__,
        server=server,
        use_pages=True,
        external_stylesheets=[
            dbc.themes.FLATLY,
            dbc.icons.BOOTSTRAP,
            DBC_CSS,
        ],
    )
    app.config.suppress_callback_exceptions = True
    app.layout = layout

    return app
