import curses


class Content:

    def __init__(self):
        self._window = curses.newwin(curses.LINES-1, curses.COLS-20, 0, 20)
        self._window.box()

        self._cur_pos = 0

    def display_tasks(self, tasks):
        if tasks is not None:
            self._window.clear()
            self._window.box()
            for i, task in enumerate(tasks):
                task.set_pos(i+1, 1)
                self._window.addstr(*task.addstr())
        else:
            self._window.clear()
            self._window.box()



    def __getattr__(self, attr_name):
        return getattr(self._window, attr_name)
