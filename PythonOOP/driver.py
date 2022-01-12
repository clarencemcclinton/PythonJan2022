from drivercar import Car

class Driver:
    def __init__(self, data):
        self.name = data['name']
        self.age = data['age']
        # self.car = data['car'] # for one car
        # for storing multiple cars per 1 user
        self.cars = data["cars"]
        
    # show car info for only 1 car
    # def car_info(self):
    #     self.car.get_car_info()

    # show car info with multiple cars
    def show_all_cars(self):
        for car in self.cars:
            car.get_car_info()

    def add_car(self, new_car):
        self.cars.append(new_car)

    def drive(self, miles):
        print(f"Driver {self.name}, is going for a ride!")
        self.car.drive(miles)
    
    def get_gas(self):
        self.car.fill_tank()

    def check_fuel(self):
        print(f"The current fuel level is: {self.car.gallons_of_gas}")

# data objects with instances of Car class
subaru_data = {
    "tank_size": 18,
    "color": "Blue",
    "make": "Subaru",
    "model": "Crosstrek",
    "year": 2019,
}
subaru = Car(subaru_data)
civic_data = {
    "tank_size": 12,
    "color": "Silver",
    "make": "Honda",
    "model": "Civic",
    "year": 2006,
}
civic = Car(civic_data)
tacoma_data = {
    "tank_size": 25,
    "color": "White",
    "make": "Toyota",
    "model": "Tacoma",
    "year": 1993,
}
tacoma = Car(tacoma_data)

driver1_data = {
    "name" : "Sbeve",
    "age" : 27,
    "cars" : []
}
driver1 = Driver(driver1_data)

print(driver1.cars)
driver1.show_all_cars()
print("-----------------------------------")
driver1.add_car(tacoma)
driver1.show_all_cars()
print("-----------------------------------")
tacoma.tank_size = 15
driver2_data = {
    "name" : "NotSbeve",
    "age" : 27,
    "cars" : [civic, subaru, tacoma]
}
driver2 = Driver(driver2_data)
driver2.show_all_cars()

# driver1 = {
#     "name" : "Sbeve",
#     "age" : 27,
#     "car" : {
#         "tank_size": 18,
#         "color": "Blue",
#         "make": "Subaru",
#         "model": "Crosstrek",
#         "year": 2019,
#     }
# }
# print(driver1)
# print(driver1.car.color)
# # driver1["car"]["color"]
# print(driver1.car.tank_size)
# print(driver1.car.model)
# print(driver1.name)

# driver1.car_info()
# driver1.check_fuel()
# driver1.get_gas()
# driver1.check_fuel()
# driver1.drive(3)

# driver1.car.fill_tank().get_car_info()