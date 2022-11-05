import random
from tabulate import tabulate
"""
# part 1
class Car:
    def __init__(self, registration, max_speed, current_speed=0, travelled_dist=0):
        self.registration = registration
        self.max_speed = max_speed
        self.current_speed = current_speed
        self.travelled_dist = travelled_dist


car1 = Car("ABC-123", 142)

print(f"registration: {car1.registration}\nmax speed: {car1.max_speed} km/h\ncurrent speed: {car1.current_speed} km"
      f"/h\ntravelled distance: {car1.travelled_dist} km")


# part 2
class Car:
    def __init__(self, registration, max_speed, current_speed=0, travelled_dist=0):
        self.registration = registration
        self.max_speed = max_speed
        self.current_speed = current_speed
        self.travelled_dist = travelled_dist

    def accelerate(self, speed_change):
        if self.max_speed >= self.current_speed + speed_change >= 0:
            self.current_speed = self.current_speed + speed_change
        elif self.current_speed + speed_change > self.max_speed:
            self.current_speed = self.max_speed
        elif self.current_speed + speed_change < 0:
            self.current_speed = 0
        return


car1 = Car("ABC-123", 142)
print(f"current speed: {car1.current_speed}")
car1.accelerate(30)
print(f"current speed: {car1.current_speed}")
car1.accelerate(70)
print(f"current speed: {car1.current_speed}")
car1.accelerate(50)
print(f"current speed: {car1.current_speed}")
car1.accelerate(-200)
print(f"Emergency Break!\ncurrent speed: {car1.current_speed}")


# part 3
class Car:
    def __init__(self, registration, max_speed, current_speed=0, travelled_dist=0):
        self.registration = registration
        self.max_speed = max_speed
        self.current_speed = current_speed
        self.travelled_dist = travelled_dist

    def accelerate(self, speed_change):
        if self.max_speed >= self.current_speed + speed_change >= 0:
            self.current_speed = self.current_speed + speed_change
        elif self.current_speed + speed_change > self.max_speed:
            self.current_speed = self.max_speed
        elif self.current_speed + speed_change < 0:
            self.current_speed = 0
        return

    def drive(self, hours):
        self.travelled_dist = self.travelled_dist + (self.current_speed * hours)

car1 = Car("ABC-123", 142, 60, 2000)
car1.drive(1.5)
print(f"travelled distance: {car1.travelled_dist}")
"""


# part 4
def find_max_distance(car_list):
    max_distance = 0
    for i in car_list:
        distance = car.travelled_dist
        if distance > max_distance:
            max_distance = distance
    return max_distance


class Car:
    def __init__(self, registration, max_speed, current_speed=0, travelled_dist=0):
        self.registration = registration
        self.max_speed = max_speed
        self.current_speed = current_speed
        self.travelled_dist = travelled_dist

    def accelerate(self, speed_change):
        if self.max_speed >= self.current_speed + speed_change >= 0:
            self.current_speed = self.current_speed + speed_change
        elif self.current_speed + speed_change > self.max_speed:
            self.current_speed = self.max_speed
        elif self.current_speed + speed_change < 0:
            self.current_speed = 0
        return

    def drive(self, hours):
        self.travelled_dist = self.travelled_dist + (self.current_speed * hours)


max_dist = 0
cars = []
for car in range(10):
    registration = "ABC-" + str(car+1)
    max_speed = random.randint(100, 200)
    new_car = Car(registration, max_speed)
    cars.append(new_car)

while max_dist < 10000:
    for car in cars:
        accelerate = random.randint(-10, 15)
        car.accelerate(accelerate)

    for car in cars:
        car.drive(1)

    max_dist = find_max_distance(cars)

table = []
for car in cars:
    table.append([car.registration, car.max_speed, car.current_speed, car.travelled_dist])
print("")
print(tabulate(table, headers=['registration', 'max speed', 'current speed', 'travelled distance'], tablefmt='orgtbl'))


class Race:
    def __init__(self, name, distance, car_list):
        self.name = name
        self.distance = distance
        self.car_list = car_list

    def hour_pass(self):
        for car in self.car_list:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)

    def print_status(self):
        print(self.name + ";")
        for car in self.car_list:
            print(f"{car.registration:6s}: {car.current_speed:3d}, {car.travelled_dist} km")

    def race_finished(self):
        for car in self.car_list:
            if car.travelled_dist >= self.distance:
                return True
        return False


cars_list = []
for i in range(1, 11):
    new_car = Car(("ABC-" + str(i+1)), random.randint(100, 200))
    cars_list.append(new_car)
race = Race("derby", 8000, cars_list)
n = 0
while not race.race_finished():
    race.hour_pass()
    n += 1
    if n%10 == 0:
        print(f"After {n} hours")
        race.print_status()
print(f"The final result after {n} hours is: ")
race.print_status()