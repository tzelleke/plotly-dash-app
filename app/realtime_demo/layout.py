import datetime

from dash import Input, Output, callback, dcc, html
from plotly.subplots import make_subplots

from app.components.codeblock import codeblock
import app.layout.sidebar as sidebar

from . import callbacks as cb

timedelta = datetime.timedelta(seconds=3600)


def _build_figure():
    fig = make_subplots(rows=2, cols=1, vertical_spacing=0.2)
    fig["layout"]["margin"] = {"l": 30, "r": 10, "b": 30, "t": 10}
    fig["layout"]["legend"] = {"x": 0, "y": 1, "xanchor": "left"}

    fig.add_trace(
        {
            "x": [],
            "y": [],
            "name": "Altitude",
            "mode": "lines+markers",
            "type": "scatter",
        },
        row=1,
        col=1,
    )
    fig.add_trace(
        {
            "x": [],
            "y": [],
            "text": [],
            "name": "Longitude vs Latitude",
            "mode": "lines+markers",
            "type": "scatter",
        },
        row=2,
        col=1,
    )

    now = datetime.datetime.now()
    fig.update_xaxes(range=[now - timedelta, now + timedelta], row=1, col=1)
    fig.update_yaxes(range=[690, 730], row=1, col=1)
    fig.update_xaxes(range=[-190, 190], row=2, col=1)
    fig.update_yaxes(range=[-90, 90], row=2, col=1)
    fig.update_xaxes(autorange=False)

    return fig


sidebar_content = [
    html.P("Sidebar"),
]

page_content = html.Div(
    html.Div(
        [
            dcc.Interval(
                id="interval-component",
                interval=5000,
                n_intervals=0,
            ),
            html.H4("TERRA Satellite Live Feed"),
            html.Div(id="live-update-text"),
            dcc.Graph(id="live-update-graph", figure=_build_figure()),
            codeblock("figure-structure"),
        ]
    )
)

layout = sidebar.layout(
    main_content=page_content,
    sidebar_content=sidebar_content,
)

callback(
    Output("live-update-text", "children"), Input("interval-component", "n_intervals")
)(cb.update_metrics)

callback(
    Output("live-update-graph", "figure"), Input("interval-component", "n_intervals")
)(cb.update_graph_live)

callback(
    Output("figure-structure", "children"),
    Input("live-update-graph", "figure"),
    Input("interval-component", "n_intervals"),
)(cb.update_figure_json)
