from dash import Input, Output, callback, dcc, html
import dash_bootstrap_components as dbc

import app.layout.sidebar as sidebar

from . import callbacks as cb
from .data import df

sidebar_content = [
    html.P("A simple sidebar layout with navigation links", className="lead"),
    dbc.Nav(
        [
            dbc.NavLink("Subpage 1", href="#", active="exact", class_name="fw-bold"),
            dbc.NavLink("Subpage 2", href="#", active="exact", class_name="fw-bold"),
            dbc.NavLink("Subpage 3", href="#", active="exact", class_name="fw-bold"),
        ],
        vertical=True,
        pills=True,
    ),
]

_dropdown = dcc.Dropdown(
    df.country.unique(),
    "Canada",
    id="dropdown-selection",
    className="dbc",
)

_graph = dcc.Graph(id="graph-content")

page_content = [
    html.H1(children="Title of Dash App", style={"textAlign": "center"}),
    _dropdown,
    _graph,
]

layout = sidebar.layout(
    main_content=page_content,
    sidebar_content=sidebar_content,
)

callback(
    Output(_graph, "figure"),
    Input(_dropdown, "value"),
)(cb.update_graph)
