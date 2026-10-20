
import curses
from curses import wrapper
import pyfiglet


MENU_OPTIONS = [
    "Explore Projects",
    "Create New Project",
    "Exit",
]


def draw_menu(stdscr, banner, current):
    stdscr.clear()
    height, width = stdscr.getmaxyx()

    # NOVA banner
    for i, line in enumerate(banner.splitlines()):
        if i + 1 < height:
            stdscr.addnstr(i + 1, 2, line, width - 4)

    title_y = len(banner.splitlines()) + 2
    if title_y < height:
        stdscr.addstr(
            title_y, 2,
            "Welcome to NOVA WORKSPACE v1.0!",
            curses.color_pair(1) | curses.A_BOLD,
        )

    # Dynamic menu
    menu_y = title_y + 2

    for index, option in enumerate(MENU_OPTIONS):
        y = menu_y + index

        if y >= height - 1:
            break

        text = f"  {index + 1}. {option}  "

        if index == current:
            stdscr.addstr(
                y, 2, text[:width - 4],
                curses.color_pair(2) | curses.A_BOLD,
            )
        else:
            stdscr.addstr(y, 2, text[:width - 4])

    stdscr.refresh()


def main(stdscr):
    curses.curs_set(0)
    curses.start_color()
    curses.use_default_colors()

    curses.init_pair(1, curses.COLOR_GREEN, -1)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_GREEN)

    banner = pyfiglet.figlet_format("NOVA")
    current = 0

    while True:
        draw_menu(stdscr, banner, current)
        key = stdscr.getch()

        # Navigation
        if key == curses.KEY_DOWN:
            current = (current + 1) % len(MENU_OPTIONS)

        elif key == curses.KEY_UP:
            current = (current - 1) % len(MENU_OPTIONS)

        # Selection
        elif key in (10, 13, curses.KEY_ENTER):
            if current == 2:
                break

            stdscr.clear()
            stdscr.addstr(
                2, 2,
                f"You selected: {MENU_OPTIONS[current]}",
                curses.A_BOLD,
            )
            stdscr.addstr(4, 2, "Press any key to return...")
            stdscr.refresh()
            stdscr.getch()

        # Escape to exit
        elif key == 27:
            break


if __name__ == "__main__":
    wrapper(main)
