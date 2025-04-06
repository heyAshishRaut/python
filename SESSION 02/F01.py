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