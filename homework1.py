class Vechil:
    def __init__(self,brand,name,color,capacity,plate_number) :
        self.__bbrand=brand
        self.__nname=name
        self.__ccolor=color
        self.__ccapacity=capacity
        self.__pplate_number=plate_number


    def drive(self):
        return f"he {self.__nname} is  driving! "
    def drift(self):
        
            return f"the  {self.__nname} is not drifting"
    
    def carry_cargo(self):
        return f"the  {self.__nname} carrying cargo= {self.__ccapacity} !!"


bus=Vechil('Toyota','bus1','black','10','44444 cde')
truck=Vechil('Hyundai','H1','white','30','3333333 abc')



class Bus(Vechil):
    print(bus.drive())
    print(bus.drift())
    print(bus.carry_cargo())
class Truck(Vechil):
    print(truck.drive())
    print(truck.drift())
    print(truck.carry_cargo())





