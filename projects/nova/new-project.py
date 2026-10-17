import sys
import curses
import time
from curses import wrapper
from datetime import datetime, timezone
import json
from pathlib import Path
def new_project(stdscr, name):
    stdscr.clear
    stdscr.addstr(0,0,"###New Project###")
    stdscr.addstr(1,0,"Press Enter To Save.")
    #Get New Name
    l = list(name)
    name = l
    while True:
        stdscr.addstr(2,0,"Enter The Name: ")
        stdscr.clrtoeol()  # Clear the rest of the line
        stdscr.addstr(2,15,"".join(name))
        stdscr.refresh()
        key = stdscr.getch()
        if key in (10, 13):  # Enter
            break
        elif key in (curses.KEY_BACKSPACE, 127, 8):
            if name:
                name.pop()
        elif 32 <= key <= 126:
                name.append(chr(key))
    if len(name)>0:
        name = "".join(name)
    
        #get new path
    path = []
    while True:
        stdscr.addstr(3,0,"Enter The Path: ")
        stdscr.clrtoeol()  # Clear the rest of the line
        stdscr.addstr(3,15,"".join(path))
        stdscr.refresh()
        key = stdscr.getch()
        if key in (10, 13):  # Enter
            break
        elif key in (curses.KEY_BACKSPACE, 127, 8):
            if path:
                path.pop()
        elif 32 <= key <= 126:
            path.append(chr(key))
    if len(path)>0:
        path = "".join(path)
        
        # Get New Descrip
    descrip = []
    while True:
        stdscr.addstr(4,0,"Enter The Description: ")
        stdscr.clrtoeol()  # Clear the rest of the line
        stdscr.addstr(4,15,"".join(descrip))
        stdscr.refresh()
        key = stdscr.getch()
        if key in (10, 13):  # Enter
            break
        elif key in (curses.KEY_BACKSPACE, 127, 8):
            if descrip:
                descrip.pop()
        elif 32 <= key <= 126:
            descrip.append(chr(key))
    if len(descrip)>0:
           descrip = "".join(descrip)
        #chage project status
    status = []
    while True:
            stdscr.addstr(5,0,"Enter The status: ")
            stdscr.clrtoeol()  # Clear the rest of the line
            stdscr.addstr(5,17,"".join(status))
            stdscr.refresh()
            key = stdscr.getch()
            if key in (10, 13):  # Enter
                break
            elif key in (curses.KEY_BACKSPACE, 127, 8):
                if status:
                    status.pop()
            elif 32 <= key <= 126:
                status.append(chr(key))
    if len(status)>0:
            status = "".join(status)
    creation_date=[]
    while True:
        stdscr.addstr(6,0,"Enter The Creation Date: ")
        stdscr.clrtoeol()  # Clear the rest of the line
        stdscr.addstr(6,24,"".join(creation_date))
        stdscr.refresh()
        key = stdscr.getch()
        if key in (10, 13):  # Enter
            break
        elif key in (curses.KEY_BACKSPACE, 127, 8):
            if creation_date:
                creation_date.pop()
        elif 32 <= key <= 126:
            creation_date.append(chr(key))
    if len(creation_date)>0:
        creation_date = "".join(creation_date)
        #get complete date if not completed yet
    complete_date=[]
    while True:
        stdscr.addstr(7,0,"Enter The Complete Date: ")
        stdscr.clrtoeol()  # Clear the rest of the line
        stdscr.addstr(7,24,"".join(complete_date))
        stdscr.refresh()
        key = stdscr.getch()
        if key in (10, 13):  # Enter
            break
        elif key in (curses.KEY_BACKSPACE, 127, 8):
            if complete_date:
                complete_date.pop()
        elif 32 <= key <= 126:
            complete_date.append(chr(key))
    if len(complete_date)>0:
        complete_date = "".join(complete_date)
    global new_project_dict
    new_project_dict={
                "Project Name": name,
                "Project Path": path,
                "Project Description": descrip,
                "Project Status": status,
                "Creation time": creation_date,
                "Complete Date": complete_date,
            }
    return new_project_dict
            
        
def save(name, project):
    projects_path = fr"/home/rubai/Python/projects/nova/projects/{name.lower()}.json"
    f =open(projects_path, "w")
    formated= json.dumps(new_project_dict, indent=6)
    f.write(formated)
    f.close


def main(stdscr):


    if len(sys.argv) > 1:
        name = sys.argv[1]
    else:
        name = input("Enter project name: ")
    project = new_project(stdscr, name)
    save(project.get("Project Name"), project)
if __name__ == "__main__":
    wrapper(main)


    
    
    

