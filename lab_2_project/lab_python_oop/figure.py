from abc import ABC, abstractmethod

class Figure(ABC):
    """
    Абстрактный класс Геометрическая фигура
    """

    @abstractmethod
    def area(self):
        """Абстрактный метод для вычисления площади фигуры"""
        pass

    def __repr__(self):
        """Возвращает строковое представление фигуры"""
        return "{} {} цвета площадью {:.2f}".format(
            self.name,
            self.color.color,
            self.area()
        )

    @property
    @abstractmethod
    def name(self):
        """Абстрактное свойство для имени фигуры"""
        pass
