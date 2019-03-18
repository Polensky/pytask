import curses


class Menu:

    def __init__(self, tasklists):
        self._window = curses.newwin(curses.LINES-1,20)
        self._window.box()
        self.tasklists = tasklists
        self.curs_pos = 0

        self.current_tasklist = tasklists[0]
        self.redraw(0)


    def move_up(self):
        if self.curs_pos != 0:
            self.addstr(*self.tasklists[self.curs_pos].addstr())
            self.curs_pos -= 1
            tasklist = self.tasklists[self.curs_pos]
            self.move(*tasklist.get_pos())
            self.addstr(*tasklist.addstr(), curses.A_REVERSE)
            self.current_tasklist = self.tasklists[self.curs_pos]

    def move_down(self):
        if self.curs_pos != len(self.tasklists) - 1:
            self.addstr(*self.tasklists[self.curs_pos].addstr())
            self.curs_pos += 1
            tasklist = self.tasklists[self.curs_pos]
            self.move(*tasklist.get_pos())
            self.addstr(*tasklist.addstr(), curses.A_REVERSE)
            self.current_tasklist = self.tasklists[self.curs_pos]

    def redraw(self, index):
        self._window.clear()
        self._window.box()
        for i, tasklist in enumerate(self.tasklists):
            tasklist.set_pos(i+1, 1)
            if i == index:
                self.addstr(*tasklist.addstr(), curses.A_REVERSE)
                self.current_tasklist = tasklist
            else:
                self.addstr(*tasklist.addstr())

        self.noutrefresh()
        curses.doupdate()


    def __getattr__(self, attr_name):
        return getattr(self._window, attr_name)

