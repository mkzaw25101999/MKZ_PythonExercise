# greet you by name
name = input("Enter the Name: ")
print(f"Hello, {name}!")
print()

# Get the quantity of radius of the circle from the user as input
import math

radius = float(input("Enter the quantity of radius of the circle: "))


# The area of the circle will be calculated by using the formula : pi* (radius*2)
pi = math.pi
area = pi*(radius*2)


# Prints out the area of the circle to user
print(f"The area of the circle:  {area}")
print()

# Get the quantities of length and width of a rectangle from the user as input
length = float(input("Enther the quantity of length of a rectangle: "))
width = float(input("Enter te quantity of width of a rectangle: "))

# the perimeter  of the rectangle will be calculated by using this formula: 2*(length+width)
perimeter = 2*(length+width)

# The area of the rectangle will be calculated by using this formula: (length*width)
Area = length * width

# Print out the perimeter and area of the rectangle to user
print(f"the perimeter of the rectangle: {perimeter}")
print(f"the area of the rectangle: {Area}")
print()

# Asking the 3 integer numbers from user as input
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
print()

# Calculation of sum of numbers
print(f"sum of numbers: {num1+num2+num3}")

# Calculation of product of numbers
print(f"product of numbers: {num1*num2*num3}")

# Calculation of average of numbers
sumofnumber = int(num1+num2+num3)
print(f"average of numbers: {sumofnumber/3}")
print()

# Get the mass in medieval units from the user as input
talents = float(input("Enter talents:\n "))
pounds = float(input("Enter pounds:\n "))
lots = float(input("Enter lots:\n "))

# convert the input values
onetalent = 20
onepound = 32
onelot = 13.3

# Calculation of the total mass in grams
totalGram = (talents * onepound + pounds) * onepound + lots * onelot

# Convert grams to kilograms and grams
kilograms = int(totalGram // 1000)
grams = totalGram % 1000

# Print out the weight in modern units to user
print(f"The weight in modern units:\n {kilograms} kilograms and {grams:.2f} grams.")
