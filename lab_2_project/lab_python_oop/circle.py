import math
from .figure import Figure
from .color import FigureColor

class Circle(Figure):
    """
    Класс Круг
    """

    def __init__(self, radius, color):
        self.radius = radius
        self.color = FigureColor()
        self.color.color = color
        self._name = "Круг"

    def area(self):
        """Вычисление площади круга"""
        return math.pi * self.radius ** 2

    @property
    def name(self):
        return self._name

    def __repr__(self):
        return "{} {} цвета радиусом {}. Площадь: {:.2f}".format(
            self.name,
            self.color.color,
            self.radius,
            self.area()
        )
