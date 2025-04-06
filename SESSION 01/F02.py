"""
Description -
Assignment on loops
"""



"""
01
Counting positive numbers
Given a list of numbers, count how many are +ve
numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
"""

# count  = 0
# numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
# for num in numbers:
#     if(num  > 0):
#         count = count + 1

# print("Total positive numbers are - ", count)

"""
02
Sum of even numbers
Calculate sum of even numbers up to a given number n
"""

# num = int(input("Enter number - "))
# sum = 0
# for i in range(1, num):
#     if(i % 2 == 0):
#         sum = sum + i

# print("Sum of even numbers till ", num, " is ", sum)

"""
03
Multiplication table printer
"""

# num = int(input("Enter number - "))
# for i in range(1, 11):
#     if(i == 5):
#         continue
#     print(num, " X ", i, " = ", num * i)

"""
04
Reverse a string
"""

# str = input("Enter a string - ")
# ans = ""

# for ch in range(len(str) - 1, -1, -1):
#     ans = ans + str[ch]
# print(ans)


"""
05
Find first non-repeating character
"""

# str = input("Enter string - ")
# ans = False
# e = ""
# for ch in str:
#     if(str.count(ch) == 1):
#         ans = True
#         e = ch
#         break
# if(ans):
#     print("First non-repeating character is - ", e)
# else:
#     print("No non-repeating character is present")

"""
06
Calculate factorial
"""

# fact = int(input("Enter number - "))
# ans = 1

# for i in range(1, fact + 1):
#     ans = ans * i

# print("factorial of ", fact, " is ", ans)

# j = 1
# while(j <= fact):
#     ans = ans * j
#     j = j + 1
# print("factorial of ", fact, " is ", ans)

"""
07
Validate input
Keep asking the user of input unless until they enter a number between 1 and 10
"""

# while True:
#     user = int(input("Enter a number - "))
#     if(user >= 1 and user <= 10):
#         print("validated!")
#         break

"""
08
Prime number checker
"""

# count = 0
# user = int(input("Enter a number - "))
# for i in range(1, user + 1):
#     if(user % i == 0):
#         count += 1
#     if(count > 2):
#         print("Not a prime number")
#         break
# if(count <= 2):
#     print("Prime number")

"""
09
Uniqueness in list
check if all elements in an list are unique. If duplicates found,
exit the loop and print the duplicate
"""

# items = ["apple", "banana", "orange", "apple", "mango"]

# for i in items:
#     if items.count(i) > 1:
#         print(i)
#         break;

"""
10
Exponential backoff
Implement an exponential backoff strategy that doubles the wait 
time between retries, starting from 1 sec, but stop after 5 sec
"""

# import time

# waitTime = 1
# maxRetries = 5
# attempt = 0

# while attempt < maxRetries:
#     print("Attempt ", attempt + 1, ", Wait time ", waitTime)
#     time.sleep(waitTime)
#     waitTime *= 2
#     attempt += 1
