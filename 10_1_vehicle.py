from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def drive(self, drive):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        needed_fuel = (self.fuel_consumption + 0.9) * distance
        if needed_fuel <= self.fuel_quantity:
            self.fuel_quantity -= needed_fuel
            return self.fuel_quantity

    def refuel(self, fuel):
        self.fuel_quantity += fuel
        return self.fuel_quantity


class Truck(Vehicle):

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        needed_fuel = (self.fuel_consumption + 1.6) * distance
        if needed_fuel <= self.fuel_quantity:
            self.fuel_quantity -= needed_fuel
            return self.fuel_quantity

    def refuel(self, fuel):
        self.fuel_quantity += 0.95 * fuel
        return self.fuel_quantity


car = Car(20, 2)
car.drive(5)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)

truck = Truck(100, 10)
truck.drive(7)
print(truck.fuel_quantity)
truck.refuel(20)
print(truck.fuel_quantity)
