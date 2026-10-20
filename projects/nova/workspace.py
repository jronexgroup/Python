import curses
from curses import wrapper
import json
import os 
import pyfiglet
import edit_projects
import show_projects
import new_project
import list_projects


def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_WHITE)
    curses.curs_set(0)

    banner = pyfiglet.figlet_format("NOVA")
    current = 0
    while True:
        for i, line in enumerate(banner.splitlines()):
            stdscr.addstr(i + 1, 2, line,)

        stdscr.addstr(7, 2, "Welcome to NOVA WORKSPACE v1.0!", curses.A_BOLD | curses.color_pair(1))
        if current == 1:
            stdscr.addstr(9,1, "1.Explore Projects",curses.A_BOLD | curses.color_pair(2))
        else:
            stdscr.addstr(9,1, "1.Explore Projects")
        if current == 2:
            stdscr.addstr(10,1, "2.Create New Project", curses.A_BOLD | curses.color_pair(2))
        else:
            stdscr.addstr(10,1, "2.Create New Project")
        stdscr.refresh()
        key = stdscr.getch()

        if key == curses.KEY_DOWN and current !=2:
            current += 1
        elif key == curses.KEY_UP and current !=0:
            current -= 1
        elif key in (10, 13, curses.KEY_ENTER):
            break
        elif key == 27:
            break



if __name__ == "__main__":
    wrapper(main)