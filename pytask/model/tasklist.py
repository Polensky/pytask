from .displayable import Displayable
from .record import Record
from .task import Task


class Tasklist(Displayable, Record):
    def __init__(self, title, id):
        super().__init__(text=title)
        self.title = title
        self.id = id

    @staticmethod
    def all():
        tasklists = []
        for tasklist in Tasklist.api().get_tasklists():
            tasklists.append(
                Tasklist(
                    title=tasklist['title'],
                    id=tasklist['id'],
                )
            )
        return tasklists
        return super().api().get_task_lists()

    @property
    def tasks(self):
        if not hasattr(self, '_tasks'):
            tasks = Tasklist.api().get_tasks(list_id=self.id)
            if 'items' not in tasks:
                return []
            self._tasks = [Task.from_dict(task) for task in tasks['items']]
        return self._tasks
