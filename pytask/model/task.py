from .displayable import Displayable
from .record import Record


class Task(Displayable, Record):
    completed, needs_action = 'completed', 'needsAction'

    def __init__(self, title, id, status, position=None, completed=None, updated=None, **kwargs, ):
        self.title = title
        self.id = id
        self.status = status
        self.position = position
        self.completed = completed
        self.updated = updated

        super().__init__(text=self.display_text)

    def switch_status(self, tasklist):
        self.status = Task.completed if self.status == Task.needs_action else Task.needs_action
        self.set_text(self.display_text)
        Task.api().update_task(tasklist, self.id, {'id': self.id, 'status': self.status})

    def change_name(self, tasklist, name):
        self.title = name
        self.set_text(self.display_text)
        Task.api().update_task(tasklist, self.id, {'id': self.id, 'title': self.title})

    @staticmethod
    def from_dict(dictionary):
        return Task(**dictionary)

    @staticmethod
    def create(title='', tasklist=0):
        result = Task.api().create_task(tasklist, {"title": title})
        return Task.from_dict(result)

    @property
    def display_text(self):
        completed = 'X' if self.status == Task.completed else 'O'
        return f'{completed} {self.title}'
