from flask import Flask
from app.views import todo


def create_app():
    app = Flask(__name__)
    app.register_blueprint(todo)

    return app
