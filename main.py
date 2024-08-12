import curses
import os
import subprocess

# Paths to the individual algorithm scripts
scripts = {
    "1": "ant_colony.py",
    "2": "bee_colony.py",
    "3": "bat_algorithm.py",
    "4": "grey_wolf.py",
    "5": "firefly_algorithm.py"
}

def run_algorithm(script):
    """Executes the selected algorithm script."""
    if os.path.exists(script):
        subprocess.run(["python3", script])
    else:
        print(f"Script {script} not found.")

def main_menu(stdscr):
    curses.curs_set(0)  # Hide cursor
    stdscr.clear()
    stdscr.refresh()

    k = 0
    cursor_x = 0
    cursor_y = 0

    menu_items = [
        "1 - Run Ant Colony Algorithm",
        "2 - Run Bee Colony Algorithm",
        "3 - Run Bat Algorithm",
        "4 - Run Grey Wolf Algorithm",
        "5 - Run Firefly Algorithm",
        "q - Quit"
    ]

    while k != ord('q'):
        stdscr.clear()
        stdscr.addstr(0, 0, "Select an algorithm to run:")
        for idx, item in enumerate(menu_items):
            x = cursor_x
            y = cursor_y + idx + 1
            stdscr.addstr(y, x, item)

        # Refresh the screen
        stdscr.refresh()

        # Wait for next input
        k = stdscr.getch()

        if chr(k) in scripts:
            run_algorithm(scripts[chr(k)])

curses.wrapper(main_menu)
