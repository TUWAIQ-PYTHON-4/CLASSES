
# define a Vehicle class . it has the following structure :
from turtle import color


class Vehicle:

    # properties brand, name, color, capacity, plate_number
    def __init__(self, brand: str, name: str, color: str, capacity: str, plate_number: str):
        self.__brand= brand
        self.__name = name
        self.__color = color
        self.__capacity = capacity
        self.__plate_number= plate_number

    # methods
    def VechileInfo(self,): ## for print the detalis about the vechile
        print("Brand:", self.__brand, "|", "Name:", self.__name,"|", "Color:", self.__color,"|", "Capacity:", self.__capacity,"|", "Plate N0:", self.__plate_number)

    def drive(self,):
        print(f"{self.__name} is driving!")

    def drift(self):
        print(f"{self.__name} is drifting !!")  

    def carry_cargo(self):
        print(f"{self.__name} is carrying cargo !!")  

    # for each of the properties do a setter & getter (encabsulate the data).
    def set_name(self, name):
        self.__name = name

    def set_brand(self, brand):
        self.__brand = brand

    def set_color(self, color):
        self.__color = color

    def set_capacity(self, capacity):
        self.__capacity = capacity

    def set_plate_number(self, plate_number):
        self.__plate_number = plate_number

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

# creating inheritance class from Vechile
class bus(Vehicle):

    def drift(self):
        print(f"{self.get_name()} can not drift !!")  

    def carry_cargo(self):
        print(f"{self.get_name()} is not used to carry cargo !!")      


class truck(Vehicle):

    def drift(self,):
        print(f"{self.get_name()} can not drifting !!")    

# Create the objects
obj_bus = bus("TOYOTA", "Hiace", "White", "16 seats", "AAA 1111") 
obj_truck = truck("FORD", "F150", "Blue", "4 seats", "BBB 2222")

#Print the objects
obj_bus.VechileInfo()
print("")
obj_bus.drive()
obj_bus.drift()
obj_bus.carry_cargo()
print("---------------------")
obj_truck.VechileInfo()
print("")
obj_truck.drive()
obj_truck.drift()
obj_truck.carry_cargo()
