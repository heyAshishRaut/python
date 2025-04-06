"""
06
Class Variables
Add a class variable to Car that keeps track of the number of 
cars created.
"""

class Car:
    noOfVehicles = 0

    def __init__(self, company, model):
        self.company = company
        self.model = model

        Car.noOfVehicles += 1

car01 = Car("Tata", "Tiago")
car02 = Car("Tata", "Nexon")
car03 = Car("Tata", "Nexon")

print(Car.noOfVehicles)
    