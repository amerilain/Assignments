# Write a program that asks the user how much money they have and lets them know if they have enough
# for a latte that costs 5 euros.
# If they don't have enough, there is no output.

money = float(input("Enter amount of money: "))
if money >= 5:
    print("You can buy latte.")