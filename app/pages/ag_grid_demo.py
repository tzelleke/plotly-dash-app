from dash import register_page

from app.ag_grid_demo.layout import layout

register_page(__name__, path="/ag-grid-demo", layout=layout)
