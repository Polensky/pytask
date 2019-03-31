import curses


class BottomText:
    def __init__(self):
        self._window = curses.newwin(1, curses.COLS, curses.LINES - 1, 0)
        self._window.addstr(0,0,'use <j> <k> to navigate the menu')
        self.noutrefresh()
        curses.doupdate()

    def redraw(self):
        self._window.addstr(0,0,'use <j> <k> to navigate the menu')
        self.noutrefresh()
        curses.doupdate()


    def __getattr__(self, attr_name):
        return getattr(self._window, attr_name)
