

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b



x = int(input("Enter value 1"))
y = int(input("Enter value 2"))

print("Add:", add(x, y))
print("Subtract:", subtract(x, y))
print("Multiply:", multiply(x, y))
print("Divide:", divide(x, y))


##################################################
###Write a program to import the math module and:
##
##Find the square root of a number.
##
##Calculate the sine of a number.
import math
num = float(input("Enter a number: "))
sqr= math.sqrt(num)
print("Square root:", sqr)
angldeg = float(input("Enter angle in degrees: "))
anglrad = math.radians(angldeg)
sineresult = math.sin(anglrad)
print("Sine of", angldeg, "degrees:", sineresult)

######################################################
#Create a module named greetings.py that has a function say_hello(name) which prints a greeting message. Import this module and call the function in another Python file.
def greetings(name):
    print(f"Hello, {name}! Welcome!")

name= input("Enter your name: ")
greetings(name)
##########################################################
###Use the random module to:
##
##Generate a random number between 1 and 100.
##
##Choose a random element from a list.
##
##Shuffle a list.
import random
randomnum = random.randint(1, 100)
print("Random number between 1 and 100:", randomnum)
items = ['a', 'b', 'c', 'd']
randomitem = random.choice(items)
print("Randomly chosen item:", randomitem)
random.shuffle(items)
print("Shuffled list:", items)

######################
#
from datetime import datetime, date
now = datetime.now()
print("Current date and time:", now)
print("Year:", now.year)
print("Month:", now.month)
print("Day:", now.day)
date1 = date(2023, 1, 1)
date2 = date(2025, 1, 1)

difference = date2 - date1
print("Days between", date1, "and", date2, ":", difference.days)



#########################
#
import time

t = time.strftime("%H:%M:%S")
print("Current time:", t)

print("Pausing for 3 seconds...")
time.sleep(3)
print("Resumed!")

s = time.time()

for i in range(1000000):
    pass

e = time.time()
print("Time taken:", e - s, "seconds")



