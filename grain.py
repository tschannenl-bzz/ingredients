from ingredient import Ingredient


class Grain(Ingredient):
    def __init__(self):
        self._allergen = ''
        super().__init__(self.name, self.price)

    @property
    def allergen(self):
        return self._allergen

    @allergen.setter
    def allergen(self, allergen=str):
        self._allergen = allergen

    def __str__(self):
        return f"Grain(name='{self.name}', price={self.price}, allergen='{self.allergen}')"
