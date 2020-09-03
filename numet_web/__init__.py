from flask import Flask
from . import single_variable


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.register_blueprint(single_variable.bp)
    return app
