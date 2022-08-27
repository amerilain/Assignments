import math
import random

# part 1
name = input("What is Your name? ")
print("hello, " + name + "!")

# part 2
radius = float(input("What is the radius of the circle? "))
print(f"The area of the circle is {math.pi * (radius ** 2):.2f}")

# part 3
length = float(input("What is the length? "))
width = float(input("What is the width? "))
print(f"The perimeter of the rectangle is {(length * 2) + (width * 2):.2f}")
print(f"The area of the rectangle is {length * width:.2f}")

# part 4
num1 = float(input("enter a number: "))
num2 = float(input("enter a number: "))
num3 = float(input("enter a number: "))

print(f"The sum of your numbers is {num1 + num2 + num3:.0f}")
print(f"The product of your numbers is {num1 * num2 * num3:.0f}")
print(f"The average of your numbers is {(num1 + num2 + num3)/3:.2f}")

# part 5
talents = float(input("Enter talents:\n"))
pounds = float(input("\nEnter pounds:\n"))
lots = float(input("\nEnter lots:\n"))

talent_grams = float(talents * 20 * 32 * 13.3)
pounds_grams = float(pounds * 32 * 13.3)
lots_grams = float(lots * 13.3)

total = talent_grams + pounds_grams + lots_grams
total_kilo = total/1000
total_grams = total % 1000

print("\n" + "The weight in modern units:")
print(f"{math.floor(total_kilo)} kilograms and {total_grams:.2f} grams.")

# part 6
print(f"{random.randint(0, 999):03d}")
print(str(random.randint(1, 6)) + str(random.randint(1, 6)) + str(random.randint(1, 6)) + str(random.randint(1, 6)))
