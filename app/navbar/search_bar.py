import dash_bootstrap_components as dbc

search_bar = dbc.InputGroup(
    [
        dbc.Input(type="search", size="sm", placeholder="Search"),
        dbc.Button("Search", color="secondary", size="sm", n_clicks=0),
    ],
    class_name="ms-4 me-auto mt-3 mt-md-0",
    style={"maxWidth": "24rem"},
)
