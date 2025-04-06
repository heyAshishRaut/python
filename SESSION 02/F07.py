"""
07
Static Method
Add a static method to the Car class that returns a general 
description of a car.
"""

class Car:
    def __init__(self, company, model):
        self.company = company
        self.model = model
    
    @staticmethod
    def display():
        print("Tarzan - the wonder car")

# 01
car01 = Car("Tata", "Nexon")
car01.display()

# 02
Car.display()
