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
            for i in range(floor-self.current):
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


class Building:
    def __init__(self, bottom, top, elevator_list):
        self.elevator_list = []
        for i in range(elevator_list):
            self.elevator_list.append(Elevator(bottom, top))

    def run_elevator(self, elevator_num, floor):
        print(f"The elevator number {elevator_num} is running")
        self.elevator_list[elevator_num - 1].go_to(floor)

    def fire_alarm(self):
        print("---------------")
        print("Fire!")
        for i in self.elevator_list:
            i.go_to(i.bottom)


print("Elevators in the building:")
building = Building(1, 7, 3)
building.run_elevator(1, 10)
building.run_elevator(2, 4)
building.run_elevator(3, 4)
building.fire_alarm()