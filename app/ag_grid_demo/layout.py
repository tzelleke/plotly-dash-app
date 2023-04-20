from dash import Input, Output, callback, html
import dash_ag_grid as dag
import pandas as pd

import app.layout.sidebar as sidebar

from . import callbacks as cb

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/solar.csv")

grid = dag.AgGrid(
    id="quickstart-grid",
    rowData=df.to_dict("records"),
    columnDefs=[{"field": i} for i in df.columns],
    defaultColDef={
        "resizable": True,
        "sortable": True,
        "filter": True,
        "minWidth": 125,
    },
    columnSize="sizeToFit",
)

sidebar_content = [
    html.P("A simple sidebar layout with navigation links", className="lead"),
]

page_content = [
    html.H1(
        [
            "Title of Dash App",
            grid,
        ],
        style={"textAlign": "center"},
    ),
]

layout = sidebar.layout(
    main_content=page_content,
    sidebar_content=sidebar_content,
)

callback(
    Output("quickstart-output", "children"), Input("quickstart-grid", "cellClicked")
)(cb.display_cell_clicked_on)
