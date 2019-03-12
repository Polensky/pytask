
class TaskList:
    def __init__(self, name, id):
        self.name = name
        self.id = id


    def set_pos(self, y, x):
        self.y = y
        self.x = x

    def get_pos(self):
        return self.y, self.x


    def addstr(self):
        return self.y, self.x, self.name
