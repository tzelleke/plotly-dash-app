from dash import html

from app.components.sidebar import sidebar


def layout(main_content, sidebar_content):
    return html.Div(
        [
            sidebar(sidebar_content),
            html.Div(
                main_content,
                style={
                    "marginLeft": "18rem",
                    "marginRight": "2rem",
                    "padding": "2rem 1rem",
                },
            ),
        ],
    )
