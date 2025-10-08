#!/usr/bin/env python3
"""
Основной файл программы для тестирования классов геометрических фигур
"""

from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square

# Импортируем внешний пакет
from colorama import Fore, Back, Style, init

def main():
    """
    Основная функция программы
    """
    # Инициализация colorama
    init(autoreset=True)

    print(Fore.CYAN + "=== Тестирование геометрических фигур ===")

    # Параметр всех фигур в зависимости от номера варианта
    N = 17

    print(Fore.YELLOW + f"Номер варианта: {N}")

    # Создание объектов с использованием N
    # Прямоугольник синего цвета шириной N и высотой N
    rectangle = Rectangle(N, N, "синий")
    print(Fore.BLUE + str(rectangle))

    # Круг зеленого цвета радиусом N
    circle = Circle(N, "зеленый")
    print(Fore.GREEN + str(circle))

    # Квадрат красного цвета со стороной N
    square = Square(N, "красный")
    print(Fore.RED + str(square))

    # Демонстрация работы внешнего пакета colorama
    print(Fore.YELLOW + "\n=== Демонстрация внешнего пакета colorama ===")
    print(Fore.MAGENTA + Back.WHITE + "Этот текст использует colorama для цветного вывода!")
    print(Fore.CYAN + "Цветной вывод в консоли")
    print(Style.BRIGHT + Fore.WHITE + Back.RED + "Яркий текст на красном фоне")

    # Вывод информации о фигурах с использованием colorama
    print(Fore.CYAN + "\n=== Цветной вывод информации о фигурах ===")
    print(Fore.BLUE + f"Прямоугольник: {rectangle.area():.2f}")
    print(Fore.GREEN + f"Круг: {circle.area():.2f}")
    print(Fore.RED + f"Квадрат: {square.area():.2f}")

if __name__ == "__main__":
    main()
