import plotly.express as px
import plotly.io as pio

from .data import df

pio.templates.default = "seaborn"


def update_graph(value):
    return px.line(
        df[df.country == value],
        x="year",
        y="pop",
    )
