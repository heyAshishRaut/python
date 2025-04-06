"""
01
Baics function syntax
Write a function to calculate and return the square of a number
"""

# def calSquare(num):
#     return num * num

# print(calSquare(4))

"""
02
Function with multiple parameter
Create a function that takes two numbers as parameters and return 
there sum 
"""

# def sumOFTwo(num1, num2):
#     return num1 + num2

# print(sumOFTwo(5, 10))

"""
03
Polymorphism in functions
Write a function multiply that mulitplies two number, but also 
accept string and multiply string
"""

# def multiply(one, two):
#     return one * two

# print(multiply("one", 3))

"""
04
Returning multiple values
Create a function that returns both area and circumferences of a 
circle given its radius
"""

# import math
# def areaAndCircum(radius):
#     return math.pi * (radius ** 2), 2 * math.pi * radius 

# area, circumference = areaAndCircum(5)
# print("Area - ", round(area, 2), " and Circumference - ", round(circumference, 2))

"""
05
Default parameter value
Write a function that greets a user. If no name provided, it should
greet with a default name
"""

# def greet(name = "folk"):
#     print("Hello ", name)

# greet("Ashish")

"""
06
Lambda function
Create a lambda function to complete the cube of a number
"""

# cube = lambda x : x ** 3
# print(cube(3))

"""
07
Function with *args
Write a function that takes variable number of arguments and
return their sum
"""

# def sumAll(*args):
#     # cal = 0
#     # for i in args:
#     #     cal = cal + i
#     # return cal
#     return sum(args)

# ans = sumAll(1, 2, 3, 4, 5)
# print(ans)

"""
08
Function with **kwargs
Create a function that accepts anny number of keywords argument
and print them in key - value format
"""

# def printKwargs(**kwargs):
#     for key, value in kwargs.items():
#         print(key, " - ", value)

# printKwargs(name = "Sher", power = "Meow")

"""
09
Generator function with yield
Write a generator function that yields even numbers up to a
specified limits
"""

# def printEven(limit):
#     for i in range(2, limit + 1, 2):
#         yield i

# for k in printEven(17):
#     print(k)

"""
10
Recursive function
Create a recursive function to calculate the factorial of a
number
"""

# def fact(num):
#     if(num == 1):
#         return 1
    
#     return num * fact(num - 1)

# print(fact(5))