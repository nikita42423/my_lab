from .figure import Figure
from .color import FigureColor

class Rectangle(Figure):
    """
    Класс Прямоугольник
    """

    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = FigureColor()
        self.color.color = color
        self._name = "Прямоугольник"

    def area(self):
        """Вычисление площади прямоугольника"""
        return self.width * self.height

    @property
    def name(self):
        return self._name

    def __repr__(self):
        return "{} {} цвета шириной {} и высотой {}. Площадь: {:.2f}".format(
            self.name,
            self.color.color,
            self.width,
            self.height,
            self.area()
        )
