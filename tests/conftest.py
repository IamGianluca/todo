import datetime

import pytest

from todo.task import Task


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
def task1(tomorrow):
    return Task(body="Buy some ham", deadline=tomorrow)

@pytest.fixture(scope='function')
def task2(tomorrow):
    return Task(body="Check in for flight to Paris",
                deadline=tomorrow)
