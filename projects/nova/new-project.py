import curses
import time
from curses import wrapper
from datetime import datetime, timezone
import json
from pathlib import Path
def new_project():
    # Clear screen
   
    project_name = input("Enter Project Name: ")
    project_path = input("Paste Project Path: ")
    project_descrip = input("Give A Short Description: ")
    print("1.Just Started  2:Ongoing  3:Completed")
    project_status= int(input ("What is Project Status: "))
    created_at=  input("Creating Date: ")
    if project_status == 3:

        completed_at = input("Enter Project Completion date: ")
    else :
        completed_at= None

    project_dict={
        "Project Name": project_name,
        "Project Path": project_path,
        "Project Description": project_descrip,
        "Project Status": project_status,
        "Creation time": created_at,
        "Complete Date": completed_at,
    }
    projects_path = fr"/home/rubai/Python/projects/nova/projects/{project_name.lower()}.json"
    f =open(projects_path, "w")
    formated= json.dumps(project_dict, indent=6)
    f.write(formated)
    f.close



    
    
    

