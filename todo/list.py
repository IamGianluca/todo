import uuid


class List(object):
    """A list."""

    def __init__(self, tasks=None):
        self.id_ = uuid.uuid4()
        self.tasks = tasks

    @property
    def tasks(self):
        return self.__tasks

    @tasks.setter
    def tasks(self, tasks):
        if tasks is None:
            self.__tasks = {}
        else:
            self.__tasks = {task.id_: task for task in tasks}

    def __len__(self):
        return sum(1 for n in self.tasks.keys())

    def add(self, tasks):
        for task in tasks:
            self.__tasks[task.id_] = task

    def remove(self, ids):
        for id_ in ids:
            del self.__tasks[id_]

    def values(self):
        return [t for t in self.__tasks.values()]