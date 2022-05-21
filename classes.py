

class Vehicle:
    
    def __init__(self,brand,name,color,capacity,plate_number):
        self.__brand= brand
        self.__name=name
        self.__color=color
        self.__capacity=capacity
        self.__plate_number=plate_number
    
    def get_brand(self):
        return self.__brand
    def set_brand(self,brand):
        self.__brand=brand
    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name=name
    def get_color(self):
        return self.__color
    def set_color(self,color):
        self.__color=color
    def get_capacity(self):
        return self.__capacity
    def set_capacity(self,capacity):
        self.__capacity=capacity
    def get_plate_number(self):
        return self.__plate_number
    def set_plate_number(self,plate_number):
        self.__plate_number=plate_number
    
    def drive(self):
        print(f"{self.__name} is driving")
    def drift(self):
        print(f"{self.__name} is drifting")
    def carry_cargo(self):
        print(f"{self.__name} is carring cargo")

class Bus(Vehicle):
    def drive(self):
        print(f"{self.get_name()} is driving")
    def drift(self):
        print(f"{self.get_name()} can not drifting")
    def carry_cargo(self):
        print(f"{self.get_name()} is cant carry cargo")

class Truck(Vehicle):
    def drive(self):
        print(f"{self.get_name()} is driving")
    def drift(self):
        print(f"{self.get_name()} can not drifting")
    def carry_cargo(self):
        print(f"{self.get_name()} is carrying cargo")


vehicle =Vehicle("GMC","Yukon","white","6","875 AED")
vehicle.drive()
vehicle.drift()
vehicle.carry_cargo()

truck=Truck("Mercedes","Actors","Blue","2","452 ASD")
truck.drive()
truck.drift()
truck.carry_cargo()

bus=Bus("Hyundai","H1","Black","9","987 RDH")
bus.drive()
bus.drift()
bus.carry_cargo()

