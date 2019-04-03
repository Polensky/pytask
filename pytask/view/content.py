import curses
from . import UiList


class Content(UiList):
    def __init__(self, tasks):
        self._window = curses.newwin(curses.LINES-1, curses.COLS-20, 0, 20)
        super().__init__(self._window, tasks)
