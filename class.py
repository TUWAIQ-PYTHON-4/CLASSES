'''
# CLASSES

## define a Vehicle class . it has the following structure :

#### properties
- brand
- name
- color
- capacity
- plate_number


#### methods
- drive()
  prints "the vehicle_name is driving!"
- drift()
  prints "the vehicle_name is drifting !!" or something else depending on the class.
- carry_cargo()
  prints "the vehicle_name is carrying cargo !!" or something else depending on the class


### for each of the properties do a setter & getter (encabsulate the data).

### Create tow other subclasses (inherit from vehicle):
- Bus
- Truck


### Note
- override  the methods as needed for each subclass of vehicle. 
- create at least one object of each class.
- call all the methods on each object. 

'''

class Vehicle:
    def __init__(self,brand,name,color,capacity,plate_number):

        def drive():
            print(f"{self.name} is driving!!")
        def drift():
            print("the vehicle_name is drifting !!")
        def carry_cargo():
            print(f"{self.name} is carring cargo!!")

new_car = Vehicle("toyota", "camry","white","5","1 2 3") #this is object ==> instance of the class

print(new_car.name())
new_car.drive()


#inhertince 
class Bus(Vehicle):

    def drift(self):
      print (f"{self.get_name()} can't drifting") # polymorphism // ovverrided super 




class Truck(Vehicle):
   def drift(self):
      print (f"{self.get_name()} can't drifting") # polymorphism // ovverrided super 


bus1 = Bus('H','dd','black','20','192')

truck1 = Truck('H','dd','black','20','192')