import curses
from curses import wrapper
import os


def select_project(stdscr):
    curses.curs_set(0)

    projects_dir = "/home/rubai/Python/projects/nova/projects"

    projects = []

    for name in os.listdir(projects_dir):
        name = os.path.splitext(name)[0]

    
        projects.append(name)

    current = 0

    while True:
        stdscr.clear()

        stdscr.addstr(0, 0, "NOVA - Select a Project")
        stdscr.addstr(1, 0, "Use UP/DOWN arrows | ENTER: Select | ESC: Exit")

        for index, project in enumerate(projects):
            y = index + 3

            if index == current:
                stdscr.attron(curses.A_REVERSE)
                stdscr.addstr(y, 2, f"> {project}")
                stdscr.attroff(curses.A_REVERSE)
            else:
                stdscr.addstr(y, 2, f"  {project}")

        stdscr.refresh()

        key = stdscr.getch()

        if key == curses.KEY_DOWN:
            current = (current + 1) % len(projects)

        elif key == curses.KEY_UP:
            current = (current - 1) % len(projects)

        elif key in (curses.KEY_ENTER, 10, 13):
            return projects[current]

        elif key == 27:  # ESC
            return None


def main(stdscr):
    selected = select_project(stdscr)

    if selected:
        stdscr.clear()
        stdscr.addstr(0, 0, f"Selected project: {selected}")
        stdscr.addstr(2, 0, "Press any key to exit.")
        stdscr.refresh()
        stdscr.getch()


wrapper(main)