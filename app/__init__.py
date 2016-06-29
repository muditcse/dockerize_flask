__author__ = 'smrati.katiyar@gmail.com'

from app.api_1_0.hello_views import wr

from flask import Flask

def create_app():
    app = Flask(__name__)

    app.register_blueprint(wr)

    return app