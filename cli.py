import curses
from menu import Menu
from content import Content
from task_api import TaskAPI


class PyTaskApp:

    def __init__(self):
        self.tsk_api = TaskAPI()
        self.tsk_api.connect()
        self.tasklists = self.tsk_api.get_taskslists()

    def application(self, stdscr):
        # settings
        stdscr.nodelay(True)
        stdscr.clear()
        curses.cbreak()
        curses.noecho()
        curses.curs_set(0)
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
        if curses.has_colors:
            curses.start_color()

        #initialise
        self.menu = Menu()
        self.content = Content()

        for i, tasklist in enumerate(self.tasklists):
            tasklist.set_pos(i+1, 1)
            if i == 0:
                self.menu.addstr(*tasklist.addstr(), curses.A_REVERSE)
            else:
                self.menu.addstr(*tasklist.addstr())

        self.curs_pos = 0

        stdscr.noutrefresh()
        self.menu.noutrefresh()
        self.content.noutrefresh()
        curses.doupdate()

        #application loop
        while True:
            c = stdscr.getch()
            if c == ord('q'):
                break
            elif c == ord('k'):
                self.move_up()
            elif c == ord('j'):
                self.move_down()

            stdscr.noutrefresh()
            self.menu.noutrefresh()
            self.content.noutrefresh()
            curses.doupdate()

        curses.nocbreak()
        curses.echo()
        curses.curs_set(1)
        curses.endwin()


    def move_up(self):
        if self.curs_pos != 0:
            self.menu.addstr(*self.tasklists[self.curs_pos].addstr())
            self.curs_pos -= 1
            tasklist = self.tasklists[self.curs_pos]
            self.menu.move(*tasklist.get_pos())
            self.menu.addstr(*tasklist.addstr(), curses.A_REVERSE)
            self.content.display_tasks(tasklist.tasks)

    def move_down(self):
        if self.curs_pos != len(self.tasklists) - 1:
            self.menu.addstr(*self.tasklists[self.curs_pos].addstr())
            self.curs_pos += 1
            tasklist = self.tasklists[self.curs_pos]
            self.menu.move(*tasklist.get_pos())
            self.menu.addstr(*tasklist.addstr(), curses.A_REVERSE)
            self.content.display_tasks(tasklist.tasks)

    def run(self):
        curses.wrapper(self.application)


PyTaskApp().run()
