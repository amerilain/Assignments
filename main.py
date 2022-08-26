import math
import random
"""
# phase 1
name = input("What is Your name? ")
print("hello, " + name + "!")

# phase 2
radius = float(input("What is the radius of the circle? "))
print(f"The area of the circle is {math.pi * (radius ** 2):.2f}")

# phase 3
length = float(input("What is the length? "))
width = float(input("What is the width? "))
print(f"The perimeter of the rectangle is {(length * 2) + (width * 2):.2f}")
print(f"The area of the rectangle is {length * width:.2f}")

# phase 4
num1 = float(input("enter a number: "))
num2 = float(input("enter a number: "))
num3 = float(input("enter a number: "))

print(f"The sum of your numbers is {num1 + num2 + num3:.0f}")
print(f"The product of your numbers is {num1 * num2 * num3:.0f}")
print(f"The average of your numbers is {(num1 + num2 + num3)/3:.2f}")
"""
# Write a program that asks the user to enter a mass in medieval units:
# talents (leiviskä), pounds (naula), and lots (luoti).
# The program converts the input to full kilograms and grams and outputs the result to the user:
# One talent is 20 pounds.
# One pound is 32 lots.
# One lot is 13,3 grams.

talents = float(input("Enter talents:\n"))
pounds = float(input("Enter pounds:\n"))
lots = float(input("Enter lots:\n"))

talent_grams = float(talents * 20 * 32 * 13.3)
pounds_grams = float(pounds * 32)
lots_grams = float(talents * 13.3)

total = talent_grams + pounds_grams + lots_grams
total_kilo = total/1000
total_grams = total % 1000

print("The weight in modern units:")

print(f"{total_kilo} + kilograms and {total_grams} grams.")
"""
print(f"{random.randint(0, 999):03d}")
print(str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)))
"""