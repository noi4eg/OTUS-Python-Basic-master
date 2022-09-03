"""
создайте класс `Plane`, наследник `Vehicle`
"""

from homework_02.base import Vehicle
from homework_02.exceptions import CargoOverload


class Plane(Vehicle):
    # cargo = 0
    # max_cargo = 0

    def __init__(self, weight, fuel, fuel_consumtion, max_cargo):
        super().__init__(weight, fuel, fuel_consumtion)
        self.cargo = 0
        self.max_cargo = max_cargo

    def load_cargo(self, new_cargo):
        if self.cargo + new_cargo <= self.max_cargo:
            self.cargo += new_cargo
        else:
            raise CargoOverload

    def remove_all_cargo(self):
        removed_cargo = self.cargo
        self.cargo = 0
        return removed_cargo
