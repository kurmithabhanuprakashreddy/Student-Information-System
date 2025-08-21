#StudentInformationSystem.py
from StudentMenu import menu
from StudentAdd import addstudent
from StudentSelect import viewallstudents,viewsinglestudent
from StudentSearch import  searchstudent
from StudentUpdate import updatestudent
from StudentDelete import deletestudent
while(True):
    try:
        menu()
        ch=int(input("Enter UR Choice:"))
        match(ch):
            case 1:
                addstudent()
            case 2:
                deletestudent()
            case 3:
                updatestudent()
            case 4:
                searchstudent()
            case 5:
                viewsinglestudent()
            case 6:
                viewallstudents()
            case 7:
                print("Thx Program Using this Project")
                break
            case _:
                print("Ur Selection of Operation is Wrong--try again")
    except ValueError:
        print("\tDon't Enter NON-Ints for Choice--try again")