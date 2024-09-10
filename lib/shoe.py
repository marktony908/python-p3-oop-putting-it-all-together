import sys

class Shoe:
    def __init__(self, brand, size, color="Unknown"):
        self.brand = brand
        self.size = size
        self.color = color
        self.condition = "New"

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        if not isinstance(value, str) or not value:
            raise ValueError("Brand must be a non-empty string.")
        self._brand = value

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            print("size must be an integer")
        else:
            self._size = value

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, value):
        if not isinstance(value, str) or not value:
            raise ValueError("Color must be a non-empty string.")
        self._color = value

    def cobble(self):
        self.condition = "New"
        print("Your shoe is as good as new!")

    def __str__(self):
        return f"{self.brand} shoe, size {self.size}, color {self.color}, condition {self.condition}"
