class Vehicle:
    def __init__(self, nabrandme,  name, color,capacity, plate_number):
        #instance properties / Attribues
        self.__nabrandme = nabrandme
        self.__name = name 
        self.__color = color
        self.__capacity = capacity 
        self.plate_number= plate_number

    #creating a setter and getter function for setting and getting attribute
    def set_nabrandme(self, nabrandme):
        self.__nabrandme = nabrandme
    def get_nabrandme(self):
        return self.__nabrandme
    def set_name(self, name):
        self.__name = name
    def get_name(self):
        return self.__name
    def set_color(self, color):
        self.__color = color
    def get_color(self):
        return self.__color
    def set_capacity(self, capacity):
        self.__capacity = capacity
    def get_capacity(self):
        return self.__capacity
    def set_plate_number(self, plate_number):
        self.__plate_number = plate_number
    def get_plate_number(self):
        return self.__plate_number

# crea methods 
    def drive(self):
        print(f"The {self.__name} is driving!")
    def drift(self):
        print(f"The {self.__name} is drifting!!")
    def carry_cargo(self):
        print(f"The {self.__name} is carrying cargo !!")

# creat sub-class  
class Truck(Vehicle):
    # override merthods   
    def carry_cargo(self):
        print(f"The {self.get_name()} {self.get_nabrandme()} is carrying cargo !!")
class Bus(Vehicle):
    # override merthods   
    def drift(self):
        print(f"The {self.get_name()}  can't drifting!!")
    def carry_cargo(self):
        print(f"The {self.get_name()}  isn't carrying cargo !!")

# creat objects
vehicle = Vehicle("Hyundai","Sonata","white",5,4545)
truck1 = Truck("volvo", "FMX", "gray",2,1234)
bus1 = Bus("gillig", "LLC", "black", 40, 1122)

vehicle.drift()
truck1.drift()
truck1.drive()
truck1.carry_cargo()

bus1.drive()
bus1.drift()
bus1.carry_cargo()