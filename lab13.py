class Vehicle:
    
    def __init__(self,brand,name,color,capacity,plate_number):
        self.__brand = brand
        self.__name = name
        self.__color = color
        self.__capacity = capacity
        self.__plate_number = plate_number
    
    def set_brand(self, brand):
        if isinstance(brand, str):
            self.__brand = brand

    def get_brand(self):
        return self.__brand
    
    def set_name(self, name):
        if isinstance(name, str):
            self.__name = name

    def get_name(self):
        return self.__name

    def set_color(self, color):
        if isinstance(color, str):
            self.__color = color

    def get_color(self):
        return self.__color

    def set_capacity(self, capacity):
        if isinstance(capacity, int):
            self.__capacity = capacity

    def get_capacity(self):
        return self.__capacity

    def set_plate_number(self, plate_number):
        if isinstance(plate_number, int):
            self.__plate_number = plate_number

    def get_plate_number(self):
        return self.__plate_number
    
    def drive(self):
        print(f"The {self.get_name()} is driving!")
    def drift(self):
        print(f"The {self.get_name()} is drifting !!")
    def carry_cargo(self):
        print(f"The {self.get_name()} is carrying cargo !!")

class bus(Vehicle):
    def drift(self):
        print(f"The {self.get_name()} can not drift !!")
    def drift(self):
        print(f"The {self.get_name()} can not carry cargo !!")

class truck(Vehicle):
    def drift(self):
        print(f"The {self.get_name()} can not drift !!")

bus1 = bus("Toyota","lors","White & Bronze",49,115488875)
bus1.drive()
bus1.drift()
bus1.carry_cargo()

truck1 = truck("Mercedes","G900","White",3,14986515)
truck1.drive()
truck1.drift()
truck1.carry_cargo()

car1 = Vehicle("chevrolet","Camaro","Red",4,995546563)
car1.drive()
car1.drift()
car1.carry_cargo()