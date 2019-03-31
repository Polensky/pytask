from .displayable import Displayable


class Task(Displayable):
    def __init__(self, title, id, status,
                 position=None,
                 completed=None,
                 updated=None,
                 **kwargs, ):
        super().__init__(title=title)
        self.id = id
        self.status = status
        self.position = position
        self.completed = completed
        self.updated = updated

    @staticmethod
    def from_dict(dictionary):
        return Task(**dictionary)
