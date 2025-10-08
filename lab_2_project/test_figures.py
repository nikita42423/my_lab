#!/usr/bin/env python3
"""
Модульные тесты для геометрических фигур
"""

import unittest
import math
from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square

class TestFigures(unittest.TestCase):
    """
    Тестовый класс для геометрических фигур
    """

    def setUp(self):
        """Настройка тестовых данных"""
        self.rectangle = Rectangle(5, 3, "синий")
        self.circle = Circle(4, "зеленый")
        self.square = Square(6, "красный")

    def test_rectangle_area(self):
        """Тест площади прямоугольника"""
        self.assertEqual(self.rectangle.area(), 15)

    def test_circle_area(self):
        """Тест площади круга"""
        expected_area = math.pi * 4 ** 2
        self.assertAlmostEqual(self.circle.area(), expected_area)

    def test_square_area(self):
        """Тест площади квадрата"""
        self.assertEqual(self.square.area(), 36)

    def test_figure_names(self):
        """Тест имен фигур"""
        self.assertEqual(self.rectangle.name, "Прямоугольник")
        self.assertEqual(self.circle.name, "Круг")
        self.assertEqual(self.square.name, "Квадрат")

    def test_colors(self):
        """Тест цветов фигур"""
        self.assertEqual(self.rectangle.color.color, "синий")
        self.assertEqual(self.circle.color.color, "зеленый")
        self.assertEqual(self.square.color.color, "красный")

    def test_repr_methods(self):
        """Тест строкового представления"""
        self.assertIn("Прямоугольник", str(self.rectangle))
        self.assertIn("Круг", str(self.circle))
        self.assertIn("Квадрат", str(self.square))
        self.assertIn("синий", str(self.rectangle))
        self.assertIn("зеленый", str(self.circle))
        self.assertIn("красный", str(self.square))

if __name__ == '__main__':
    unittest.main()
