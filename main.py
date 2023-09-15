# greeting with your name
name = input("Enter the Name: ")
print(f"Hello, {name}!")
print()


import math

radius = float(input("Enter the quantity of radius of the circle: "))


# The area of the circle will be calculated by using the formula: pi* (radius*2)
pi = math.pi
area = pi*(radius*2)


print(f"The area of the circle:  {area}")
print()

# Get the quantities of length and width of a rectangle from the user as input
length = float(input("Enter the quantity of length of a rectangle: "))
width = float(input("Enter the quantity of width of a rectangle: "))


perimeter = 2*(length+width)

Area = length * width

print(f"the perimeter of the rectangle: {perimeter}")
print(f"the area of the rectangle: {Area}")
print()

# Asking the 3 integer numbers from user as input
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
print()

print(f"sum of numbers: {num1+num2+num3}")

print(f"product of numbers: {num1*num2*num3}")

sumofnumber = int(num1+num2+num3)
print(f"average of numbers: {sumofnumber/3}")
print()

# Get the mass in medieval units from the user as input
talents = float(input("Enter talents:\n "))
pounds = float(input("Enter pounds:\n "))
lots = float(input("Enter lots:\n "))

onetalent = 20
onepound = 32
onelot = 13.3

totalpounds = (talents*20)+pounds
totallots = (totalpounds*32)
totalgrams = totallots*13.3

kilograms = int(totalgrams / 1000)
grams = totalgrams % 1000

print(f"The weight in modern units:\n {kilograms} kilograms and {grams:.2f} grams.")
