from dataclasses import dataclass


@dataclass
class Displayable:
    '''Classes which are displayable by ncurse.'''
    x: int = 0
    y: int = 0
    title: str = ''

    @property
    def pos(self):
        return self.y, self.x

    @pos.setter
    def pos(self, position):
        self.y, self.x = position

    def addstr(self):
        return self.y, self.x, self.title
