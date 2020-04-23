from car_data import cars
from main import *


#Display the values in the cars list so show user the cars in the database
def list_cars():
    for car in cars:
        print(car['id'], car['make'], car["year_model"])

#Creating a function to check the id and make the results accordingly
def user_car_id(car_id):
    for car in cars:
        if car['id'] == car_id: # You should return a car instead of printing.
            print(car["id"], car["year_model"], car["distance_driven"], car["base_price"],
              car["tank_size"], car["kilometers_per_tank"], car["make"])


def select_car():
#match the user input with the cars id and then display the properties of the id selects
    car_id = input("Please select a car with its ID \n")

    try:
        selection = int(car_id)
        if selection == 1:
            return user_car_id(selection)
        elif selection == 2:
            return user_car_id(selection)
        elif selection == 3:
            return user_car_id(selection)
        elif selection == 4:
            return user_car_id(selection)
        elif selection == 5:
            return user_car_id(selection)
        elif selection == 6:
            return user_car_id(selection)
        elif selection == 7:
            return user_car_id(selection)
        elif selection == 8:
            return user_car_id(selection)
        elif selection == 9:
            return user_car_id(selection)
        else:
            print("Please select car with id. PLease try again \n")

    except ValueError:
        print("Thats not a valid input")
        select_car()

#Just printing the fuel usage and resell price for each car
        fuel_usage = Car.calculate_fuel_usage(caddy)
        print(fuel_usage)


select_car()

