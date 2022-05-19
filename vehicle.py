class Vehicle:

    def __init__(self, *args):

        
        if len(args) == 5:
            self.brand = args[0]
            self.name = args[1]
            self.color = args[2]
            self.capacity = args[3]
            self.plate_number = args[4]

        
        elif len(args) == 0:
            pass

    
    def get_brand(self):
        return self.brand

    def set_brand(self, b):
        self.brand = b

    def get_name(self):
        return self.name

    def set_name(self, n):
        self.name = n

    def get_color(self):
        return self.color

    def set_color(self, c):
        self.color = c

    def get_capacity(self):
        return self.capacity

    def set_capacity(self, c):
        self.capacity = c

    def get_plate_number(self):
        return self.plate_number

    def set_plate_number(self, pn):
        self.plate_number = pn

    def drive(self):
        print("The", self.name, "is driving!")

    def drift(self):
        print("The", self.name, "is drifting !!")

    def carry_cargo(self):
        print("The", self.name, "is carrying cargo !!")


class Bus(Vehicle):
    def drive(self):
        print("The Bus is driving!")

    def drift(self):
        print("The Bus can't drifting !!")

    def carry_cargo(self):
        print("The Bus can't carrying cargo !!")


class Truck(Vehicle):

    def drive(self):
        print("The Truck is driving!")

    def drive(self):
        print("The Truck can't drifting !!")

    def carry_cargo(self):
        print("The Truck is carrying cargo !!")


vehicle = Vehicle("Hyundai", "Azera", "Black", 5, 5443)
print("\nVehicle Info:")
print("Brand:",vehicle.get_brand(), "\nName:",vehicle.get_name(), "\nColor:",vehicle.get_color(),
      "\nCapacity:", vehicle.get_capacity(), "\nPlate Number:", vehicle.get_plate_number())
vehicle.drive()
vehicle.drift()
vehicle.carry_cargo()

bus = Bus("Nissan", "Mini van", "White", 12, 1234)
print("\nBus Info:")
print("Brand:", bus.get_brand(), "\nName:",bus.get_name(), "\nColor:",bus.get_color(),
      "\nCapacity:", bus.get_capacity(), "\nPlate Number:", bus.get_plate_number())
bus.drive()
bus.drift()
bus.carry_cargo()

truck = Truck()
truck.set_brand("Hyundai")
truck.set_name("H350")
truck.set_color("Gray")
truck.set_capacity(14)
truck.set_plate_number(6278)

print("\nTruck Info:")
print("Brand:", truck.get_brand(), "\nName:", truck.get_name(), "\nColor:", truck.get_color(),
      "\nCapacity:", truck.get_capacity(), "\nPlate Number:", truck.get_plate_number())
truck.drive()
truck.drift()
truck.carry_cargo()
