class Vehicle :
    def __init__(self,brand,name,color,capacity,plate_number) :
        self.__brand = brand
        self.__name = name
        self.__color = color
        self.__capacity = capacity
        self.__plate_number = plate_number

        

    def set_brand(self, brand):
        self.brand = brand

    def get_brand(self):
        return self.__brand


    def set_name(self, name):
           self.name = name
    
    def get_name(self):
            return self.__name



    def set_color(self, color):
           self.color = color

    def get_color(self):
            return self.__color



    def set_capacity(self, capacity):
           self.capacity = capacity

    def get_capacity(self):
            return self.__capacity



    def set_plate_nunber(self, plate_number):
           self.capacity = plate_number

    def get_plate_number(self):
            return self.__plate_number



    def drive(self):
         print(f"{self.__name} is driving!")
    def drift(self):
        print(f"{self.__name} is drifting !!")
    def carry_cargo(self):
        print(f"{self.__name} is carrying cargo !!")

car1 = Vehicle("Honda","Accord" ,"white" ,5,6)





class bus (Vehicle) :
    def drive(self):
        print(f"{self.get_name()} is can driving!")
    def drift(self):
        print(f"{self.get_name()} is can't drftinf!")

    def carry_cargo(self):
        print(f"{self.get_capacity()} is carrying cargo !!")

bus1=bus("honday","qwe","black",50,44)
bus1.drive()
bus1.drift()
bus1.carry_cargo()

class track(Vehicle):
    def drive(self):
        print(f"{self.get_name()} is can driving!")
    def drift(self):
         print (f"the {self.get_name()} can drifting")
    def carry_cargo(self):
         print(f"the {self.get_capacity()} is carrying cargo !!") 


 

car2 = track("Honda","Accord" ,"white" ,5,6)



car2.drive()
car2.drift()
car2.carry_cargo()




   

        