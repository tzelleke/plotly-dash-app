import dash_bootstrap_components as dbc

breadcrumb = dbc.Breadcrumb(
    items=[
        {"label": "Home", "href": "/"},
        {"label": "Page 1", "href": "/page-1"},
        {"label": "Breadcrumb", "active": True},
    ],
)
