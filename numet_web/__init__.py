import os

from flask import Flask, render_template, send_from_directory

from . import single_variable


def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.register_blueprint(single_variable.bp)

    @app.route('/favicon.ico')
    def favicon():
        return send_from_directory(os.path.join(app.root_path, 'static'),
                                   'favicon.ico', mimetype='image/vnd.microsoft.icon')

    @app.route('/')
    def index():
        return render_template('index.html')

    return app
