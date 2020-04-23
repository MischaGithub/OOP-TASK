#Creating a car program to retrieve information

from datetime import datetime

class Car:

    resell = 0
    fuel_usage = 0

    def __init__(self, car_id, year_model, distance_driven, base_price, tank_size,
                 kilometers_per_tank, make,):
        self.car_id = car_id
        self.year_model = year_model
        self.distance_driven = distance_driven
        self.base_price = base_price
        self.tank_size = tank_size
        self.kilometers_per_tank = kilometers_per_tank
        self.make = make

    def __str__(self):
        return "this is a {car_id} {year} {make}, with a tank size of {tank}.".format(car_id= self.car_id ,year=self.year_model, make=self.make,
                                                                             tank=self.tank_size)


    def calculate_fuel_usage(self):
        car_fuel = self.kilometers_per_tank / self.tank_size

        return 'Fuel usage: ' + str(int(car_fuel)), 'km/l'

    def car_value(self):

        current_date = int(datetime.now().strftime("%Y"))

        age = current_date - self.year_model

        if age < 20:
            return int(self.base_price * (0.9 * age))
        elif age >= 20:
            return int(self.base_price * (0.9 * age) + 20000)



class Volkswagen(Car):

    def car_details(self):

        Car.__str__(self)
        Car.calculate_fuel_usage(self)
        Car.car_value(self)


caddy = Volkswagen(1, 1995, 240000, 200000, 30, 100, 'Volkswagen')
touareg = Volkswagen(2, 2010,  10000, 300000,  20, 120, 'Volkswagen')
t_roc = Volkswagen(3, 2017, 300000, 900000, 15, 80, 'Volkswagen')




class Mercedes(Car):

    def car_de(self):
        Car.__str__(self)
        Car.calculate_fuel_usage(self)
        Car.car_value(self)


mb_100 = Mercedes(4, 1982, 560000, 50000, 25, 150, 'Mercedes')
sprinter = Mercedes(5, 2012, 30000, 500000, 20, 90, 'Mercedes')
amg = Mercedes(6, 2019, 10000, 1000000, 15, 15, 'Mercedes')

class Toyota(Car):

    def car_details(self):
        Car.__str__(self)
        Car.calculate_fuel_usage(self)
        Car.car_value(self)


scion_xb = Toyota(7, 2000, 600000, 250000, 25, 200, 'Toyota')
aurion = Toyota(8, 2015, 30000, 350000, 20, 100, 'Toyota')
corolla = Toyota(9, 2018, 2000, 800000, 25, 200, 'Toyota')




#Just printing out the details for the fuel usage nd resell value for Volkswagen
print(caddy.__str__())
print(caddy.calculate_fuel_usage())
print(caddy.car_value())
print(touareg.__str__())
print(touareg.calculate_fuel_usage())
print(touareg.car_value())
print(t_roc.__str__())
print(t_roc.calculate_fuel_usage())
print(t_roc.car_value())

#Just printing out the details for the fuel usage nd resell value for Mercedes
print(mb_100.__str__())
print(mb_100.calculate_fuel_usage())
print(mb_100.car_value())
print(sprinter.__str__())
print(sprinter.calculate_fuel_usage())
print(sprinter.car_value())
print(amg.__str__())
print(amg.calculate_fuel_usage())
print(amg.car_value())

#Just printing out the details for the fuel usage nd resell value for Toyota
print(scion_xb.__str__())
print(scion_xb.calculate_fuel_usage())
print(scion_xb.car_value())
print(aurion.__str__())
print(aurion.calculate_fuel_usage())
print(aurion.car_value())
print(corolla.__str__())
print(corolla.calculate_fuel_usage())
print(corolla.car_value())





