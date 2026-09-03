class Car:
    total_car = 0

    def __init__(self, brand, model):
        self.__brand = brand # now brand is private attribute means in this entire class it can use with __brand name
        self.__model = model
        Car.total_car += 1
    
    def full_name(self):
        return f"{self.__brand} {self.__model}"

    def get_brand(self):
        return self.__brand + " !"
    
    def fuel_type(self):
        return "petrol or Diesel"
    
    @staticmethod
    def general_description():
        return "Cars are means of transport"
    
    @property
    def model(self):
        return self.__model 

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    
    def fuel_type(self):
        return "Electric charge"

my_tesla = ElectricCar("Tesla", "Model S", "85kwh")

my_car = Car("Tata", "Safari")
# my_car.model = "City" -> can't possible

print(my_car.model)





