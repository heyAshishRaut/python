"""
08
Property Decorators
Use a property decorator in the Car class to make the model 
attribute read-only.
"""

class Car:
    def __init__(self, company, model):
        self.company = company
        self.__model = model
    
    @property
    def model(self):
        return self.__model
    
car01 = Car("Tata", "Nexon")
print(car01.model)