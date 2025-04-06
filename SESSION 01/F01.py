"""
Description -
Assignment on conditional statements
"""



"""
01
Age group categorization
classify a person age group - child (1 < 13), teenager (13 - 19), adult 
(20 - 59), senior (60+)
"""

# age = int(input("Enter your age - "))
# if (age >= 1 and age < 13):
#     print("Child")
# elif (age >= 13 and age <= 19):
#     print("Teenager")
# elif(age >= 20 and age <= 59):
#     print("Adult")
# else :
#     print("Senior")

"""
02
Movie ticket pricing
Movie tickets are priced based on age $12 for adults (18 and above)
, $8 for childrens, and everyone gets a $2 discount of wednesday
"""

# age = int(input("Enter age - "))
# day = input("Enter day - ").lower()

# price = 0;

# if (age >= 1 and age < 18) :
#     price = 8
# elif (age >= 18) :
#     price = 12
# else :
#     price = -1

# if (price > 0) :
#     if(day == "wednesday") :
#         print("Price is ", price - 2)
#     else :
#         price("Price is ", price)
# else :
#     print("Invalid entry")

"""
03
Grade calculator
Assign letter's grade based n student's score
A - [90, 100]
B - [80, 89]
C - [70, 79]
D - [60, 69]
F - [below 60]
"""

# score = int(input("Enter score - "))

# if (score >= 90 and score <= 100):
#     print("A")
# elif (score >= 80 and score <= 89):
#     print("B")
# elif (score >= 70 and score <= 79):
#     print("C")
# elif (score >= 60 and score <= 69):
#     print("D")
# elif (score < 0) :
#     print("invalid entry")
# else :
#     print("F")

"""
04
Fruit ripeness checker
Determine if a fruit is ripe, overripe or unripe based on its color
"""

# fruitColor = input("Enter color - ").lower()

# if(fruitColor == "green"):
#     print("unripe")
# elif (fruitColor == "yellow"):
#     print("ripe")
# else:
#     print("overripe")

"""
05
Weather activity suggestion
Suggest an activity based on weather (Sunny - Go for a walk),
(Rainy - Read a book), and (Snowy - Build a snowman)
"""

# weather = input("Enter weather")

# if(weather == "Sunny"):
#     print("Go for a walk")
# elif(weather == "Rainy"):
#     print("Read a book")
# else:
#     print("Build a snowman")

"""
06
Transportation mode selection
Choose mode of transportation based on distance
(< 3 km - walk), ([3, 15]km - bike), and ( > 15 km - car)
"""

# distance = int(input("Enter distance"))

# if (distance < 3):
#     print("Walk")
# elif (distance > 3 and distance <= 15):
#     print("Bike")
# else: 
#     print("Car")

"""
07
Coffee customization
Customize a coffee order - small, medium, and large. With an option
for "extra shot" of espresso
"""

# size = input("Enter coffee size - ").lower()
# extraShot = input("Did you need extra shot of espresso ? ").lower()

# boolExtraShot = True
# if(extraShot == "no"):
#     boolExtraShot = False

# if boolExtraShot:
#     print("Coffee size - ", size, " with extra shot of Espresso")
# else:
#     print("Coffe size - ", size, " with no extra shot of Espresso")

"""
08
Password Checker
"""

# password = input("Enter password - ")

# strength = {
# "capital" : False,
# "small" : False,
# "number" : False,
# "special" : False,
# "length" : False
# }

# if(len(password) > 8):
#     strength["length"] = True

# for ch in password:
#     if ch.isupper():
#         strength["capital"] = True

#     if ch.islower():
#         strength["small"] = True

#     if ch in "@#$%^&*!":
#         strength["special"] = True

#     if ch.isdigit():
#         strength["number"] = True

# count = 0

# criteria_met = sum(strength.values())

# if(criteria_met == 5):
#     print("Strength - Strong")
# elif(criteria_met >= 3):
#     print("Strength - Moderate")
# else:
#     print("Strength - Weak")

"""
09
Leap Year
A year is a leap year if:
Divisible by 400 
OR
Divisible by 4 AND NOT divisible by 100  
"""

# year = int(input("Enter year - "))

# if(year % 400 == 0):
#     print("Leap year")
# elif(year % 4 == 0 and year % 100 != 0):
#     print("Leap year")
# else:
#     print("Not a Leap year")

"""
10
Pet food recommendation
Recommend a type of pet food based on pet's species and age
Dog < 2 - Puppy food
Cat > 5 - Senior cat food  
"""

# species = input("Enter species - ").lower()
# age = int(input("Enter age - "))

# if(species == "dog" and age < 2):
#     print("Puppy Food")
# elif(species == "cat" and age > 5):
#     print("Senior cat food")
# else:
#     print("Normal food")