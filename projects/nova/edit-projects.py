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
    global projects_dict
    with open(projects_path, "r") as f:
        content = f.read()
        projects_dict= json.loads(content)
        return projects_dict

def edit_projects(projects_dict , stdscr):
#Dict To Variable
    global name, path, descrip , status , creation_time , complete_date
    name = list(projects_dict.get("Project Name"))
    path = list(projects_dict.get("Project Path"))
    descrip = list(projects_dict.get("Project Description"))
    status = list(projects_dict.get("Project Status"))
    creation_time = projects_dict.get("Creation time")
    complete_date = projects_dict.get("Complete Date")
    
    
    stdscr.clear
    stdscr.addstr(0,0,"###Editing The Project###")
    stdscr.addstr(1,0,"Press Enter To Save.")
    #Get New Name
    while True:
        stdscr.addstr(2,0,"Enter New Name: ")
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
    while True:
            stdscr.addstr(3,0,"Enter New Path: ")
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
    while True:
            stdscr.addstr(4,0,"Enter New path: ")
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
    while True:
            stdscr.addstr(5,0,"Enter New status: ")
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
    #get complete date if not completed yet
    if complete_date == None:
        complete_date= []
        while True:
                stdscr.addstr(6,0,"Enter New Complete Date: ")
                stdscr.clrtoeol()  # Clear the rest of the line
                stdscr.addstr(6,24,"".join(complete_date))
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
            "Creation time": creation_time,
            "Complete Date": complete_date,
        }
    return new_project_dict
        
    
    

    

def save(stdscr, name, project):
    projects_path = fr"/home/rubai/Python/projects/nova/projects/{name.lower()}.json"
    f =open(projects_path, "w")
    formated= json.dumps(new_project_dict, indent=6)
    f.write(formated)
    f.close







def main(stdscr):
    directory = "/home/rubai/Python/projects/nova/projects"
    list_project(directory, stdscr)

#Get Project Name load and show
    
    # Get Project Name
    file_name = []
    num_projects =len(os.listdir(directory))
    while True:
        
        stdscr.addstr(num_projects, 0, "Enter The Project Name: ")
        stdscr.clrtoeol()  # Clear the rest of the line
        stdscr.addstr(num_projects, 24, "".join(file_name))
        stdscr.refresh()

        key = stdscr.getch()

        if key in (10, 13):  # Enter
            break
        elif key in (curses.KEY_BACKSPACE, 127, 8):
            if file_name:
                file_name.pop()
        elif 32 <= key <= 126:  # Printable ASCII characters
            file_name.append(chr(key))
    if len(file_name)>0:
        file_name = "".join(file_name)

        projects_dict = load_project(file_name)
        new_project_dict = edit_projects(projects_dict, stdscr)
        save(stdscr , name, new_project_dict)

if __name__ == "__main__":
    wrapper(main)

