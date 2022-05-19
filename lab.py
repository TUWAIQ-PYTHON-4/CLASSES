class Vehicle:
    def __init__(self,brand , name , color , capacity , plate_number) :
       self.__brand = brand
       self.__name= name 
       self.__color=color 
       self.__capacity=capacity
       self.__plare_number=plate_number
        
    def get_brand(self):
        return self.__brand
    def set_brand(self,x):
        self.__brand=x
    def get_name(self):
        return self.__name
    def set_name(self,x):
        self.__name=x
    def get_color(self):
        return self.__color
    def set_color(self,x):
        self.__color=x
    def get_capacity(self):
        return self.__capacity
    def set_capacity(self,x):
        self.__capacity=x 
    def get_plate_number(self):
        return self.__plare_number
    def set_plate_number(self,x):
        self.__plare_number= x
        

    def bus_info(self):
        print(f"Bus name: {self.__name} from the : {self.__brand} \n")
    def truck_info(self):
        print(f"Truck name: {self.__name} from the : {self.__brand} \n")

class Bus(Vehicle):
    def __init__(self, brand, name, color, capacity, plate_number , size):
        self.__size= size
        super().__init__(brand, name, color, capacity, plate_number)
        
    def drive(self):
        print(f"The {self.get_name()} is driving ")
    def drift(self):
        print(f"the {self.get_name()} is not drifting !!")
    def carry_cargo(self):
        print(f"the {self.get_name()} is not carrying cargo !!")
    def bus_size(self):
        print(f"the {self.get_name()} size is {self.__size}")
    
bus1 = Bus("Mercedes-Benz","daimler","black",400.0,"5785 - EWQ","Mini")
bus2 = Bus("Xiamen Golden dragon Bus","Golden Dragon","gold",800.0,"7555 - AB","big")

bus1.bus_info()
bus1.drive() 
bus1.drift()
bus1.carry_cargo()
bus1.bus_size()
print("______________________________\n")
bus2.bus_info()
bus2.drive() 
bus2.drift()
bus2.carry_cargo()
bus2.bus_size()
    
    
class Truck(Vehicle):
    def drive(self):
        print(f"The {self.get_name()} is driving ")
    def drift(self):
        print(f"the {self.get_name()} is drifting !!")
    def carry_cargo(self):
        print(f"the {self.get_name()} is carrying cargo !!")
    def not_drift(self):
        print(f"the {self.get_name()} is not drifting !!")
  
truck1 = Truck("Toyota","tacoma Access Cab","red" ,600.22,'7824 - KSA')
truck2 = Truck(" Nissan","frontier King Cab","blue" ,745.22,'9099 - RAA')

print("______________________________\n")
truck1.truck_info()
truck1.drive() 
truck1.drift()
truck1.carry_cargo()
print("______________________________\n")
truck2.truck_info()
truck2.drive() 
truck2.not_drift()
truck2.carry_cargo()
    