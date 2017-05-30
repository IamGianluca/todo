import datetime
import os

import pytest
from flask.testing import FlaskClient
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from todo import config
from todo.factory import create_app
from todo.models import Board, State, Task, User


@pytest.yield_fixture(scope='session')
def app():
    """Session-wide test Flask application."""
    app = create_app(database_uri=config.TEST_DATABASE_URI, testing=True,
                     debug=True)
    app.test_client_class = TestClient
    context = app.app_context()
    context.push()
    yield app
    context.pop()


class TestClient(FlaskClient):
    def open(self, *args, **kwargs):
        if 'json' in kwargs:
            kwargs['data'] = json.dumps(kwargs.pop('json'))
            kwargs['content_type'] = 'application/json'
        return super().open(*args, **kwargs)


@pytest.yield_fixture(scope='session')
def db(app):
    """Session-wide test database."""
    from todo.models import db as _db
    _db.create_all()
    yield _db
    _db.drop_all()


# a bug in flask-sqlalchemy prevents empty dictionaries from being correctly
# interpreted when passed as binds: http://tinyurl.com/yaaegdma
class _dict(dict):
    def __nonzero__(self):
        return True


@pytest.yield_fixture(scope='function')
def session(db):
    """Create a new database session for a test."""
    connection = db.engine.connect()
    transaction = connection.begin()

    options = dict(bind=connection, binds=_dict())
    session = db.create_scoped_session(options=options)

    db.session = session

    yield session

    transaction.rollback()
    connection.close()
    session.remove()


@pytest.fixture
def factory(db):
    from .factory import Factory
    return Factory(db)


@pytest.fixture(scope='function')
def today():
    return datetime.datetime.today() + datetime.timedelta(minutes=30)


@pytest.fixture(scope='function')
def yesterday(today):
    return today - datetime.timedelta(days=1)


@pytest.fixture(scope='function')
def tomorrow():
    return datetime.datetime.today() + datetime.timedelta(days=1)


@pytest.fixture(scope='function')
def in7days(today):
   return today + datetime.timedelta(days=7)


@pytest.fixture(scope='function')
def user():
    return User(username='luca', email='my@email.com')


@pytest.fixture(scope='function')
def another_user():
    return User(username='another', email='another@email.com')


@pytest.fixture(scope='function')
def board():
    return Board(title='board')


@pytest.fixture(scope='function')
def backlog(board):
    return State(name='backlog', board=board)


@pytest.fixture(scope='function')
def hit(board):
    return State(name='hit', board=board)


@pytest.fixture(scope='function')
def master(board):
    return State(name='master', board=board)


@pytest.fixture(scope='function')
def task(backlog, tomorrow, user, hit):
    return Task(description='service road bike', assignee=user,
                state=hit, deadline=tomorrow)
