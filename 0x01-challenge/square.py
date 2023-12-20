#!/usr/bin/python3
"""Square class module below."""


class Square:
    """Created Square class."""
    def __init__(self, width=0, height=0):
        """
        Instantiates Square class
        
        Args:
        - width: Width of square
        - height: Height of square
        """
        self.width = width
        self.height = height

    def area_of_my_square(self):
        """
        Area of the square
        
        Returns:
        Area of the square class.
        """
        return (self.width * self.height)

    def permiter_of_my_square(self):
        """
        Perimeter of the square.
        
        Returns:
        perimeter of square class.
        """
        return ((self.width * 2) + (self.height * 2))

    def __str__(self):
        """
        String representation of class.
        
        Returns:
        String representation of the square class
        in the below format.
        """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
