class Vehicle:
    def _init_(self, nabrandme,  name, color,capacity, plate_number):
        
        self.__nabrandme = nabrandme
        self.__name = name 
        self.__color = color
        self.__capacity = capacity 
        self.plate_number= plate_number

   
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

class Truck(Vehicle):
      
    def carry_cargo(self):
        print(f"The {self.get_name()} {self.get_nabrandme()} is carrying cargo !!")
class Bus(Vehicle):
     
    def drift(self):
        print(f"The {self.get_name()}  can't drifting!!")
    def carry_cargo(self):
        print(f"The {self.get_name()}  isn't carrying cargo !!")


vehicle = Vehicle("Toyota","..","black",3,3333)
truck1 = Truck("Toyota", "..", "red",3,1111)
bus1 = Bus("Toyota", "...", "blue", 5, 1111)

vehicle.drift()
truck1.drift()
truck1.drive()
truck1.carry_cargo()

bus1.drive()
bus1.drift()
bus1.carry_cargo()
