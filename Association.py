from ObjectOrientedProgramming import Car
import random
from tabulate import tabulate


# part 1
class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current = bottom

    def floor_up(self):
        if self.current < self.top:
            print(f"The elevator moves from floor {self.current} to floor {self.current +1}")
            self.current += 1
            return True
        else:
            return False

    def floor_down(self):
        if self.current > self.bottom:
            print(f"The elevator moves down from floor {self.current} to floor {self.current -1}")
            self.current -= 1
            return True
        else:
            return False

    def go_to(self, floor):
        if floor > self.current:
            for i in range(floor - self.current):
                if not self.floor_up():
                    break
        elif floor < self.current:
            for i in range(self.current - floor):
                if not self.floor_down():
                    break

        else:
            print(f"you are already at {self.current}")


elevator1 = Elevator(1, 100)
elevator1.go_to(10)


# part 2
class Building:
    def __init__(self, bottom, top, elevator_list):
        self.elevator_list = []
        for i in range(elevator_list):
            self.elevator_list.append(Elevator(bottom, top))

    def run_elevator(self, elevator_num, floor):
        print(f"The elevator number {elevator_num} is running")
        self.elevator_list[elevator_num - 1].go_to(floor)

# part 3
    def fire_alarm(self):
        print("---------------")
        print("Fire!")
        for i in self.elevator_list:
            i.go_to(i.bottom)


building = Building(1, 7, 3)
print(f"Elevators in the building: {len(building.elevator_list)}")
building.run_elevator(1, 10)
building.run_elevator(2, 4)
building.run_elevator(3, 4)
building.fire_alarm()


# part 4
class Race:
    def __init__(self, registration, distance, car_list):
        self.name = registration
        self.distance = distance
        self.car_list = car_list

    def hour_pass(self):
        for car in self.car_list:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)

    def print_status(self):
        table = []
        print(self.name + ";")
        for car in self.car_list:
            table.append([car.registration, car.current_speed, car.travelled_dist])

        return print(tabulate(table, headers=['registration', 'current speed', 'travelled distance km'], tablefmt='orgtbl'))


        #for car in self.car_list:
        #    print(f"{car.registration:6s}: {car.current_speed:3d}, {car.travelled_dist} km")

    def race_finished(self):
        for car in self.car_list:
            if car.travelled_dist >= self.distance:
                return True
        return False


cars_list = []
for i in range(10):
    new_car = Car(("ABC-" + str(i+1)), random.randint(100, 200))
    cars_list.append(new_car)
race = Race("Grand demolition Derby", 8000, cars_list)
n = 0
while not race.race_finished():
    race.hour_pass()
    n += 1
    if n % 10 == 0:
        print(f"After {n} hours")
        race.print_status()
print(f"The final result after {n} hours is: ")
race.print_status()