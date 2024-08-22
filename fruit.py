from ingredient import Ingredient


class Fruit(Ingredient):
    def __init__(self, origin):
        self._origin = origin
        super().__init__(self.name, self.price)

    @property
    def origin(self):
        return self._origin

    @origin.setter
    def origin(self, origin: str):
        self._origin = origin

    @property
    def __str__(self):
        return f"Fruit(name='{self.name}', price={self.price}, origin='{self.origin}')"
