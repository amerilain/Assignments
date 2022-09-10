import random

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