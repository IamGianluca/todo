from flask import url_for
import pytest

from todo.models import Board, State, Task, User


def test_api_health(client):
    assert client.get(url_for('todo.check_health')).status_code == 200

def test_get_tasks(client):
    # when
    response = client.get(url_for('todo.get_tasks'))

    # then
    assert response.status_code == 200
    assert response.headers['Content-Type'] == 'application/json'
    assert response.json == {'task': 1}


class TestRoutes:

    def test_retrieve_task(self, client, session, task):
        # given
        session.add(task)
        session.commit()
        assert len(Task.query.all()) == 1

        # when
        response = client.get(url_for('todo.get_task', task_id=1))

        # then
        assert response.status_code == 200
        assert response.json == {
            'json_list': [{
                'id': task.id,
                'description': task.description
            }]
        }

    # def test_retrieve_users(session, user):
        # """Given a user exists in the database, we should be able to retrieve
        # its details from the API.
        # """
        # # given

        # # when

        # # then


    # def test_add_user(session, user):
        # """Given a user doesn't exist in the database, we should be able to
        # create it from the API.
        # """
        # pass

    # def test_remove_user(session, user):
        # """Given a user exists in the database, we should be able to remove it
        # from the API.
        # """
        # pass

    # def test_create_task(session, task):
        # """Given a task doesn't exist in the board, we should be able to create
        # it.
        # """
        # pass

    # def test_assign_task(session, task, user):
        # """Given an existing unassigned task, we should be able to assign it to
        # a given user.
        # """
        # pass

    # def test_change_assignee(session, task, another_user):
        # """Given a task already assigned to a user, we should be able to
        # re-assign it to another user.
        # """
        # pass
