import math


class GeometricObject:
    def __init__(
            self,
            x: float = 0.0,
            y: float = 0.0,
            color: str = None,
            filled: bool = False
    ):
        self.__x = x
        self.__y = y
        self.color = color
        self.filled = filled

    def set_coordinate(self, x: float, y: float):
        self.__x = x
        self.__y = y

    def set_color(self, color: str):
        self.color = color

    def set_filled(self, filled: bool):
        self.filled = filled

    def get_x(self) -> float:
        return self.__x

    def get_y(self) -> float:
        return self.__y

    def get_color(self) -> str:
        return self.color

    def is_filled(self) -> bool:
        return self.filled

    def __repr__(self):
        res = ''
        res += f'({self.get_x()}, {self.get_y()}) {self.color} '
        if self.filled:
            res += 'filled'
        else:
            res += 'no filled'
        return res

    def __str__(self):
        res = (f'({self.__x}, {self.__y})\n'
               f'color: {self.color}\n'
               f'filled: {self.filled}')
        return res


class Circle(GeometricObject):
    def __init__(
            self,
            x: float = 0.0,
            y: float = 0.0,
            radius: float = 0.0,
            color: str = None,
            filled: bool = False
    ):
        super().__init__(x, y, color, filled)
        self.__radius = radius

    @property
    def radius(self) -> float:
        return self.__radius

    @radius.setter
    def radius(self, radius):
        self.__radius = radius

    def get_area(self) -> float:
        return math.pi * (self.__radius ** 2)

    def get_perimetr(self) -> float:
        return 2 * math.pi * self.__radius

    def get_diametr(self) -> float:
        return self.__radius * 2

    def __repr__(self):
        res = ''
        res += f'radius: {self.__radius} ({self.get_x()}, {self.get_y()}) {self.color} '
        if self.filled:
            res += 'filled'
        else:
            res += 'no filled'
        return res

    def __str__(self):
        res = (f'radius: {self.__radius}\n'
               f'({self.get_x()}, {self.get_y()})\n'
               f'color: {self.color}\n'
               f'filled: {self.filled}')
        return res


class Rectangle(GeometricObject):
    def __init__(
            self,
            x: float = 0.0,
            y: float = 0.0,
            width: float = 0.0,
            height: float = 0.0,
            color: str = None,
            filled: bool = False
    ):
        super().__init__(x, y, color, filled)
        self.width = width
        self.height = height

    def set_width(self, width: float):
        self.width = width

    def set_height(self, height: float):
        self.height = height

    def get_width(self) -> float:
        return self.width

    def get_height(self) -> float:
        return self.height

    def get_area(self) -> float:
        return self.height * self.height

    def get_perimetr(self) -> float:
        return self.height * 2 + self.width * 2

    def __str__(self):
        res = (f'width: {self.width}\n'
               f'height: {self.height}\n'
               f'({self.get_x()}, {self.get_y()})\n'
               f'color: {self.color}\n'
               f'filled: {self.filled}')
        return res

    def __repr__(self):
        res = ''
        res += f'width: {self.width} height: {self.height} ({self.get_x()}, {self.get_y()}) {self.color} '
        if self.filled:
            res += 'filled'
        else:
            res += 'no filled'
        return res
