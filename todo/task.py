import datetime
import uuid


class Task(object):
    """An activity that needs to be accomplished by a deadline.

    Attr:
        id_: [uuid.uuid4] Unique identifier for the task.
        body: [str] The description of the task.
        __deadline: [str] The deadline.
        _postponed: [int] Counter for times the task got postponed.
    """

    def __init__(self, body, deadline=None):
        """Instantiate a new task.

        Args:
            body: [str] The description of the task.
            (deadline): [datetime.datetime] The deadline."""
        self.id_ = uuid.uuid4()
        self.body = body
        self.deadline = deadline

    @property
    def deadline(self):
        """Return deadline.

        Side effects:
            Returns the task deadline.
        """
        return self.__deadline

    @deadline.setter
    def deadline(self, new_deadline):
        """Set deadline.

        Args:
            new_deadline: [datetime.datetime] The deadline.
        Raises:
            ValueError if *new_deadline* is smaller than current datetime.
        Side effects:
            Update deadline and increment counter for times the task got
            postponed if *new_deadline* is greater than current deadline.
        """
        if new_deadline is None:
            self.__deadline = None
        else:
            if new_deadline < datetime.datetime.today():
                raise ValueError("Deadline should not be earlier than "\
                                 "the current datetime")

            # increment counter if postponing task
            if hasattr(self, "_postponed"):
                if self.deadline < new_deadline:
                    self._postponed += 1
                else:
                    pass
            else:
                self._postponed = 0
            self.__deadline = new_deadline
