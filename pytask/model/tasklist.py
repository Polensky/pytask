from .displayable import Displayable


class TaskList(Displayable):
    def __init__(self, title, id, tasks):
        super().__init__(title=title)
        self.title = title
        self.id = id
        self.tasks = tasks
