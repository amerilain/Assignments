import random

# part 1
n = 1
while n <= 1000:
    if n % 3 == 0:
        print(n)
        n += 1
    else:
        n += 1

# part 2
while True:
    value = int(input("Give a length in cm: "))
    if value < 0:
        break
    else:
        print(f"The length in inches is {value * 2.54}.")

# part 3
count = 0
smallest = 0
largest = 0

while True:
    num = input("Enter a number (return to quit): ")
    if num == "":
        break
    while num != "":
        num = int(num)

        if num > largest:
            largest = num
            if count == 0:
                smallest = num
                count += 1
                break
            break

        if num < smallest:
            smallest = num
            count += 1
            break
        else:
            break

print(f"{largest} is the largest number")
print(f"{smallest} is the smallest number")

# part 4
# computer draws an integer between one and ten and assigns it to a variable
random_num = random.randint(1, 10)
# while loop
while True:
    # ask number from the user
    guess = int(input("Guess a number between one and ten: "))
    # if ==, print and break
    if guess == random_num:
        print("Correct!")
        break
    # if higher, print "too high"
    elif guess >= random_num:
        print("Too high!")
    # if lower, print too low
    elif guess <= random_num:
        print("Too low!")

# Create and assign necessary variables (count, username and password)
count = 0
username = "python"
password = "rules"
access_denied = True

# While loop (while count is less than 5)
while count < 5:
    # ask for username and password
    login_name = input("username: ")
    login_password = input("password: ")
    # if correct, print welcome, count++ and break
    if username == login_name and password == login_password:
        count += 1
        print("welcome")
        access_denied = False
        break
        # if wrong, count++
    if username != login_name or password != login_password:
        count += 1
# print Access denied
if access_denied:
    print("access denied")


# part 6
# define variables
inside_circle = 0
count = 0

# ask user to input number of points
N = int(input("Enter number of points: "))

# start while loop (True?)
while count < N:
    # randomly generate points on y and x axis
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    # if inside increase counts by one
    if x**2 + y**2 < 1:
        inside_circle += 1
        count += 1
    # else only increase the count
    else:
        count += 1


# calculate pi
pi = float(4 * inside_circle / N)
# print pi
print(f"pi = {pi: 0.20f}")



"""


