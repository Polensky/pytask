import curses


class UiList:
    def __init__(self, window, elements):
        self._window = window
        self._elements = elements
        self._window.box()

        self.curs_pos = 0
        self.current_element = self._elements[0]
        self.redraw(0)

    def move_up(self):
        if self.curs_pos != 0:
            self.curs_pos -= 1
            self.current_element = self._elements[self.curs_pos]
            self.redraw(self.curs_pos)

    def move_down(self):
        if self.curs_pos != len(self._elements) - 1:
            self.curs_pos += 1
            self.current_element = self._elements[self.curs_pos]
            self.redraw(self.curs_pos)

    def redraw(self, index):
        self._window.clear()
        self._window.box()

        if self._elements:
            for i, element in enumerate(self._elements):
                element.pos = i+1, 1
                if i == index:
                    self.addstr(*element.addstr(), curses.A_REVERSE)
                    self.current_element = element
                else:
                    self.addstr(*element.addstr())

        self.noutrefresh()
        curses.doupdate()

    def __getattr__(self, attr_name):
        return getattr(self._window, attr_name)
