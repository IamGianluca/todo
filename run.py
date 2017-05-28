from todo import config
from todo.factory import create_app


if __name__ == '__main__':
    app = create_app(database_uri=config.DATABASE_URI, debug=False)
    app.run(host='0.0.0.0', debug=True)
