from ingredient import Ingredient


class Additive(Ingredient):
    def __init__(self, name, price, origin, allergen=''):
        super().__init__(name, price)
        self._allergen = allergen
        self._origin = origin

    @property
    def allergen(self):
        return self._allergen

    @allergen.setter
    def allergen(self, allergen: str):
        self._allergen = allergen

    @property
    def origin(self):
        return self._origin

    @origin.setter
    def origin(self, origin: str):
        self._origin = origin

    def __str__(self):
        return f"Additive(name='{self.name}', price={self.price}, allergen='{self.allergen}', origin='{self.origin}')"
