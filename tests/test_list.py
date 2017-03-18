import datetime

import pytest

from todo.list import List
from todo.task import Task


class TestList:
    """Automated tests for List class."""

    def test_empty_list(self):
        """An empty list can be created:
        - Not passing any argument when constructing the list.
        - Passing an empty list.
        - Passing a None object.
        """
        mylist = List(tasks=[])
        mylist2 = List(tasks=None)
        mylist3 = List()

    def test_add_task(self, task1, task2, tomorrow):
        """A task can be added to an existing live using the *add* method."""
        # check current length
        hit_list = List(tasks=[task1, task2])
        result = len(hit_list)
        expected = 2
        assert result == expected

        # add new task
        task3 = Task(body="Make reservation at Les Francis",
                     deadline=tomorrow)
        hit_list.add(tasks=[task3])
        result = len(hit_list)
        expected = 3
        assert result == expected

        # check ids
        result = set([i.id_ for i in hit_list.values()])
        expected = set([i.id_ for i in [task1, task2, task3]])
        assert result == expected

    def test_add_multiple_tasks(self, task1, task2):
        """Multiple tasks can be added to an existig passing a list of *Task*s
        to the *add* method.
        """
        new_list = List()
        new_list.add(tasks=[task1, task2])
        result = len(new_list)
        expected = 2
        assert result == expected

        result = set([t.id_ for t in new_list.tasks.values()])
        expected = set([t.id_ for t in [task1, task2]])
        assert result == expected

    def test_remove_task(self, task1, task2):
        """A task can be removed from a list using the *remove* method."""
        # check current length
        hit_list = List(tasks=[task1, task2])
        result = len(hit_list)
        expected = 2
        assert result == expected

        # remove task
        hit_list.remove(ids=[task2.id_])
        result = len(hit_list)
        expected = 1
        assert result == expected

        # check ids
        result = set([i.id_ for i in hit_list.values()])
        expected = set([task1.id_])
        assert result == expected

    def test_remove_multiple_tasks(self, task1, task2):
        """Multiple tasks can be removed from an existing list proving a list
        of ids to the *remove* method.
        """
        new_list = List()
        new_list.add(tasks=[task1, task2])
        new_list.remove(ids=[task1.id_, task2.id_])
        result = len(new_list)
        expected = 0
        assert result == expected

        result = set([t.id_ for t in new_list.tasks.values()])
        expected = set([])
        assert result  == expected
