from flask import Flask


def create_app(database_uri, debug=False, testing=False):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = database_uri
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['TESTING'] = testing

    from todo.models import db
    db.init_app(app)

    from todo.views import todo
    app.register_blueprint(todo)

    return app
