import math


class GeometricObject:
    """
    The GeometricObject class represents a geometric object with various attributes including coordinates, color, and fill status.
    """
    def __init__(
            self,
            x: float = 0.0,
            y: float = 0.0,
            color: str = None,
            filled: bool = False
    ):
        """
        Initializes a GeometricObject object.

        :param x: The x-coordinate of the object.
        :param y: The y-coordinate of the object.
        :param color: The color of the object.
        :param filled: The fill status of the object.

        :return: None
        """
        self.__x = x
        self.__y = y
        self.color = color
        self.filled = filled

    def set_coordinate(self, x: float, y: float):
        """
        Sets the coordinates of the object.

        :param x: The x-coordinate to set.
        :param y: The y-coordinate to set.

        :return: None
        """
        self.__x = x
        self.__y = y

    def set_color(self, color: str):
        """
        Sets the color of the object.

        :param color: The color to set.

        :return: None
        """
        self.color = color

    def set_filled(self, filled: bool):
        """
        Sets the fill status of the object.

        :param filled: The fill status to set.

        :return: None
        """
        self.filled = filled

    def get_x(self) -> float:
        """
        Gets the x-coordinate of the object.

        :return: The x-coordinate of the object.
        """
        return self.__x

    def get_y(self) -> float:
        """
        Gets the y-coordinate of the object.

        :return: The y-coordinate of the object.
        """
        return self.__y

    def get_color(self) -> str:
        """
        Gets the color of the object.

        :return: The color of the object.
        """
        return self.color

    def is_filled(self) -> bool:
        """
        Checks if the object is filled.

        :return: True if the object is filled, False otherwise.
        """
        return self.filled

    def __repr__(self) -> str:
        """
        Returns a string representation of the object.

        :return: A string representing the object.
        """
        res = ''
        res += f'({self.get_x()}, {self.get_y()}) {self.color} '
        if self.filled:
            res += 'filled'
        else:
            res += 'no filled'
        return res

    def __str__(self) -> str:
        """
        Returns a string representation of the object.

        :return: A string representing the object.
        """
        res = (f'({self.__x}, {self.__y})\n'
               f'color: {self.color}\n'
               f'filled: {self.filled}')
        return res


class Circle(GeometricObject):
    """
    The Circle class represents a circle with various attributes including radius.
    """
    def __init__(
            self,
            x: float = 0.0,
            y: float = 0.0,
            radius: float = 0.0,
            color: str = None,
            filled: bool = False
    ):
        """
        Initializes a Circle object.

        :param x: The x-coordinate of the center of the circle.
        :param y: The y-coordinate of the center of the circle.
        :param radius: The radius of the circle.
        :param color: The color of the circle.
        :param filled: The fill status of the circle.

        :return: None
        """
        super().__init__(x, y, color, filled)
        self.__radius = radius

    @property
    def radius(self) -> float:
        """
        Gets the radius of the circle.

        :return: The radius of the circle.
        """
        return self.__radius

    @radius.setter
    def radius(self, radius):
        """
        Sets the radius of the circle.

        :param radius: The radius to set.
        """
        self.__radius = radius

    def get_area(self) -> float:
        """
        Calculates the area of the circle.

        :return: The area of the circle.
        """
        return math.pi * (self.__radius ** 2)

    def get_perimetr(self) -> float:
        """
        Calculates the perimeter of the circle.

        :return: The perimeter of the circle.
        """
        return 2 * math.pi * self.__radius

    def get_diametr(self) -> float:
        """
        Calculates the diameter of the circle.

        :return: The diameter of the circle.
        """
        return self.__radius * 2

    def __repr__(self):
        """
        Returns a string representation of the circle.

        :return: A string representing the circle.
        """
        res = ''
        res += f'radius: {self.__radius} ({self.get_x()}, {self.get_y()}) {self.color} '
        if self.filled:
            res += 'filled'
        else:
            res += 'no filled'
        return res

    def __str__(self):
        """
        Returns a string representation of the circle.

        :return: A string representing the circle.
        """
        res = (f'radius: {self.__radius}\n'
               f'({self.get_x()}, {self.get_y()})\n'
               f'color: {self.color}\n'
               f'filled: {self.filled}')
        return res


class Rectangle(GeometricObject):
    """
    The Rectangle class represents a rectangle with various attributes including width and height.
    """
    def __init__(
            self,
            x: float = 0.0,
            y: float = 0.0,
            width: float = 0.0,
            height: float = 0.0,
            color: str = None,
            filled: bool = False
    ):
        """
        Initializes a Rectangle object.

        :param x: The x-coordinate of the top-left corner of the rectangle.
        :param y: The y-coordinate of the top-left corner of the rectangle.
        :param width: The width of the rectangle.
        :param height: The height of the rectangle.
        :param color: The color of the rectangle.
        :param filled: The fill status of the rectangle.

        :return: None
        """
        super().__init__(x, y, color, filled)
        self.width = width
        self.height = height

    def set_width(self, width: float):
        """
        Calculates the area of the rectangle.

        :return: The area of the rectangle.
        """
        self.width = width

    def set_height(self, height: float):
        """
        Sets the height of the rectangle.

        :param height: The height to set.
        :return: None
        """
        self.height = height

    def get_width(self) -> float:
        """
        Gets the width of the rectangle.

        :return: The width of the rectangle.
        """
        return self.width

    def get_height(self) -> float:
        """
        Gets the height of the rectangle.

        :return: The height of the rectangle.
        """
        return self.height

    def get_area(self) -> float:
        """
        Calculates the area of the rectangle.

        :return: The area of the rectangle.
        """
        return self.height * self.height

    def get_perimetr(self) -> float:
        """
        Calculates the perimeter of the rectangle.

        :return: The perimeter of the rectangle.
        """
        return self.height * 2 + self.width * 2

    def __str__(self):
        """
        Returns a string representation of the rectangle.

        :return: A string representing the rectangle.
        """
        res = (f'width: {self.width}\n'
               f'height: {self.height}\n'
               f'({self.get_x()}, {self.get_y()})\n'
               f'color: {self.color}\n'
               f'filled: {self.filled}')
        return res

    def __repr__(self):
        """
        Returns a string representation of the rectangle.

        :return: A string representing the rectangle.
        """
        res = ''
        res += f'width: {self.width} height: {self.height} ({self.get_x()}, {self.get_y()}) {self.color} '
        if self.filled:
            res += 'filled'
        else:
            res += 'no filled'
        return res
