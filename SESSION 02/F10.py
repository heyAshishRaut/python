"""
10
Multiple Inheritance
Create two classes Battery and Engine, and let the ElectricCar class 
inherit from both, demonstrating multiple inheritance.
"""

class Battery:
    def __init__(self, batterySize):
        self.batterySize = batterySize

    def battery_info(self):
        return f"Battery Size: {self.batterySize} kWh"


class Engine:
    def __init__(self, powerOutput):
        self.powerOutput = powerOutput

    def engine_info(self):
        return f"Power Output: {self.powerOutput} HP"


class ElectricCar(Battery, Engine): 
    def __init__(self, company, model, batterySize, powerOutput):
        Battery.__init__(self, batterySize)
        Engine.__init__(self, powerOutput)
        self.company = company
        self.model = model

    def display(self):
        print(f"Company: {self.company}, Model: {self.model}")
        print(self.battery_info())
        print(self.engine_info())
        print("Fuel Type: Electric Charge")


my_tesla = ElectricCar("Tesla", "Model S", 100, 1020)
my_tesla.display()
