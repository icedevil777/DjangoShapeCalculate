import math


class PlaneShapes:
    """Main parent class for plane figures"""
    titele = "Plane figures"

    def __init__(self):
        pass

    def area(self):
        """Area calculation method"""
        pass

    def perimetr(self):
        """Perimetr calculation method"""
        pass

    def diagonal(self):
        """Diagonal calculation method"""
        pass


class VolumetricShapes:
    """Main parent class for volumetric figures"""
    titele = "Volumetric figures"

    def __init__(self):
        pass

    def volume(self):
        """Volume calculation method"""

        pass

    def height(self):
        """Height calculation method"""
        pass


class Square(PlaneShapes):
    """Class describes square"""
    titele = "Square"

    def __init__(self, x):
        super().__init__()
        self.x = x

    def area(self):
        return self.x ** 2

    def perimetr(self):
        return self.x * 4

    def square_draw(self):
        pass

class Rectangle(PlaneShapes):
    """Class describes rectangle"""
    titele = "Rectangle"

    def __init__(self, x, y):
        super(PlaneShapes, self).__init__()
        self.x = x
        self.y = y

    def area(self):
        return self.x * self.y

    def perimetr(self):
        return (2 * self.x) + (2 * self.y)


class Circle(PlaneShapes):
    """Class describes circle"""
    titele = "Circle"

    def __init__(self, r):
        super().__init__()
        self.r = r

    def area(self):
        return (self.r ** 2) * math.pi

    def circumference(self):
        return self.r * 2 * math.pi

    def diametr(self):
        return self.r * 2


class Triangle(PlaneShapes):
    """Class describes triangle"""

    titele = "Equilateral_triangle"

    def __init__(self, x):
        super().__init__()
        self.x = x
        self.h = math.sqrt(self.x ** 2 - (self.x ** 2) / 4)

    def height(self):
        return self.h

    def area(self):
        return (self.x * self.h) / 2

    def median(self):
        return (math.sqrt(3) * self.x) / 2


class Rombus(PlaneShapes):
    """Class describes rombus"""
    titele = "Rombus"

    def __init__(self, a, b, c, d):
        super().__init__()
        self.a = a
        self.b = b
        self.c = c
        self.d = d

        self.diag1 = math.sqrt(a ** 2 + b ** 2)
        self.diag2 = math.sqrt(c ** 2 + d ** 2)

    def area(self):
        return (self.diag1 * self.diag2) / 2

    def perimetr(self):
        return self.a + self.b + self.c + self.d

    def diags(self):
        return self.diag1, self.diag2


class Trapezoid(PlaneShapes):
    """Class describes trapezoid"""
    titele = "Trapezoid"

    def __init__(self, a, b, c):  #
        super().__init__()
        self.a = a  # Нижнее основание
        self.b = b  # Верхнее основание
        self.c = c  # Стороны
        try:
            self.h = math.sqrt(self.c ** 2 - ((self.a - self.b) ** 2) / 4)
        except ZeroDivisionError:
            "Err"

    def area(self):
        return ((self.a + self.b) * self.h) / 2


class Сube(VolumetricShapes):
    """Class describes cube"""
    titele = "Сube"

    def __init__(self, x):
        super().__init__()
        self.x = x

    def volume(self):
        return self.x ** 3

    def area(self):
        return self.x ** 2 * 6


class Parallelepiped(VolumetricShapes):
    """Class describes parallelepiped"""
    titele = "Parallelepiped"

    def __init__(self, a, b, c):
        super().__init__()
        self.a = a
        self.b = b
        self.c = c

    def volume(self):
        return self.a * self.b * self.c

    def area(self):
        return (self.a * self.b + self.a * self.c + self.c * self.b) * 2


class Sphere(VolumetricShapes):
    """Class describes sphere"""
    titele = "Sphere"

    def __init__(self, r):
        super(VolumetricShapes, self).__init__()
        self.r = r

    def volume(self):
        return 4 * math.pi * self.r ** 3 / 3

    def area(self):
        return 4 * self.r * math.pi


class Pyramid(VolumetricShapes):
    """Class describes pyramid"""
    titele = "Pyramid_Tetrahedron"

    def __init__(self, x):
        super(VolumetricShapes, self).__init__()
        self.x = x

    def height(self):
        return math.sqrt(2 * self.x / 3)

    def volume(self):
        return math.sqrt(2) * self.x ** 3 / 12

    def area(self):
        return math.sqrt(3) * self.x ** 2


class Сylinder(VolumetricShapes):
    """Class describes сylinder"""
    titele = "Сylinder"

    def __init__(self, r, h):
        super().__init__()
        self.r = r
        self.h = h

    def volume(self):
        return self.h * math.pi * self.r ** 2

    def area(self):
        return 2 * math.pi * self.r * self.h + 2 * math.pi * self.r ** 2


class Сone(VolumetricShapes):
    """Class describes Сone"""
    titele = "Сone"

    def __init__(self, l, r):
        super().__init__()
        self.r = r  # Радиус
        self.l = l  # Образующая
        self.h = math.sqrt(l ** 2 - r ** 2)
        self.s = math.pi * self.r * (self.r + self.l)

    def volume(self):
        return (self.s * self.h) / 3

    def area(self):
        return self.s
