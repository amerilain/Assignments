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
import random

# part 4
"""Now we will program a car race. The travelled distance of a new car is initialized as zero. At the beginning of 
the main program, create a list that consists of 10 car objects created using a loop. The maximum speed of each new 
car is a random value between 100 km/h and 200 km/h. The registration numbers are created as follows: "ABC-1", 
"ABC-2" and so on. Now the race begins. One per every hour of the race, the following operations are performed: 

The speed of each car is changed so that the change in speed is a random value between -10 km/h and +15 km/h. This is 
done using the accelerate method. Each car is made to drive for one hour. This is done with the drive method. """


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