import os #built-in function

students = {'John': 90, 'Paul': 84, 'Ben': 70, 'Tony': 35, 'Kate': 100}

def print_main_window():
    os.system('clear')
    print("\t********************************************")
    print("\t***  Manipulating a Dictionary! There we go     **")
    print("\t********************************************")
    print("\n\n\n") #3 line breaks
    print("Choose an option as follows: ")
    print("[1] List Grade by Name")
    print("[2] Add a new student and grade")
    print("[3] Update grade")
    print("[4] list all Grades")
    print("[5] EXIT")

def list_grade_by_name(name):
    print(students[name])

def add_student(name,grade):
    students[name]=grade

def update_Grade(name,grade):
    students.update({name:grade})

def list_all_grades():
    for key,value in students.items():
        print(value)

while (True):
    print_main_window()
    option = int(input("Your option: "))
    os.system('clear')
    if (option == 1):
        name = input("What is the name: ")
        list_grade_by_name(name)

    elif (option == 2):
        name = input("What is the name: ")
        grade = input("what is the grade: ")
        add_student(name, grade)

    elif (option == 3):
        name = input("Enter the student name to update the grade: ")
        grade = input("what is the new grade: ")
        students.update({name: grade})

    elif (option == 4):
        list_all_grades()

    elif (option == 5):
        break
    else:
        print ("Invalid option. ")

    input("\n\nClick Return key to return.")









