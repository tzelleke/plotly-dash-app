from dash import html


def codeblock(component_id, children=None):
    if not children:
        children = []

    return html.Pre(
        children=children,
        id=component_id,
        style={
            "border": "thin lightgrey solid",
            "overflowY": "scroll",
            "height": "275px",
        },
    )
