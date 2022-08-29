

# part 1
sizeOfFish = int(input("How big is your fish?\n"))
sizeLimit = 42

if sizeOfFish < 42:
    print("Throw it back!")
    print(f"Your fish is {sizeLimit - sizeOfFish}")
else:
    print("You can keep your fish!")


# Part 2
cabin_class = input("What is your cabin class?\n")
if cabin_class == "LUX":
    print("upper-deck cabin with a balcony")
elif cabin_class == "A":
    print("above the car deck, equipped with a window")
elif cabin_class == "B" or "C":
    print("windowless cabin above the car deck")
else:
    print("Start swimming!")


# Part 3
'''
Write a program that asks for the biological gender and hemoglobin value (g/l). 
The program the notifies the user if the hemoglobin value is low, normal or high.
A normal hemoglobin value for adult females is between 117-155 g/l.
A normal hemoglobin value for adult males is between 134-167 g/l.
'''
gender = input("What is your gender (male or female)?\n")
hemoglobin = int(input("What is your hemoglobin value?\n"))

if gender == "male":
    if hemoglobin < 134:
        print("your hemoglobin is low.")
    elif 134 <= hemoglobin <= 167:
        print("your hemoglobin is normal.")
    else:
        print("your hemoglobin is high.")
if gender == "female":
    if hemoglobin < 117:
        print("your hemoglobin is low.")
    elif 117 <= hemoglobin <= 155:
        print("your hemoglobin is normal.")
    else:
        print("your hemoglobin is high.")



# part 4
year = int(input("Give a year:\n"))

if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
    print("The year is a leap year.")
else:
    print("The year is not a leap year.")