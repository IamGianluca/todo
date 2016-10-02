import datetime
from nose.tools import assert_equal

from todo.list import List
from todo.task import Task


class TestList:
    """Test suite for List class."""

    def setUp(self):
         self.tomorrow = datetime.datetime.today() + datetime.timedelta(days=1)
         self.task1 = Task(body="Buy some ham", deadline=self.tomorrow)
         self.task2 = Task(body="Check in for flight to Paris",
                           deadline=self.tomorrow)

    def test_empty_list(self):
        """The supported ways of creating empty lists is without passing any
        argument when constructing the list, or passing either an empty list
        or a None object.
        """
        mylist = List(tasks=[])
        mylist2 = List(tasks=None)
        mylist3 = List()

    def test_add_task(self):
        # check current length
        hit_list = List(tasks=[self.task1, self.task2])
        result = len(hit_list)
        expected = 2
        assert_equal(result, expected)

        # add new task
        task3 = Task(body="Make reservation at Les Francis",
                     deadline=self.tomorrow)
        hit_list.add(tasks=[task3])
        result = len(hit_list)
        expected = 3
        assert_equal(result, expected)

        # check ids
        result = set([i.id_ for i in hit_list.values()])
        expected = set([i.id_ for i in [self.task1, self.task2, task3]])
        assert_equal(result, expected)

    def test_add_multiple_tasks(self):
        """Adding multiple tasks at once should be supported."""
        new_list = List()
        new_list.add(tasks=[self.task1, self.task2])
        result = len(new_list)
        expected = 2
        assert_equal(result, expected)

        result = set([t.id_ for t in new_list.tasks.values()])
        expected = set([t.id_ for t in [self.task1, self.task2]])
        assert_equal(result, expected)

    def test_remove_task(self):
        # check current length
        hit_list = List(tasks=[self.task1, self.task2])
        result = len(hit_list)
        expected = 2
        assert_equal(result, expected)

        # remove task
        hit_list.remove(ids=[self.task2.id_])
        result = len(hit_list)
        expected = 1
        assert_equal(result, expected)

        # check ids
        result = set([i.id_ for i in hit_list.values()])
        expected = set([self.task1.id_])
        assert_equal(result, expected)

    def test_remove_multiple_tasks(self):
        new_list = List()
        new_list.add(tasks=[self.task1, self.task2])
        new_list.remove(ids=[self.task1.id_, self.task2.id_])
        result = len(new_list)
        expected = 0
        assert_equal(result, expected)

        result = set([t.id_ for t in new_list.tasks.values()])
        expected = set([])
        assert_equal(result, expected)
