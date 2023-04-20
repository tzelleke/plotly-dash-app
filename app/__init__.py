from flask import Flask

from .main import create_dash_app


def create_app():
    flask_app = Flask(__name__, instance_relative_config=False)
    dash_app = create_dash_app()
    dash_app.init_app(flask_app)
    dash_app.enable_dev_tools()

    return flask_app
