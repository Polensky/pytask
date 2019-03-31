class TaskList:
    def __init__(self, title, id, tasks):
        self.title = title
        self.id = id
        self.tasks = tasks

    @property
    def pos(self):
        return self.y, self.x

    @pos.setter
    def pos(self, value):
        self.y, self.x = value

    def addstr(self):
        return self.y, self.x, self.title
