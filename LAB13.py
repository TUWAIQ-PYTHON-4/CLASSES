
# define a Vehicle class . it has the following structure :
from turtle import color


class Vehicle:

    # properties brand, name, color, capacity, plate_number
    def __init__(self, brand: str, name: str, color: str, capacity: str, plate_number: str):
        self.brand= brand
        self.name = name
        self.color = color
        self.capacity = capacity
        self.plate_number= plate_number

    # methods
    def VechileInfo(self,): ## for print the detalis about the vechile
        print("Brand:", self.brand, "|", "Name:", self.name,"|", "Color:", self.color,"|", "Capacity:", self.capacity,"|", "Plate N0:", self.plate_number)

    def drive(self,):
        print(f"{self.name} is driving!")

    def drift(self):
        print(f"{self.name} is drifting !!")  

    def carry_cargo(self):
        print(f"{self.name} is carrying cargo !!")  

    # for each of the properties do a setter & getter (encabsulate the data).
    def set_name(self, name):
        self.name = name

    def set_brand(self, brand):
        self.brand = brand

    def set_color(self, color):
        self.color = color

    def set_capacity(self, capacity):
        self.capacity = capacity

    def set_plate_number(self, plate_number):
        self.plate_number = plate_number

    def get_brand(self):
        return self.brand

    def get_name(self):
        return self.name

    def get_color(self):
        return self.color

    def get_capacity(self):
        return self.capacity

    def get_plate_number(self):
        return self.plate_number    

# creating inheritance class from Vechile
class bus(Vehicle):

    def drift(self):
        print(f"{self.name} can not drift !!")  

    def carry_cargo(self):
        print(f"{self.name} is not used to carry cargo !!")      


class truck(Vehicle):
    def drive(self,):
        print(f"{self.name} is driving!")

    def drift(self,):
        print(f"{self.name} can not drifting !!")    

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
