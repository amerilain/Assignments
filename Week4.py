import random

# part 1
dice = int(input("How many dice to roll? "))
dice_num = 0
total = 0
for i in range(0, dice):
    dice_num = random.randint(1, 6)
    total = total + dice_num
print(f"The sum of the dice rolls is {total}.")


# part 2
# create necessary variables (list to store inputted numbers)
numbers = []
# Start while loop
while True:
    # ask user to enter a string
    num = input("enter a number (return to quit): ")
    # if empty; break
    if num == "":
        break
    # convert string to int and store number in list
    else:
        num = int(num)
        numbers.append(num)
# revers sort numbers
numbers.sort(reverse=True)
# print the 5 greatest numbers; looping through list with for loop
for i in numbers[0:5]:
    print(i)
    

# part 3
# ask user for an integer
n = int(input("enter a number to see if it's prime: "))
# since 1 is not prime we rule it out
if n > 1:
    # start for loop to check if any smaller numbers are evenly divisible. Starting at 2
    for i in range(2, n):
        if n % i == 0:
            # if a smaller number is evenly divisible, it is not prime
            print(f"{n} is not a prime number")
            break
    # if not divisible by smaller number it must be prime
    else:
        print(f"{n} is a prime number")
# if n is 1, print "not prime" 
else:
    print(f"{n} is not a prime number")


# part 4:
cities = []
for i in range(0, 5):
    city = input("Enter the name of a city: ")
    cities.append(city)
for i in range(0, len(cities)):
    print(cities[i])