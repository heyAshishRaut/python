"""
09
Class Inheritance and isinstance() Function
Demonstrate the use of isinstance() to check if my_tesla is an 
instance of Car and ElectricCar.
"""

class Car:
    def __init__(self, company, model):
        self.company = company
        self.model = model
    
    def display(self):
        print("Company - ", self.company, "and Model - ", self.model)
        print("Fuel type-  Petrol/Diesel")

class ElectricCar(Car):
    def __init__(self, company, model, batterySize):
        super().__init__(company, model)
        self.batterySize = batterySize
   
    def display(self):
        print("Company - ", self.company, "and Model - ", self.model)
        print("Fuel type-  Electric Charge")

car01 = ElectricCar("Tata", "Nexon-EV", "85kWh")

print(isinstance(car01, ElectricCar))
print(isinstance(car01, Car))

