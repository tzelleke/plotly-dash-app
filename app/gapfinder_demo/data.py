import pandas as pd

URL = (
    "https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv"
)

df = pd.read_csv(URL)
