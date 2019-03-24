class Task:
    def __init__(self, title, id, status,
                 notes=None,
                 position=None,
                 completed=None,
                 updated=None,):
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
        title = dictionary['title']
        id = dictionary['id']
        status = dictionary['status']
        position = dictionary['position']
        notes = dictionary['notes'] if 'notes' in dictionary else None
        completed = dictionary['completed'] if 'completed' in dictionary else None
        updated = dictionary['updated']
        return cls(title, id, status, notes, position, completed, updated)

