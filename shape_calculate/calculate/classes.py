import math as m
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import patches

matplotlib.use('TkAgg')


class Figures:
    """Main parent class"""
    titele = "Figures"

    def __init__(self, x=None, y=None, z=None):
        """The sides of the figures are passed to the class constructor"""
        self.x = x
        self.y = y
        self.z = z

    def get_area(self) -> int:
        """Area calculation method"""
        pass

    def get_perimetr(self) -> int:
        """Perimetr calculation method"""
        pass

    def get_volume(self) -> int:
        """Volume calculation method"""
        pass


class Square(Figures):
    """
    Class describes square
    x - side;
    """
    titele = "Square"

    def get_area(self) -> int:
        return self.x ** 2

    def get_perimetr(self) -> int:
        return self.x * 4

    def draw(self):
        fig, ax = plt.subplots(figsize=(8, 8))
        ax.add_patch(patches.Rectangle((0, 0), self.x, self.x, edgecolor='black', facecolor='black', fill=True))
        plt.xlim([-(self.x * 0.3), self.x + self.x * 0.3])
        plt.ylim([-(self.x * 0.3), self.x + self.x * 0.3])
        plt.grid(linestyle='--')
        fig.savefig('static/calculate/img/square.png')


class Rectangle(Figures):
    """
    Class describes rectangle
    x and y - sides;
    """
    titele = "Rectangle"

    def get_area(self) -> int:
        return self.x * self.y

    def get_perimetr(self) -> int:
        return (2 * self.x) + (2 * self.y)

    def draw(self):
        fig, ax = plt.subplots(figsize=(8, 8))
        ax.add_patch(patches.Rectangle((0, 0), self.x, self.y, edgecolor='black', facecolor='black', fill=True))
        if self.x > self.y:
            plt.xlim([-(self.x * 0.3), self.x + self.x * 0.3])
            plt.ylim([-(self.x * 0.3), self.x + self.x * 0.3])
        else:
            plt.xlim([-(self.y * 0.3), self.y + self.y * 0.3])
            plt.ylim([-(self.y * 0.3), self.y + self.y * 0.3])
        plt.grid(linestyle='--')
        fig.savefig('static/calculate/img/rectangle.png')


class Circle(Figures):
    """
    Class describes circle, where x - radius
    x - radius;
    """
    titele = "Circle"

    def get_area(self) -> float:
        return (self.x ** 2) * m.pi

    def get_circumference(self) -> float:
        return self.x * 2 * m.pi

    def get_diametr(self) -> float:
        return self.x * 2

    def draw(self):
        fig, ax = plt.subplots(figsize=(8, 8))
        ax.add_patch(patches.Rectangle((0, 0), self.x, self.x, edgecolor='black', facecolor='black', fill=True))
        plt.xlim([-(self.x * 0.3), self.x + self.x * 0.3])
        plt.ylim([-(self.x * 0.3), self.x + self.x * 0.3])
        plt.grid(linestyle='--')
        fig.savefig('static/calculate/img/square.png')

class Triangle(Figures):
    """
    Class describes equilateral triangle
    x - side;
    """

    titele = "EquilateralTriangle"

    def get_median(self) -> float:
        return round((m.sqrt(3) * self.x / 2), 3)

    def get_perimetr(self) -> int:
        return 3 * self.x

    def get_area(self) -> float:
        return round((m.sqrt(3) * self.x ** 2 / 4), 3)

    def draw(self):
        fig, ax = plt.subplots(figsize=(8, 8))
        # ax.set_aspect('equal')
        x = [0, self.x, self.x / 2, 0]
        y = [0, 0, self.x * 0.866, 0]
        plt.plot(x, y)
        plt.xlim([-(self.x * 0.3), self.x + self.x * 0.3])
        plt.ylim([-(self.x * 0.3), self.x + self.x * 0.3])
        plt.grid(linestyle='--')
        fig.savefig('static/calculate/img/triangle.png')


class Rombus(Figures):
    """
    Class describes rombus
    x - side; y - height;
    """
    titele = "Rombus"

    def get_area(self) -> int:
        return self.x * self.y

    def get_perimetr(self) -> int:
        return 4 * self.x

    def draw(self):
        fig, ax = plt.subplots(figsize=(8, 8))
        x = [0, self.x, self.x + m.sqrt(self.x ** 2 - self.y ** 2),
             m.sqrt(self.x ** 2 - self.y ** 2), 0]
        y = [0, 0, self.y, self.y, 0]
        plt.plot(x, y)
        plt.xlim([-(self.x * 0.1), self.x + m.sqrt(self.x ** 2 - self.y ** 2) +
                  (self.x + m.sqrt(self.x ** 2 - self.y ** 2)) * 0.1])

        plt.ylim([-(self.x * 0.1), self.x + m.sqrt(self.x ** 2 - self.y ** 2) +
                  (self.x + m.sqrt(self.x ** 2 - self.y ** 2)) * 0.1])
        plt.grid(linestyle='--')
        fig.savefig('static/calculate/img/rombus.png')


class Trapezoid(Rombus):
    """
    Class describes trapezoid
    x,y,z - top, bot and height respectively;
    """
    titele = "Trapezoid"

    def get_area(self) -> float:
        return self.z * (self.x + self.y) / 2

    def get_diagonal(self) -> float:
        return round(m.sqrt(self.z**2 + (self.y - (self.y - self.x)/2)**2), 2)

    def draw(self):
        fig, ax = plt.subplots(figsize=(8, 8))
        x = [0, self.y, self.y - (self.y - self.x) / 2, (self.y - self.x) / 2, 0]
        y = [0, 0, self.z, self.z, 0]
        plt.plot(x, y)
        if self.z > self.y and self.z > self.x:
            plt.xlim([-(self.z * 0.1), self.z + self.z * 0.1])
            plt.ylim([-(self.z * 0.1), self.z + self.z * 0.1])
        elif self.y > self.z and self.y > self.x:
            plt.xlim([-(self.y * 0.1), self.y + self.y * 0.1])
            plt.ylim([-(self.y * 0.1), self.y + self.y * 0.1])
        else:
            plt.xlim([-(self.x + self.x * 0.1), self.x + self.x * 0.1])
            plt.ylim([-(self.x + self.x * 0.1), self.x + self.x * 0.1])
        plt.grid(linestyle='--')
        fig.savefig('static/calculate/img/trapezoid.png')


class Сube(Figures):
    """
    Class describes cube
    x - side;
    """
    titele = "Сube"

    def get_volume(self):
        return self.x ** 3

    def get_area(self):
        return self.x ** 2 * 6


class Parallelepiped(Figures):
    """
    Class describes parallelepiped
    x, y , z - sides;
    """
    titele = "Parallelepiped"

    def get_volume(self):
        return self.x * self.y * self.z

    def get_area(self):
        return (self.x * self.y + self.x * self.z + self.z * self.y) * 2


class Sphere(Figures):
    """
    Class describes sphere
    x - radius;
    """
    titele = "Sphere"

    def get_volume(self):
        return 4 * m.pi * self.x ** 3 / 3

    def get_area(self):
        return 4 * self.x * m.pi


class Pyramid(Figures):
    """
    Class describes pyramid
    x - side y - height;
    """
    titele = "Pyramid_Tetrahedron"

    def get_height(self):
        return m.sqrt(2 * self.x / 3)

    def get_volume(self):
        return m.sqrt(2) * self.x ** 3 / 12

    def get_area(self):
        return m.sqrt(3) * self.x ** 2


class Сylinder(Figures):
    """
    Class describes сylinder
    x - radius, y - height
    """
    titele = "Сylinder"

    def get_volume(self):
        return self.x * m.pi * self.y ** 2

    def get_area(self):
        return 2 * m.pi * self.x * self.y + 2 * m.pi * self.x ** 2


class Сone(Figures):
    """
    Class describes Сone
    x - radius, y - height
    """
    titele = "Сone"

    def __init__(self, x, y):
        super(Figures, self).__init__()
        self.x = x
        self.y = y
        self.s = m.pi * self.x ** 2

    def get_volume(self):
        return (self.s * self.y) / 3

    def get_area(self):
        return self.s
