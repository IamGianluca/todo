import datetime
import os

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from todo.models import Base, Board, State, Task, User


TESTDB = 'testdb'
TESTDB_PATH = os.path.join('5432', TESTDB)
TESTDB_URI = 'postgresql://docker:changeme@db:' + TESTDB_PATH


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

@pytest.fixture(scope='session')
def engine():
    return create_engine(TESTDB_URI)

@pytest.yield_fixture(scope='session')
def tables(engine):
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    yield
    Base.metadata.drop_all(engine)

@pytest.yield_fixture
def session(engine, tables):
    connection = engine.connect()
    transaction = connection.begin()
    session = Session(bind=connection)

    yield session

    session.close()
    transaction.rollback()
    connection.close()

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

