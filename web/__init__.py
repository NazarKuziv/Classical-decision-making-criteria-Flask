from flask import Flask
from os import path, urandom


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = urandom(24)
    
    from .views import views
    app.register_blueprint(views, url_prefix='/')
    
    return app