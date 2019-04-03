from .displayable import Displayable
from .record import Record


class Task(Displayable, Record):
    def __init__(self, title, id, status, position=None, completed=None, updated=None, **kwargs, ):
        super().__init__(text=title)
        self.title = title
        self.id = id
        self.status = status
        self.position = position
        self.completed = completed
        self.updated = updated

    @staticmethod
    def from_dict(dictionary):
        return Task(**dictionary)

    @staticmethod
    def create(title='', tasklist=0):
        result = Task.api().create_task(tasklist, {"title": title})
        return Task.from_dict(result)
