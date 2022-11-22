from tabulate import tabulate
from ObjectOrientedProgramming import Car


# part 1
class Publication:
    def __init__(self, name):
        self.name = name

    def print_info(self):
        print(self.name, end=" ")


class Book(Publication):
    def __init__(self, name, author, page_count):
        super().__init__(name)
        self.author = author
        self.page_count = page_count

    def print_info(self):
        table = [['name', self.name], ['author', self.author], ['pages', self.page_count]]
        print(tabulate(table))


class Magazine(Publication):
    def __init__(self, name, editor):
        super().__init__(name)
        self.editor = editor

    def print_info(self):
        table = [['name', self.name], ['editor', self.editor]]
        print(tabulate(table))


pub1 = Magazine("Donald Duck", "Aki Hyyppä")
pub1.print_info()

pub2 = Book("Compartment No. 6", "Rosa Liksom", "192")
pub2.print_info()


# part 2
class ElectricCar(Car):
    def __int__(self, registration, max_speed, battery):
        super().__init__(registration, max_speed)
        self.battery = battery

    def print_travel(self):
        print(f"Electric Car travel distance is: {self.travelled_dist}")


class GasolineCar(Car):
    def __init__(self, registration, max_speed, tank):
        super().__init__(registration, max_speed)
        self.tank = tank

    def print_travel(self):
        print(f"Gas Car travel distance is: {self.travelled_dist}")


electric_car = ElectricCar("abc-15", 180, 52.5)
gas_car = GasolineCar("acb-123", 165, 32.3)
electric_car.accelerate(80)
electric_car.drive(3)
gas_car.accelerate(120)
gas_car.drive(3)
electric_car.print_travel()
gas_car.print_travel()