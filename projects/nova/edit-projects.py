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