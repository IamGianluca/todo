import uuid


class List(object):
    """A collection of tasks.

    Attr:
        id_: [uuid.uuid4] A unique identifier for the list.
        __tasks: [dict] A dictionary of tasks associated to the list, indexed
        by task id.
    """
    # NOTE: inherit from collections.abc.Sequence instead of creating an
    # interface for a dictionary
    def __init__(self, tasks=None):
        """Instantiate a List object.

        Args:
            tasks: [list] A list of tasks that will be included in the List
            object.
        """
        self.id_ = uuid.uuid4()
        self.tasks = tasks

    @property
    def tasks(self):
        """Getter method for the tasks instance variable.

        Returns:
            [dict] All tasks currently in the list.
        """
        # TODO: would it be better to return the values of the dictionary
        # instead and have an additional method to return the ids?
        return self.__tasks

    @tasks.setter
    def tasks(self, tasks):
        """Setter method for the tasks instance variable.

        Args:
            tasks: [dict] Tasks that need to be added to the List object at the
            construction time.
        Side effects:
            Update the __tasks instance variable status.
        """
        if tasks is None:
            self.__tasks = {}
        else:
            self.__tasks = {task.id_: task for task in tasks}

    def __len__(self):
        """Length of the List object.

        Returns:
            [int] The number of Tasks included in the List at the current time.
        """
        return sum(1 for n in self.tasks.keys())

    def add(self, tasks):
        """Add new Tasks to the List.

        Args:
            tasks: [list] New tasks to be added to the List.
        Side effects:
            Add a new element to the self.__tasks dictionary.
        """
        for task in tasks:
            self.__tasks[task.id_] = task

    def remove(self, ids):
        """Remove elements from the List.

        Args:
            ids: [list] The ids of the Tasks that need to be removed from the
            List object.
        Side effects:
            Remove the elements corresponding to the ids provided in the
            method call from the self.__tasks dictionary.
        """
        for id_ in ids:
            del self.__tasks[id_]

    def values(self):
        """Retrieve a view of the Tasks from the List.

        Returns:
            [list] All items currently included in the List.
        """
        return [t for t in self.__tasks.values()]
