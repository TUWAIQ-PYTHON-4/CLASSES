# CLASSES

## define a Vehicle class . it has the following structure :
### Note
# - override  the methods as needed for each subclass of vehicle. 
# - create at least one object of each class.
# - call all the methods on each object. 

class Vehicle:
    # Initalizer
    def __init__(self, brand, name, color,capacity, plate_number):
        
        #### properties
        self.__brand = brand
        self.__name = name
        self.__color = color
        self.__capacity = capacity
        self.__plate_number = plate_number

    #### for each of the properties do a setter & getter (encabsulate the data).
    # getter method
    def get_brand(self):
        return self.__brand

    def get_name(self):
        return self.__name

    def get_color(self):
        return self.__color

    def get_capacity(self):
        return self.__capacity
        
    def get_plate_number(self):
        return self.__plate_number
      
    # setter method
    def set_brand(self, x):
        self.__brand = x
    def set_name(self, x):
        self.__name = x
    def set_color(self, x):
        self.__color = x
    def set_capacity(self, x):
        self.__capacity = x
    def set_plate_number(self, x):
        self.__plate_number = x
    
    #### methods
    def drive(self):
        print("the {} is driving !!".format(self.__name))
    def drift(self):
        print("the {} is drifting !!".format(self.__name)) # or something else depending on the class.
    def carry_cargo(self):
        print("the {} is carrying cargo !!".format(self.__name)) # or something else depending on the class

### Create tow other subclasses (inherit from vehicle):
class Bus(Vehicle):
    # Initalizer
    #def __init__(self):
        #### properties
        #super().__init__()
    
    # polymorphism / overriding the super fly method
    def drift(self):
        return super().drift() # calling the parent class drift() method
        print('the {} can not drift !!'.format(self.get_name()))

class Truck(Vehicle):
    # Initalizer
    #def __init__(self):
        #### properties
        #super().__init__()
    
    def carry_cargo(self):
        return super().carry_cargo()
        print('the {} can not carry cargo !!'.format(self.get_name()))


# Objects 
vehicle = Vehicle('tesla','x','white',4,'111 AAA')
vehicle.drive()
vehicle.drift()
vehicle.carry_cargo()

bus = Bus('toyota','hiace','Black',24,'123 ABC')
bus.drive()
bus.drift()
bus.carry_cargo()

truck = Truck('mercedes','maybach','navy',4,'0 ASD')
truck.drive()
truck.drift()
truck.carry_cargo()



