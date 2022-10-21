
# part 1
month = int(input("Enter a number representing a month: "))
seasons = ("Winter", "Winter", "Spring", "Spring", "Spring", "Summer", "Summer", "Summer", "Fall", "Fall", "Fall",
           "Winter")
if 0 < month <= 12:
    print(f"The corresponding season is {seasons[month-1]}")
else:
    print("Invalid response")

# part 2
names = set()
name = input("Enter a name: ")
while name != "":
    if name in names:
        print("Existing Name")
    else:
        names.add(name)
        print("New Name")
    name = input("Enter a new name: ")
for i in names:
    print(i)

# part 3
# create dictionary to store codes
airports = {}
while True:
    # ask user to enter an airport, fetch information of an airport, or exit
    response = input("'ENTER' to enter a new airport; 'FETCH' to fetch airport data; 'QUIT' to quit: ")
    # if user chooses to enter airport, ask for code and name of the airport
    if response == "enter":
        code = input("What is the ICAO code: ")
        name = input("What is the name of the airport: ")
        airports[code] = name
    # if the user chooses to quit
    if response == "quit":
        break
    # if the user chooses to fetch airport information
    if response == "fetch":
        if airports:
            # the program asks for the ICAO code of the airport
            code = input("What is the ICAO code?: ")
            print({airports[code]})
            break
        else:
            print("no airports to fetch")






