import os #built-in function

def print_main_window():
    os.system('clear')
    print("\t********************************************")
    print("\t***  Manipulating a List! There we go     **")
    print("\t********************************************")
    print("\n\n\n") #3 line breaks
    print("Choose an option as follows: ")
    print("[1] Add a number to the list")
    print("[2] List the numbers")
    print("[3] Clear the list")
    print("[4] EXIT")

def list_the_numbers (list1):
    print("This list contains ", len(list1), " elements, as follows:")
    for element in list1:
        print (element)

list_numbers = [] #defining an empty list

while (True):
    print_main_window()
    option = int(input("Your option: "))
    os.system('clear')
    if (option == 1):
        number = int(input("Type the number you want to add: "))
        list_numbers.append(number)
        print(number, " added to your list")
    elif (option == 2):
        list_the_numbers(list_numbers)
    elif (option == 3):
        list_numbers.clear()
        print("The list is now empty!")
    elif (option == 4):
        print("Thanks for using our application")
        break
    else:
        print ("Invalid option. ")

    input("\n\nClick Return key to return.")











