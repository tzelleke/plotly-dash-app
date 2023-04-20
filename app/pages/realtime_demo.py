from dash import register_page

from app.realtime_demo.layout import layout

register_page(__name__, path="/realtime-demo", layout=layout)
