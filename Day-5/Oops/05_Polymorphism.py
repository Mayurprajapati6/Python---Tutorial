class Car:
    def __init__(self, brand, model):
        self.__brand = brand # now brand is private attribute means in this entire class it can use with __brand name
        self.model = model
    
    def full_name(self):
        return f"{self.__brand} {self.model}"

    def get_brand(self):
        return self.__brand + " !"
    
    def fuel_type(self):
        return "petrol or Diesel"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    
    def fuel_type(self):
        return "Electric charge"

my_tesla = ElectricCar("Tesla", "Model S", "85kwh")

print(my_tesla.fuel_type())

safari = Car("Tata", "Safari")

print(safari.fuel_type())
