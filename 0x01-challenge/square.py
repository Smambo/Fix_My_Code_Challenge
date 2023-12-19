#!/usr/bin/python3
"""Square class module below."""


class Square():
    """Created Square class."""
    def __init__(self, width=0, height=0, **kwargs):
        """Instantiates Square class"""
        self.width = width
        self.height = height
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return (self.width * self.height)

    def perimeter_of_my_square(self):
        """Perimeter of the square."""
        return ((self.width * 2) + (self.height * 2))

    def __str__(self):
        """String representation of class."""
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """Creates object."""
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.perimeter_of_my_square())
