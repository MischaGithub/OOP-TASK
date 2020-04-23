#importing list cars from car menu
from car_menu import list_cars
#import from car menu to have the user select the car based on id
from car_menu import select_car


import sys

#Creating a menu to give theses 3 options and then performing the option selected
def menu():
    #The 3 options
    option = int(input(
                       "Welcome. \n 1.Check database. \n 2.Select car \n 3.Exit \n"
                       
                       "Please select an option \n"))
#Creating a loop to match the user option and get the output desired
    try:
        option_selected = int(option)
        if option_selected == 1:
            list_cars()
            menu()
        elif option_selected == 2:
            select_car()
        elif option_selected == 3:
            sys.exit("Goodbye")
        else:
            print("You selected an invalid option! Try again\n")
            menu()
    #Creating an exception so that if the input is incorrect to try agan
    except ValueError:
        print("Please select a valid option \n")
        menu()


menu()