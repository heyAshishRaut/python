"""
Leap Year
A year is a leap year if:
Divisible by 400 
OR
Divisible by 4 AND NOT divisible by 100  
"""

year = int(input("Enter year - "))

if(year % 400 == 0):
    print("Leap Year")
if(year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

# dict → key-value
# list → ordered & mutable
# tuple → ordered & immutable

"""
Baics function syntax
Write a function to calculate and return the square of a number
"""

def calSquare(num):
    return num * num

print(calSquare(4))