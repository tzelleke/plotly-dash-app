from dash import register_page

from app.gapfinder_demo.layout import layout

register_page(__name__, path="/gapfinder-demo", layout=layout)
