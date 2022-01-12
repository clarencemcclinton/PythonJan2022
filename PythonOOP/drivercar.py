class Car:
    # class attributes
    manufacturer = "GMC"
    number_of_cars = 0
    all_cars = []
    # init method / instance attributes
    def __init__(self, data):
        self.tank_size = data["tank_size"]
        self.gallons_of_gas = 0
        self.color = data["color"]
        self.year = data["year"]
        self.make = data["make"]
        self.model = data["model"]
        # updating class attribute values
        Car.number_of_cars += 1
        Car.all_cars.append(self)

    # class method
    @classmethod # decorator
    def total_gallons_of_gas(cls): # pass in 'cls' so class can be referenced
        total_gallons = 0
        for car in Car.all_cars:
            total_gallons += car.gallons_of_gas
        return total_gallons

    # static method
    @staticmethod # decorator
    def enough_gas(total_gas, gas_needed):
        if total_gas < gas_needed:
            print("Sorry! Not enough fuel")
            return False
        else:
            print("enjoy your trip!")
            return True

    # instance method
    def fill_tank(self): # pass in 'self'so individual instances can be referenced
        self.gallons_of_gas = self.tank_size
        return self

    def drive(self, miles):
        if Car.enough_gas(self.gallons_of_gas, miles):
            self.gallons_of_gas -= miles
        else:
            print("Looks like a stay at home day!")
        return self

    def get_car_info(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}, and Tank Size: {self.tank_size}")
        return self

# class Driver:
#     def __init__(self, data):
#         self.name = data['name']
#         self.age = data['age']
#         # self.car = data['car'] # for one car
#         # for storing multiple cars per 1 user
#         self.cars = data["cars"]
        
#     # show car info for only 1 car
#     # def car_info(self):
#     #     self.car.get_car_info()

#     # show car info with multiple cars
#     def show_all_cars(self):
#         for car in self.cars:
#             car.get_car_info()

#     def add_car(self, new_car):
#         self.cars.append(new_car)

#     def drive(self, miles):
#         print(f"Driver {self.name}, is going for a ride!")
#         self.car.drive(miles)
    
#     def get_gas(self):
#         self.car.fill_tank()

#     def check_fuel(self):
#         print(f"The current fuel level is: {self.car.gallons_of_gas}")

# # data objects with instances of Car class
# subaru_data = {
#     "tank_size": 18,
#     "color": "Blue",
#     "make": "Subaru",
#     "model": "Crosstrek",
#     "year": 2019,
# }
# subaru = Car(subaru_data)
# civic_data = {
#     "tank_size": 12,
#     "color": "Silver",
#     "make": "Honda",
#     "model": "Civic",
#     "year": 2006,
# }
# civic = Car(civic_data)
# tacoma_data = {
#     "tank_size": 25,
#     "color": "White",
#     "make": "Toyota",
#     "model": "Tacoma",
#     "year": 1993,
# }
# tacoma = Car(tacoma_data)

# driver1_data = {
#     "name" : "Sbeve",
#     "age" : 27,
#     "cars" : []
# }
# driver1 = Driver(driver1_data)

# print(driver1.cars)
# driver1.show_all_cars()
# print("-----------------------------------")
# driver1.add_car(tacoma)
# driver1.show_all_cars()
# print("-----------------------------------")
# tacoma.tank_size = 15
# driver2_data = {
#     "name" : "NotSbeve",
#     "age" : 27,
#     "cars" : [civic, subaru, tacoma]
# }
# driver2 = Driver(driver2_data)
# driver2.show_all_cars()

# # driver1 = {
# #     "name" : "Sbeve",
# #     "age" : 27,
# #     "car" : {
# #         "tank_size": 18,
# #         "color": "Blue",
# #         "make": "Subaru",
# #         "model": "Crosstrek",
# #         "year": 2019,
# #     }
# # }
# # print(driver1)
# # print(driver1.car.color)
# # # driver1["car"]["color"]
# # print(driver1.car.tank_size)
# # print(driver1.car.model)
# # print(driver1.name)

# # driver1.car_info()
# # driver1.check_fuel()
# # driver1.get_gas()
# # driver1.check_fuel()
# # driver1.drive(3)

# # driver1.car.fill_tank().get_car_info()


