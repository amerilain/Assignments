import random
import math

# part 1
dice = 0


def roll_dice():
    return random.randint(1,6)


while dice != 6:
    dice = roll_dice()
    print(f"dice number is {dice}")


# part 2
dice = 0
dice_sides = int(input("enter the number of sides: "))


def roll_dice(sides):
    return random.randint(1, sides)


while dice != dice_sides:
    dice = roll_dice(dice_sides)
    print(f"dice number is: {dice}")


# part 3
gallon_amount = int(input("Enter an amount of gallons to convert to liters (negative value to quit): "))


def gallon_to_liter(gallons):
    return gallons * 3.785412


while gallon_amount > 0:
    print(f"That is {gallon_to_liter(gallon_amount):.0f} liters")
    gallon_amount = int(input("enter an amount of gallons (negative value to quit): "))



# part 4
def sum_of_integers(numbers):
    i = 0
    for number in numbers:
        i = i + number
    return i


integers = [1, 2, 3, 4, 5]
print(sum_of_integers(integers))


# part 5
def positive_ints(numbers):
    even_nums = []
    for i in numbers:
        if i % 2 == 0:
            even_nums.append(i)
    return even_nums


integers = [1, 2, 3, 4, 5]
print(integers)
print(positive_ints(integers))


# part 6
def pizza_calculator(diameter, euros):

    area = math.pi * (diameter/2)**2
    sq_meters = area/100
    return float(euros/sq_meters)


diameter1 = float(input("enter the diameter of the first pizza in cm: "))
price1 = float(input("enter the price of the first pizza in euros: "))
diameter2 = float(input("enter the diameter of the second pizza in cm: "))
price2 = float((input("enter the price of the second pizza in euros: ")))

unit_price1 = pizza_calculator(diameter1, price1)
unit_price2 = pizza_calculator(diameter2, price2)

if unit_price1 < unit_price2:
    print(f"pizza one is a better value")
if unit_price1 > unit_price2:
    print(f"pizza two is a better value")
if unit_price1 == unit_price2:
    print("Both pizzas are of the same value")