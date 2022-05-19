class Vehicle :

    def __init__(self , brand , name  , color , capacity , plate_number ) :
        self.__brand = brand
        self.__name = name 
        self.__color = color
        self.__capacity=capacity
        self.__plate_number=plate_number
    
    def set_brand(self, brand):
        self.__brand = brand

    def get_brand(self):
        return self.__brand

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


    def drive(self) :
        print(f"{self.__name} the vehicle_name is driving!")
    
    def drift(self):
        print( f"{self.__name} the vehicle_name is drifting !!" )

    def carry_cargo(self):
        print(f"{self.__name} is carrying cargo !!") 
    def print_all(self):
        print(f"{self.get_brand()} , {self.get_name()} , {self.get_color()} , {self.get_capacity()} , {self.get_plate_number()}")
    
class Bus(Vehicle):
    def drift(self):
        print(f"{self.get_name()} is not drifting")

class Truck(Vehicle):
    def drift(self):
        print(f"{self.get_name()} " , " is not drifting")


car_1 = Vehicle ("GMC" , "Yukon" , "black" , 5 , 1234)
car_1.print_all()
car_1.drive()
car_1.drift()
car_1.carry_cargo()



Bus_1 = Bus("Hyundai" , "H1" , "white" , 10 , 2030)
Bus_1.print_all()
Bus_1.drive()
Bus_1.drift()
Bus_1.carry_cargo()
