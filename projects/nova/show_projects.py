import sys
import curses
import time
from curses import wrapper
from datetime import datetime, timezone
import json
from pathlib import Path
import os 


# List Projects

def list_project(directory, stdscr):
    stdscr.clear()

    for number, filename in enumerate(os.listdir(directory), start=1):
        name = os.path.splitext(filename)[0]
        stdscr.addstr(number - 1, 0, f"{number}. {name}")

    stdscr.refresh()
    stdscr.getkey()



def load_project(file_name):
    projects_path = fr"/home/rubai/Python/projects/nova/projects/{file_name.lower()}.json"

    #Open File And Make Dict
    with open(projects_path, "r") as f:
        content = f.read()
        projects_dict= json.loads(content)
        return projects_dict

def show_projects(projects_dict , stdscr):
#Dict To Variable
    global name, path, descrip , status , creation_time , complete_date
    name = projects_dict.get("Project Name")
    path = projects_dict.get("Project Path")
    descrip = projects_dict.get("Project Description")
    status = projects_dict.get("Project Status")
    creation_time = projects_dict.get("Creation time")
    complete_date = projects_dict.get("Complete Date")
    
    
#Show 
    stdscr.clear()
    stdscr.refresh()
    stdscr.addstr(f"Project Name : {name}")
    stdscr.addstr(f"\nProject Path: {path}")
    stdscr.addstr(f"\nShort Description: {descrip}")
    stdscr.addstr(f"\nStatus: {status}")
    stdscr.addstr(f"\nCreation Date {creation_time}")
    if complete_date != None:
        stdscr.addstr(f"\nCompleted At {complete_date}")
    stdscr.getkey()


    

def show_text(stdscr, current):
    stdscr.addstr(0, 24, "".join(current))
    stdscr.refresh()







#main code 
def main(stdscr, name=0):

    if name != 0:
        file_name = name
    


    else:
        stdscr.keypad(True)
        directory = "/home/rubai/Python/projects/nova/projects"
        list_project(directory, stdscr)

#Get Project Name load and show
    
    # Get Project Name
        file_name = []
        num_projects = len(os.listdir(directory))
    

        while True:
            stdscr.addstr(num_projects, 0, "Enter The Project Name: ")
            stdscr.clrtoeol()  # Clear the rest of the line
            stdscr.addstr(num_projects, 24, "".join(file_name))
            stdscr.refresh()

            key = stdscr.getch()

            if key in (10, 13, curses.KEY_ENTER):
                stdscr.clear()
                break

            elif key in (curses.KEY_BACKSPACE, 127, 8):
                if file_name:
                    file_name.pop()

            elif 32 <= key <= 126:
                file_name.append(chr(key))
        if len(file_name)>0:
            file_name = "".join(file_name)

    projects_dict = load_project(file_name)
    show_projects(projects_dict, stdscr)
if __name__ == "__main__":
    wrapper(main)

    
