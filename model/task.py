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
        self.y, self.x = 0, 0


    @property
    def pos(self):
        return self.y, self.x

    @pos.setter
    def pos(self, position):
        self.y, self.x = position

    def addstr(self):
        return self.y, self.x, self.title

    @classmethod
    def from_dict(cls, dictionary):
        return cls(**dictionary)
