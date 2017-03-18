import datetime

import pytest

from todo.task import Task


class TestTask:
    """Automated tests for Task class."""

    def test_missing_body(self, tomorrow):
        """A body must be provided when creating a new task."""
        with pytest.raises(TypeError):
            Task(deadline=tomorrow)

    def test_missing_deadline(self):
        """Missing deadline should be a supported feature."""
        task = Task(body="Do homeworks")
        assert task.deadline == None

    def test_datetime_format(self, task1):
        """Deadline should be formatted as a datetime.datetime object."""
        assert isinstance(task1.deadline, datetime.datetime)

    def test_changing_deadline(self, task1, in7days):
        """Change deadline should be supported."""
        task1.deadline = in7days
        assert task1.deadline == in7days

    def test_postpone_deadline(self, task1, tomorrow, in7days):
        """Each time the deadline is changed a counter should be increased."""
        # starts counter at 0
        assert task1._postponed == 0

        # increment by 1 each time the deadline is changed
        task1.deadline = in7days
        assert task1._postponed == 1

        # change body shouldn't increment counter
        task1.body = "Buy some breakfast"
        assert task1._postponed == 1

        # if passed deadline is same as current one, counter shouldn't
        # increment
        task1.deadline = in7days
        assert task1._postponed == 1

        # if new deadline is before existing one, counter shouldn't increase
        task1.deadline = tomorrow
        assert task1._postponed == 1

    def test_anticipate_deadline(self, task1, today):
        """Anticipating the deadline is allowed but that shouldn't trigger the
        counter for postponed events either.
        """
        task1.deadline = today

        # assert postponed events counter didn't go off
        assert task1._postponed == 0

    def test_anticipate_deadline_yesterday(self, task1, yesterday):
        """When trying to set a new deadline that is earlier the current date
        a ValueError should be retrieved.
        """
        with pytest.raises(ValueError):
            task1.deadline = yesterday
