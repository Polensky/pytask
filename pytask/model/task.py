class Task:
    def __init__(self, title, id, status,
                 position=None,
                 completed=None,
                 updated=None,
                 **kwargs, ):
        self.title = title
        self.id = id
        self.status = status
        self.position = position
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

    @staticmethod
    def from_dict(dictionary):
        return Task(**dictionary)
