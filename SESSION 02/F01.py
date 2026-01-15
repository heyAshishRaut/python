"""
01
Basic Class and Object
Problem: Create a Car class with attributes like brand and model. Then 
create an instance of this class.
"""

class Car:
    def __init__(self, company, model):
        self.company = company
        self.model = model

car01 = Car("Tata", "Nexon")
print(car01.company)
print(car01.model)

# A class is a blueprint / template
# An object is a real instance created from a class

# def __init__(self, company, model):

# Called automatically when object is created
# Used to initialize data
# self refers to the current object