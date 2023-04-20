import datetime
import json
from urllib.error import HTTPError

import dash
from dash import Patch, html
from pyorbital.orbital import Orbital

try:
    satellite = Orbital("TERRA")
except HTTPError:
    satellite = None

timedelta = datetime.timedelta(seconds=3600)


def _load_data(time):
    data = {"time": time, "lat": None, "lon": None, "alt": None}
    if satellite:
        lon, lat, alt = satellite.get_lonlatalt(time)
        data = {"time": time, "lat": lat, "lon": lon, "alt": alt}

    return data


def update_metrics(n):
    style = {"padding": "5px", "fontSize": "16px"}

    if not satellite:
        return [
            html.Span("TERRA Satellite is not available", style=style),
        ]

    data = _load_data(datetime.datetime.now())

    return [
        html.Span("Longitude: {0:.2f}".format(data["lon"]), style=style),
        html.Span("Latitude: {0:.2f}".format(data["lat"]), style=style),
        html.Span("Altitude: {0:0.2f}".format(data["alt"]), style=style),
    ]


def update_graph_live(n):
    now = datetime.datetime.now()
    timerange = [now - timedelta, now + timedelta]
    data = _load_data(now)

    patch_figure = Patch()
    patch_figure["data"][0]["x"].append(data["time"])
    patch_figure["data"][0]["y"].append(data["alt"])
    patch_figure["layout"]["xaxis"]["range"] = timerange
    patch_figure["data"][1]["x"].append(data["lon"])
    patch_figure["data"][1]["y"].append(data["lat"])

    return patch_figure


def update_figure_json(figure_dict, n):
    if n > 0:
        return dash.no_update

    return json.dumps(figure_dict, indent=2)
