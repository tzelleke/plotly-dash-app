import dash_bootstrap_components as dbc

nav = dbc.Nav(
    [
        dbc.NavItem(dbc.NavLink("Home", active="exact", href="/")),
        dbc.NavItem(
            dbc.NavLink(
                "Gapfinder Demo",
                active="exact",
                href="/gapfinder-demo",
                class_name="text-nowrap",
            )
        ),
        dbc.NavItem(
            dbc.NavLink(
                "Realtime Demo",
                active="exact",
                href="/realtime-demo",
                class_name="text-nowrap",
            )
        ),
        dbc.NavItem(
            dbc.NavLink(
                "AG Grid Demo",
                active="exact",
                href="/ag-grid-demo",
                class_name="text-nowrap",
            )
        ),
    ],
    class_name="me-auto",
)
