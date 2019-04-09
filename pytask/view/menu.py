import curses
from . import UiList


class Menu(UiList):
    def __init__(self, tasklists):
        self._window = curses.newwin(curses.LINES-1, int(curses.COLS * 0.30))
        super().__init__(self._window, tasklists)

    def resize(self):
        self._window.resize(curses.LINES - 1, int(curses.COLS * 0.30))
        self.noutrefresh()
        curses.doupdate()
