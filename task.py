
class Task:
    def __init__(self, name, id, status):
        self.name = name
        self.id = id
        self.status = status


    def set_pos(self, y, x):
        self.y = y
        self.x = x

    def get_pos(self):
        return self.y, self.x


    def addstr(self):
        return self.y, self.x, self.name
