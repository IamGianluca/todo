from todo.models import Task


class Factory:

    def __init__(self, db):
        self.db = db

    def create_task(self):
        """Create task fixture."""
        task = Task(description='learn something new')
        self.db.session.add(task)
        self.db.session.commit()
