import os
directory = "/home/rubai/Python/projects/nova/projects"
def list_project(directory):
    for number, filename in enumerate(os.listdir(directory), start=1):
        name = os.path.splitext(filename)[0]
        print(f"{number}. {name}")
list_project(directory)
