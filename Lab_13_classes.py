
class Vehicle:

     #create objects for calss vehicle
    def __init__(self, brand, name, color, capacity, plate_number) -> None:
        
        self.__brand = brand
        self.__name = name
        self.__color = color
        self.__capacity = capacity
        self.__plate_number = plate_number
        
     #hiring (setter & getter) for object private 
    def set_brand(self, brand):
        if isinstance(brand, str):
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
        if isinstance(plate_number, int):
            self.__plate_number = plate_number

    def get_plate_number(self):
        return self.__plate_number

    #create methods for class
    def drive(self):
        print(f'The {self.get_brand()} {self.get_name()} is driving!')
    
    def drift(self):
        print(f'The {self.get_brand()} {self.get_name()} is drifting !!')

    def carry_cargo(self):
        print(f'The {self.get_brand()} {self.get_name()} {self.get_capacity()} is carrying cargo !!')
 # create class inheritance for class vehicle
class Bus (Vehicle):
    #create objects for calss bus
    def add_object(self,model):

         self.model = model

    #create methods for class
    def drift(self):
        print(f"The {self.get_brand()} {self.get_name()}  is can't drifting !!")
    
    def carry_cargo(self):
        print(f'The {self.get_brand()} {self.get_name()} {self.get_capacity()} is carrying cargo !!')


# create another class inheritance for class vehicle
class Truck(Vehicle):
    #create objects for calss truch
    def add_object(self, molar_capacity):

        self.molar_capacity = molar_capacity

    
    #create methods for class
    def drive(self):
        print(f"The {self.get_brand()} {self.get_name()} is driving!")

    def carry_cargo(self):
        print(f'The {self.get_brand()} {self.get_name()} is carrying cargo !!')

#call all the methods on each object
print("-" * 80)
vehicle = Vehicle("Chevrolet", "Malibu", "White", 5, 1000230110)
vehicle.drive()
vehicle.drift()
vehicle.carry_cargo()
print("-" * 80)


bus = Bus("Nissan", "NV350", "Yellow", 35, 1000240110)
bus.drift()
bus.carry_cargo()
print("-" * 80)


truck = Truck("Mercedes", "G900", "Black", 2, 1000250110)
truck.drive()
truck.carry_cargo()




