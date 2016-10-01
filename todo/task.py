import datetime
import uuid


class Task(object):

    def __init__(self, body, deadline=None):
        self.id_ = uuid.uuid4()
        self.body = body
        self.deadline = deadline

    @property
    def deadline(self):
        return self.__deadline

    @deadline.setter
    def deadline(self, new_deadline):
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
