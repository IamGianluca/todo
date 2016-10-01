import datetime
from nose.tools import assert_equal, raises
from unittest.mock import MagicMock

from todo.task import Task


class TestTask:
    """Test suite for Task class."""

    def setUp(self):
        self.today = datetime.datetime.today() + datetime.timedelta(minutes=30)
        self.tomorrow = self.today + datetime.timedelta(days=1)
        self.in7days = self.today + datetime.timedelta(days=7)
        self.yesterday = self.today - datetime.timedelta(days=1)
        self.task = Task(body="Service bike", deadline=self.tomorrow)

    @raises(TypeError)
    def test_missing_body(self):
        """A body must be provided when creating a new task."""
        Task(deadline=self.tomorrow)

    def test_missing_deadline(self):
        """Missing deadline should be a supported feature."""
        task = Task(body="Do homeworks")
        result = task.deadline
        expected = None
        assert_equal(expected, result)

    def test_datetime_format(self):
        """Deadline should be formatted as a datetime.datetime object."""
        isinstance(self.task.deadline, datetime.datetime)

    def test_changing_deadline(self):
        """Change deadline should be supported."""
        self.task.deadline = self.in7days
        expected = self.in7days
        assert_equal(self.task.deadline, expected)

    def test_postpone_deadline(self):
        """Each time the deadline is changed a counter should be increased."""
        # starts counter at 0
        new_task = Task(body="Food shopping", deadline=self.tomorrow)
        result = new_task._postponed
        expected = 0
        assert_equal(result, expected)

        # increment by 1 each time the deadline is changed
        new_task.deadline = self.in7days
        result = new_task._postponed
        expected = 1
        assert_equal(result, expected)

        # change body shouldn't increment counter
        new_task.body = "Buy some breakfast"
        result = new_task._postponed
        expected = 1
        assert_equal(result, expected)

        # if passed deadline is same as current one, counter shouldn't
        # increment
        new_task.deadline = self.in7days
        result = new_task._postponed
        expected = 1
        assert_equal(result, expected)

        # if new deadline is before existing one, counter shouldn't increase
        new_task.deadline = self.tomorrow
        result = new_task._postponed
        expected = 1
        assert_equal(result, expected)

    def test_anticipate_deadline(self):
        """Anticipating the deadline is allowed but that shouldn't trigger the
        counter for postponed events either.
        """
        new_task = Task(body="Buy flowers for mum's birthday",
                        deadline=self.tomorrow)
        new_task.deadline = self.today

        # assert postponed events counter didn't go off
        result = new_task._postponed
        expected = 0
        assert_equal(result, expected)

    @raises(ValueError)
    def test_anticipate_deadline_yesterday(self):
        """When trying to set a new deadline that is earlier the current date
        a ValueError should be retrieved.
        """
        self.task.deadline = self.yesterday
