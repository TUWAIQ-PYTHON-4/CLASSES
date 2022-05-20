class Vehicle:

    def __init__(self,name,brand,color,capacity,plate_number):
        self.__name=name
        self.__brand=brand
        self.__color=color
        self.__capacity=capacity
        self.__plate_number=plate_number


    def car(self):
            self.__drive()
            print(f"{self.__name()} is driving!")
            self.__drift()
            print(f"{self.__name()}is drifting !!")
            self.__carry_cargo()
            print(f"{self.__name()} is carrying cargo !!")
            
    def set_name(self, name):
            self.__name = name

    def get_name(self):
            return self.__name  


    def set_brand(self, brand):
            self.__brand = brand

    def get_brand(self):
            return self.__brand  


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


class Bus(Vehicle):
    
    def drive(self):
        print(f"{self.get_name()} is driving!")

    def drift(self):
        print(f"{self.get_name()} can't drifting!")

    def carry_cargo(self):
        print(f"{self.get_name()} can't carrying cargo")
           
    
Bus1 = Bus("school bus" , "ford" , "yellow" , "90 passengers", "78566")
Bus1.drive()
Bus1.drift()
Bus1.carry_cargo()


class Truck (Vehicle):

    def drive(self):
        print(f"{self.get_name()} is driving!")

    def drift(self):
        print(f"{self.get_name()} can't drifting!")

    def carry_cargo(self):
        print(f"{self.get_name()} is carrying cargo !!")
           
Truck1 = Truck("Cargo Truck", "mercedes ","white","2 passengers","87599")
Truck1.drive()
Truck1.drift()
Truck1.carry_cargo()


               







