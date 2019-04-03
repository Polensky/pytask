import curses


class BottomText:
    def __init__(self):
        self._window = curses.newwin(1, curses.COLS, curses.LINES - 1, 0)
        self.default_text = 'use <j> <k> to navigate the menu'
        self.text = ''
        self.redraw()

    def redraw(self):
        self._window.clear()
        self._window.addstr(0, 4, self.text if len(self.text) > 0 else self.default_text)
        self.noutrefresh()
        curses.doupdate()

    def __getattr__(self, attr_name):
        return getattr(self._window, attr_name)
