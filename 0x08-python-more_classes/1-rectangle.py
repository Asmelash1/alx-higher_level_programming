#!/usr/bin/python3

"""Module of define a empty class Rectangle"""





class Rectangle:

    """Class Rectangle"""



    def __init__(self, width=0, height=0):

        """Function to validade of the width and height of rectangle"""

        self.width = width

        self.height = height



    @property

    def width(self):

        """Function that validade fo the width"""

        return self.__width



    @width.setter

    def width(self, value):

        """Function that validade fo the width"""

        if type(value) is not int:

            raise TypeError("width must be an integer")

        if value < 0:

            raise ValueError("width must be >= 0")

        self.__width = value



    @property

    def height(self):

        """Function that validade fo the height"""

        return self.__height



    @height.setter

    def height(self, value):

        """Function that validade fo the height"""

        if type(value) is not int:

            raise TypeError("height must be an integer")

        if value < 0:

            raise ValueError("height must be >= 0")

        self.__height = value
