class Vehicle:

 def __init__(self,brand,name,color,capacity,plate_number) -> None:
        self.__brand = brand
        self.__name = name
        self.__color = color
        self.__capacity = capacity
        self.__plate_number = plate_number

def drive(self):
    print('The 'f'{self.__name}','is driving!')

def drift(self):
    print('The 'f'{self.__name}'," is drifting !!")

def carry_cargo(self):
    print('The 'f'{self.__name}',"is carrying cargo !!")

# Set and Get for Brand
def set_brand(self, brand):
        self.__brand = brand

def get_brand(self):
        return self.__brand

# Set and Get for name
def set_name(self, name):
        self.__name = name

def get_name(self):
        return self.__name

# Set and Get for color
def set_color(self, color):
    if isinstance(color, str):
        self.__color = color

def get_color(self):
        return self.__color

# Set and Get for capacity
def set_capacity(self, capacity):
        self.__capacity = capacity

def get_capacity(self):
        return self.__capacity

# Set and Get for plate_number
def set_plate_number(self, plate_number):
        self.__plate_number = plate_number

def get_plate_number(self):
        return self.__plate_number

v1=Vehicle('chevrolet','C4','Black',6,'2376')
v1.drive()
v1.drift()
v1.carry_cargo()

class Bus(Vehicle):
  def carry_cargo(self):
    print('The 'f'{self.__name}',"Cant carrying cargo !!")
  def drift(self):
    print('The 'f'{self.__name}'," Can not drifting !!")
b1=Bus('toyota','B21','white',20,'8756')
b1.carry_cargo()
b1.drift()


class Truck(Vehicle):
    def drift(self):
      print('The 'f'{self.__name}'," Can not drifting !!")
t1=Truck('kia','T6','Gray',2,'1998')
t1.drift()
 


