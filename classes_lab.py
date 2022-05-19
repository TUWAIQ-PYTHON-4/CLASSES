# define a Vehicle class . it has the following structure 
# properties

class Vehicle:
    def __init__(self, brand, name, color, capacity, plate_number) :
        self.__brand = brand
        self.__name = name
        self.__color = color
        self.__capacity = capacity
        self.__plate_number = plate_number

# methods

    def drive(self):
        print(f"{self.__name} is driving!")

    def drift(self):
        print(f"{self.__name} is drifting!")

    def carry_cargo(self):
        print(f"{self.__name} is carrying cargo!")


# for each of the properties do a setter & getter (encabsulate the data).
# name 
    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

# brand
    def set_brand(self, brand):
        self.__brand = brand

    def get_brand(self):
        return self.__brand

# color
    def set_color(self, color):
        self.__color = color

    def get_color(self):
        return self.__color

# capacity
    def set_capacity(self, capacity):
        self.__capacity = capacity

    def get_capacity(self):
        return self.__capacity

# plate number
    def set_plate_number(self, plate_number):
        self.__plate_number = plate_number
    def get_plate_number(self):
        return self.__plate_number  

print()

# Create tow other subclasses (inherit from vehicle): -Bus  -Truck
class Bus(Vehicle):

# override  the methods as needed for each subclass of vehicle. 
    def drive(self):
        print(f"{self.get_name()} is driving!")

    def drift(self):
        print(f"{self.get_name()} is drifting!")

    def carry_cargo(self):
        print(f"{self.get_name()} is not carrying cargo!")

# - create at least one object of each class.
shcool_bus=Bus('Bus1','School Bus','Yellow',30,'2366 asdg')

# call all the methods on each object. 
shcool_bus.drive()
shcool_bus.drift()
shcool_bus.carry_cargo()

print()


class Truck(Vehicle):
# override  the methods as needed for each subclass of vehicle. 
    def drive(self):
        print(f"{self.get_name()} is driving!")

    def drift(self):
        print(f"{self.get_name()} is not drifting!")

    def carry_cargo(self):
        print(f"{self.get_name()} is not carrying cargo!")

# - create at least one object of each class.
food_truck=Truck('Truck1','Food Truck','White and Black',3 ,'1883 jklo')

# call all the methods on each object. 
food_truck.drive()
food_truck.drift()
food_truck.carry_cargo()