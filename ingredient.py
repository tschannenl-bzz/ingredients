from abc import ABC, abstractmethod


class Ingredient(ABC):
    @abstractmethod
    def __init__(self, name, price):
        self._name = name
        self._price = price

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, name=str):
        self.name = name

    @property
    def price(self):
        return self.price
