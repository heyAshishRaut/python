"""
05
Polymorphism
Demonstrate polymorphism by defining a method fuel_type in both 
Car and ElectricCar classes, but with different behaviors.
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
car01.display()

car02 = Car("Tata", "Nexon")
car02.display()