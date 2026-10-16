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
def edit_project(name, path, descrip , status , complete_date ):
    
    while True:
        print("1.name")
        print("2.path")
        print("3.description")
        print("4.Status")
        print("5.Complete date")
        choice = input("Enter Your Choice: ") 
        if choice == "1" or choice.lower().startswith("na"):
            name= input("Enter New Name: ")
            return name
        elif choice == "2" or choice.lower().startswith("p"):
            path = input("Paste New Path: ")
            return path
        elif choice == "3" or choice.lower().startswith("d"):
            descrip = input("Enter New Description: ")
            return descrip 
        elif choice == "4" or choice.lower().startswith("s"):
            status = input("Enter Current Status: ")
            return status
        elif choice == "5" or choice.lower().startswith("c"):
            complete_date = input("Enter Complete Date: ")
            return complete_date
        else:
            print("Hey Stupid! Choose Correctly")
        choice = input("Want to Change anything Else...? \n Yes or No: ")
        if choice.lower().startswith("n"):
            break
    







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
    
    print(edit_project(name, path, descrip , status , complete_date))
    # wrapper(edit_project, name, path, descrip , status , creation_time , complete_date )
    
