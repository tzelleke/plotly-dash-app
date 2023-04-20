from dash import html


def sidebar(children):
    return html.Div(
        children,
        className="bg-light",
        style={
            "position": "fixed",
            "top": "56px",
            "left": 0,
            "bottom": 0,
            "width": "16rem",
            "padding": "2rem 1rem",
        },
    )
