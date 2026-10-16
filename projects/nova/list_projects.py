import os
import curses
from curses import wrapper

def list_project(stdscr):
    directory = "/home/rubai/Python/projects/nova/projects"
    stdscr.clear()

    for number, filename in enumerate(os.listdir(directory), start=1):
        name = os.path.splitext(filename)[0]
        stdscr.addstr(number - 1, 0, f"{number}. {name}")
    stdscr.refresh()

    stdscr.getkey()
if __name__ == "__main__":
    wrapper(list_project)
