import pytest
import requests

from todo.models import Base, Board, State, Task, User


def test_api_health():
    # when
    response = requests.get('http://docker_app_2:5000/')

    # then
    assert response.ok == True

def test_get_tasks():
    # when
    response = requests.get('http://docker_app_1:5000/todo/api/v1.0/tasks')

    # then
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json'
    assert response.json() == {'task': 1}
