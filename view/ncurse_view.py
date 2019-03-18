from view import Content, Menu
import curses


class CurseView:

    def __init__(self, tasklists):
        curses.wrapper(self._init_curse)

        self.menu = Menu(tasklists)
        self.content = Content(tasklists[0].tasks)
        self.is_cursor_on_menu = True

        self.stdscr.noutrefresh()
        curses.doupdate()

    def _init_curse(self, stdscr):
        self.stdscr = stdscr
        self.stdscr.nodelay(True)
        self.stdscr.clear()
        curses.cbreak()
        curses.noecho()
        curses.curs_set(0)
        curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
        if curses.has_colors:
            curses.start_color()

    def start_loop():
        stdscr.noutrefresh()
        curses.doupdate()


    def quit(self):
        curses.nocbreak()
        curses.echo()
        curses.curs_set(1)
        curses.endwin()
