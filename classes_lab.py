# define the class 
class Vehicle:
    def __init__(self, brand,  name, color, capacity, plate_number):
        # Properties (private)
        self.__brand = brand
        self.__name = name 
        self.__color = color
        self.__capacity = capacity
        self.__plate_number = plate_number
    # drive function
    def drive(self):
        print("the {} is driving!".format(self.__name))
    # drift function
    def drift(self):
        print("the {} is drifting !!".format(self.__name))
    # carry cargo function
    def carry_cargo(self):
        print("the {} is carrying cargo !!".format(self.__name))

    # setter functions
    def set_brand(self, n):
        self.__brand = n

    def set_name(self, n):
        self.__name = n

    def set_color(self, n):
        self.__color = n

    def set_capacity(self, n):
        self.__capacity = n
    def set_plate_number(self, n):
        self.__plate_number = n

    # getter functions
    def get_brand(self):
        return self.__brand

    def get_name(self):
        return self.__name

    def get_color(self):
        return self.__color

    def get_capacity(self):
        return self.__capacity

    def get_plate_number(self):
        return self.__plate_number

# two other subclasses (inheritance: inherit from vehicle)
class Bus(Vehicle):
    def __init__(self, brand, name, color, capacity, plate_number):
        super().__init__(brand, name, color, capacity, plate_number)

class Truck(Vehicle):
    def __init__(self, brand, name, color, capacity, plate_number):
        super().__init__(brand, name, color, capacity, plate_number)

# override the methods as needed for each subclass of vehicle.

# create at least one object of each class.
obj_vehicle = Vehicle("Mazda","CX-9","Black","5","5607 RXZ")
obj_bus = Bus("IC Bus","School Bus","Yellow","36","4398 DRV")
obj_truck = Truck("Ford", "F-150","Blue","3","2871 PWR")

# call all the methods on each object.

# object 1 with all methods.
obj_vehicle.drive()
obj_vehicle.drift()
obj_vehicle.carry_cargo()

obj_vehicle.set_brand("BMW")
obj_vehicle.set_name("The X1")
obj_vehicle.set_color("gray")
obj_vehicle.set_capacity("5")
obj_vehicle.set_plate_number("1132 ZRC")

print(obj_vehicle.get_brand())
print(obj_vehicle.get_name())
print(obj_vehicle.get_color())
print(obj_vehicle.get_capacity())
print(obj_vehicle.get_plate_number())

print(" ")
# object 2 with all methods.
obj_bus.drive()
obj_bus.drift()
obj_bus.carry_cargo()

obj_bus.set_brand("Mercedes Benz")
obj_bus.set_name("Citaro")
obj_bus.set_color("white")
obj_bus.set_capacity("101")
obj_bus.set_plate_number("1006 ENQ")

print(obj_bus.get_brand())
print(obj_bus.get_name())
print(obj_bus.get_color())
print(obj_bus.get_capacity())
print(obj_bus.get_plate_number())

print(" ")
# object 3 with all methods.

obj_truck.drive()
obj_truck.drift()
obj_truck.carry_cargo()

obj_truck.set_brand("GMC")
obj_truck.set_name("Sierra")
obj_truck.set_color("Red")
obj_truck.set_capacity("5")
obj_truck.set_plate_number("6619 TRK")

print(obj_truck.get_brand())
print(obj_truck.get_name())
print(obj_truck.get_color())
print(obj_truck.get_capacity())
print(obj_truck.get_plate_number())