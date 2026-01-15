"""
04
Encapsulation
Problem: Modify the Car class to encapsulate the brand attribute, making 
it private, and provide a getter method for it.
"""

class Car:
    def __init__(self, company, model):
        # Python renames private variables
        self.__company = company
        self.model = model
    
    def getCompany(self):
        return self.__company
    
car01 = Car("Tata", "Nexon")
ans = car01.getCompany()
print(ans)