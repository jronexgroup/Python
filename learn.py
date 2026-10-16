import curses
import time
from curses import wrapper
from datetime import datetime, timezone
import json
from pathlib import Path
import os 


# List Projects
def list_project(directory):
    for number, filename in enumerate(os.listdir(directory), start=1):
        name = os.path.splitext(filename)[0]
        print(f"{number}. {name}")


def load_project(file_name):
    projects_path = fr"/home/rubai/Python/projects/nova/projects/{file_name.lower()}.json"

    #Open File And Make Dict
    with open(projects_path, "r") as f:
        content = f.read()
        projects_dict= json.loads(content)
        return projects_dict

def show_projects(projects_dict):
#Dict To Variable
    global name, path, descrip , status , creation_time , complete_date
    name = projects_dict.get("Project Name")
    path = projects_dict.get("Project Path")
    descrip = projects_dict.get("Project Description")
    status = projects_dict.get("Project Status")
    creation_time = projects_dict.get("Creation time")
    complete_date = projects_dict.get("Complete Date")
    

#Show 
    print (f"Project Name : {name}")
    print(f"Project Path: {path}")
    print(f"Short Description: {descrip}")
    print(f"Status: {status}")
    print(f"Creation Date {creation_time}")
    if complete_date != None:
        print(f"Completed At {complete_date}")


    
    

#Edit function
def edit_project(stdscr, name, path, descrip , status , creation_time , complete_date ):
    stdscr.clear()
    stdscr.refresh()
    stdscr.addstr("### Editing The Details! ###")
    stdscr.addstr(f"\nProject Name : {name}")
    stdscr.addstr(f"\nProject Path: {path}")
    stdscr.addstr(f"\nShort Description: {descrip}")
    stdscr.addstr(f"\nStatus: {status}")
    stdscr.addstr(f"\nCreation Date {creation_time}")
    stdscr.addstr(f"\nCompleted At {complete_date}")
    stdscr.getkey()








#main code 
directory = "/home/rubai/Python/projects/nova/projects"
list_project(directory)

#Get Project Name load and show
file_name = input("Enter The Project Name: ")
projects_dict = load_project(file_name)
show_projects(projects_dict)



# Check Want To Edit And Execute Edit Function If Wanted
want = input("Want To Edit? \n Yes or No: ")
if want.lower().startswith("y"):
    
    # wrapper(edit_project, name, path, descrip , status , creation_time , complete_date )
    exp = 0
    n = 4
    while exp != n:
        print("1.name")
        print("2.path")
        print("3.description")
        print("4.Status")
        print("5.Complete date")
        choice = input("Enter Your Choice: ") 
        if choice == "1" or choice.lower().startswith("n"):
            name = input("Enter New Name: ")
        
