import curses


class Menu:

    def __init__(self):
        self._window = curses.newwin(curses.LINES-1,20)
        self._window.box()

        self._cur_pos = 0

    def __getattr__(self, attr_name):
        return getattr(self._window, attr_name)

