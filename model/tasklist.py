class TaskList:
    def __init__(self, title, id, tasks):
        self.title = title
        self.id = id
        self.tasks = tasks

    def set_pos(self, y, x):
        self.y = y
        self.x = x

    def get_pos(self):
        return self.y, self.x

    def addstr(self):
        return self.y, self.x, self.title
