"""
02
Class Method and Self
Problem: Add a method to the Car class that displays the full name of 
the car (brand and model).
"""

class Car:
    def __init__(self, company, model):
        self.company = company
        self.model = model
    
    def displayName(self):
        print("Company - ", self.company, "and Model - ", self.model)

car01 = Car("Tata", "Harrier")
car01.displayName()