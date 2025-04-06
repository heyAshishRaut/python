"""
03
Inheritance
Problem: Create an ElectricCar class that inherits from the Car class and
has an additional attribute battery_size.
"""


class Car:
    def __init__(self, company, model):
        self.company = company
        self.model = model
    
    def displayName(self):
        print("Company - ", self.company, "and Model - ", self.model)

class ElectricCar(Car):
    def __init__(self, company, model, batterySize):
        super().__init__(company, model)
        self.batterySize = batterySize

car01 = ElectricCar("Tata", "Nexon-EV", "85kWh")
car01.displayName()
print(car01.batterySize)