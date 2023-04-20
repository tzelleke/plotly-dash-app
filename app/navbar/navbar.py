from dash import Input, Output, State, callback, html
import dash_bootstrap_components as dbc

from .nav import nav

# from .search_bar import search_bar
from .social_links import social_links
from .user_settings import user_settings

PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"

navbar_brand = html.A(
    dbc.Row(
        [
            dbc.Col(html.Img(src=PLOTLY_LOGO, height="30px")),
            dbc.Col(dbc.NavbarBrand("Plotly Dash Demo", class_name="ms-2")),
        ],
        align="center",
        class_name="g-0",
    ),
    href="/",
    style={"textDecoration": "none"},
)

# <li class="nav-item py-2 py-lg-1 col-12 col-lg-auto"></li>
separator = dbc.Nav(
    dbc.NavItem(
        [
            html.Div(className="vr d-none d-lg-flex h-100 mx-lg-2 text-white"),
            html.Hr(className="d-lg-none my-2 text-white-50"),
        ]
    ),
)

navbar = dbc.Navbar(
    dbc.Container(
        [
            navbar_brand,
            dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
            dbc.Collapse(
                [
                    nav,
                    # search_bar,
                    social_links,
                    separator,
                    user_settings,
                ],
                id="navbar-collapse",
                is_open=False,
                navbar=True,
            ),
        ],
        fluid=True,
    ),
    color="primary",
    dark=True,
    fixed="top",
    class_name="py-2",
)


@callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open
