import curses
from view import Menu, Content
from view import CurseView
from model import TaskList, TaskAPI


class PyTaskApp:

    def __init__(self):
        self.tsk_api = TaskAPI()
        self.tsk_api.connect()
        self.tasklists = self.tsk_api.get_taskslists()
        self.view = CurseView(self.tasklists)

    def application(self):
        while True:
            c = self.view.stdscr.getch()
            if c == ord('q'):
                self.view.quit()
                break
            elif c == ord('k'):
                self.move_up()
            elif c == ord('j'):
                self.move_down()
            elif c == ord('\t'):
                self.switch_window()

    def move_up(self):
        if self.is_cursor_on_menu:
            self.menu.move_up()
            self.content.display_tasks(self.menu.current_tasklist.tasks)
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
            self.content.display_tasks(self.menu.current_tasklist.tasks)
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
            self.content.addstr(*self.tasklists[self.menu.curs_pos].addstr())
        else:
            task = self.current_tasklist.tasks[0]
            self.content.addstr(*task.addstr(), curses.A_REVERSE)



PyTaskApp().application()
