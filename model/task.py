class Task:
    def __init__(self, title, id, status,
                 notes=None,
                 position=None,
                 completed=None,
                 updated=None,
                 **kwargs, ):
        self.title = title
        self.id = id
        self.status = status
        self.postion = position
        self.completed = completed
        self.updated = updated

    def set_pos(self, y, x):
        self.y = y
        self.x = x

    def get_pos(self):
        return self.y, self.x

    def addstr(self):
        return self.y, self.x, self.title

    @classmethod
    def from_dict(cls, dictionary):
        return cls(**dictionary)
