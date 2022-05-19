class Vehicle:
    def __init__(self, brand: str = 'defuallt', name: str = 'defuallt', color: str = 'defuallt',
                 capacity: str = 'defuallt', plate_number: str = 'defuallt') -> None:
        self.__brand = brand
        self.__name = name
        self.__color = color
        self.__capacity = capacity
        self.__plate_number = plate_number

    def __set_name__(self, name):
        self.__name = name

    def __set_brand__(self, brand):
        self.__brand = brand

    def __set_color__(self, color):
        self.__color = color

    def __set_capacity__(self, capacity):
        self.__capacity = capacity

    def __set_plate_number__(self, plate_number):
        self.__plate_number = plate_number

    def get_name(self):
        return self.__name

    def get_brand(self):
        return self.__brand

    def get_color(self):
        return self.__color

    def get_capacity(self):
        return self.__capacity

    def get_plate_number(self):
        return self.__plate_number

    def drive(self):
        print(f"the {self.__name} is driving!")

    def drift(self):
        print(f"the {self.__name} is drifting !!")

    def carry_cargo(self):
        print(f"the {self.__name} is carrying cargo !!")


class Bus(Vehicle):
    def drive(self):
        print(f"the Bus named {self.get_name()} is driving!")

    def drift(self):
        print(f"the Bus named {self.get_name()} can not drift...")

    def carry_cargo(self):
        print(f"the Bus named {self.get_name()} is carrying cargo !!")


class Truck(Vehicle):
    def drive(self):
        print(f"the Truck named {self.get_name()} is driving!")

    def drift(self):
        print(f"the Truck named {self.get_name()} can not drift...")

    def carry_cargo(self):
        print(f"the Truck named {self.get_name()} is carrying cargo !!")


v1, v2, v3 = Vehicle(name='Veachl in super'), Bus(name='bus1'), Truck(name='Truck1')

v1.drift()
v1.drift()
v1.carry_cargo()

v2.drive()
v2.drift()
v2.carry_cargo()

v3.drive()
v3.drift()
v3.carry_cargo()


