import curses
from . import UiList


class Content(UiList):
    def __init__(self, tasks):
        width = int(curses.COLS * 0.70)
        x = curses.COLS - width
        self._window = curses.newwin(curses.LINES-1, width, 0, x)
        super().__init__(self._window, tasks)

    def resize(self):
        self._window.resize(curses.LINES - 1, int(curses.COLS * 0.70))
        self.noutrefresh()
        curses.doupdate()
