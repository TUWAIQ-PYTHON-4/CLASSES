'''
## define a Vehicle class . it has the following structure :

#### properties
- brand
- name
- color
- capacity
- plate_number
'''



class Vehicle:
    def __init__(self,brand,name,color,capacity,plate_number):
        self.__brand=brand
        self.__name=name
        self.__color=color
        self.__capacity=capacity
        self.plate_number=plate_number

    def set_brand(self,brand):
        self.__brand=brand
    def get_brand(self):
        return self.__brand
    
    def set_name(self,name):
        self.__name=name
    def get_name(self):
        return self.__name

    def set_color(self,color):
        self.__color=color
    def get_color(self):
        return self.__color

    def set_capacity(self,capacity):
        self.__capacity=capacity
    def get_capacity(self):
        return self.__capacity

    def set_plate_number(self,plate_number):
        self.__plate_number=plate_number
    def get_plate_number(self):
        return self.__plate_number

    

    '''
    #### methods
   - drive()
     prints "the vehicle_name is driving!"
   - drift()
     prints "the vehicle_name is drifting !!" or something else depending on the class.
   - carry_cargo()
     prints "the vehicle_name is carrying cargo !!" or something else depending on the class
    '''
    def drive(self):
        print("the "+self.get_name()+" is driving!")
    def drift(self):
        print("the "+self.get_name()+" is drifting !!")
    def carry_cargo(self):
        print("the "+self.get_name()+" is carrying cargo !!")
    
    
'''
    ### Create tow other subclasses (inherit from vehicle):
    - Bus
    - Truck
'''

class Bus(Vehicle):
    def drift(self):
        print(f"the {self.get_brand()} bus can drift")
    def carry_cargo(self):
        print(f"the {self.get_brand()} bus can't carry cargo")
bus1 = Bus("Yutong","Saleh","White","30","BBB111")
bus1.drive()  
bus1.carry_cargo() 
bus1.drift()


class Truck(Vehicle):
    def drift(self):
        print(f"the {self.get_brand()} Truck can't drift")
    def carry_cargo(self):
        print(f"the {self.get_brand()} Truck can carry cargo")
truck1 = Truck("Toyota","saad","White","3","TTT111")
truck1.drive()
truck1.drift()
truck1.carry_cargo()









