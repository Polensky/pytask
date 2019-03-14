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
        self.menu = Menu(self.tasklists)
        self.content = Content()

        for i, tasklist in enumerate(self.tasklists):
            tasklist.set_pos(i+1, 1)
            if i == 0:
                self.menu.addstr(*tasklist.addstr(), curses.A_REVERSE)
                self.current_tasklist = tasklist
            else:
                self.menu.addstr(*tasklist.addstr())

        self.is_cursor_on_menu = True

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
            elif c == ord('\t'):
                self.switch_window()

            stdscr.noutrefresh()
            self.menu.noutrefresh()
            self.content.noutrefresh()
            curses.doupdate()

        curses.nocbreak()
        curses.echo()
        curses.curs_set(1)
        curses.endwin()

    def move_up(self):
        if self.is_cursor_on_menu:
            self.menu.move_up()
            self.content.display_tasks(self.current_tasklist.tasks)
        else:
            if self.content.curs_pos != 0:
                task = self.current_tasklist.tasks[self.content.curs_pos]
                self.content.addstr(*task.addstr())
                self.content.curs_pos -= 1
                task = self.current_tasklist.tasks[self.content.curs_pos]
                self.content.addstr(*task.addstr(), curses.A_REVERSE)

    def move_down(self):
        if self.is_cursor_on_menu:
            self.menu.move_down()
            self.content.display_tasks(self.current_tasklist.tasks)
        else:
            if self.content.curs_pos != len(self.current_tasklist.tasks) - 1:
                task = self.current_tasklist.tasks[self.content.curs_pos]
                # lattribut y existe pas ici apparament
                self.content.addstr(*task.addstr())
                self.content.curs_pos += 1
                task = self.current_tasklist.tasks[self.content.curs_pos]
                self.content.addstr(*task.addstr(), curses.A_REVERSE)

    def switch_window(self):
        self.is_cursor_on_menu = not self.is_cursor_on_menu
        if self.is_cursor_on_menu:
            self.content.addstr(*self.tasklists[self.content.curs_pos].addstr())
        else:
            task = self.current_tasklist.tasks[0]
            self.content.addstr(*task.addstr(), curses.A_REVERSE)



    def run(self):
        curses.wrapper(self.application)


PyTaskApp().run()
