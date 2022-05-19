class Vehicle():
    #### properties
    def __init__(self,brand,name,color,capacity,plate_number):
        self.__brand = brand
        self.__name = name
        self.__color = color
        self.__capacity = capacity
        self.__plate_number = plate_number


### for each of the properties do a setter & getter (encabsulate the data).

    def set_brand(self,brand):
        self.__brand = brand

    def get_brand(self):
        return self.__brand

    def set_name(self,name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_color(self,color):
        self.__color = color

    def get_color(self):
        return self.__color

    def set_capacity(self,capacity):
        self.__capacity = capacity

    def get_capacitye(self):
        return self.__capacity
        
    def set_plate_number(self,plate_number):
        self.__plate_number = plate_number

    def get_plate_number(self):
        return self.__plate_number

    
    
    #### methods
    def drive(self):
        print(f"{self.__name} is driving!")
    def drift(self):
        print(f"{self.__name} is drifting !!")
    def carry_cargo(self):
        print(f"{self.__name} is carrying cargo !!")


### Create tow other subclasses (inherit from vehicle):
b = Vehicle("car","car_1","blue",87,"68")
b.drive()

class Bus(Vehicle):
    
    def drive(self):
        print(f"{self.get_name()} is driving!")

    def carry_cargo(self):
        print(f"{self.get_capacitye()} is carrying cargo !!")

bus_1 = Bus("Toyota","bus1","black",25,"0453")
bus_1.drive()
bus_1.carry_cargo()



class Truck(Vehicle):
    def drift(self):
        print(f"{self.get_name()} is drifting !!")
    
    def carry_cargo(self):
        print(f"{self.get_capacitye()} is carrying cargo !!")


truck_1 = Truck("Ford","truck1","green",4,"9754") 

truck_1.drift()
truck_1.carry_cargo()





