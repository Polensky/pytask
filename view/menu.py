import curses
from view import UiList


class Menu(UiList):
    def __init__(self, tasklists):
        self._window = curses.newwin(curses.LINES-1, 20)
        super().__init__(self._window, tasklists)
