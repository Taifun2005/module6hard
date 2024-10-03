class Figure:      #Фигура
    sides_count = 0
    def __init__(self, color, sides):
        self.__sides = sides if self.__is_valid_sides(*sides) else [1] * self.sides_count  #(список сторон(целые числа))
        self.__color = color if self.__is_valid_color(*color) else [0, 0, 0]    #(список цветов в формате RGB)
        self.filled = False      #(закрашенный, bool)

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):    #проверяет корректность переданных значений перед установкой нового цвета.
        if 0 <= r <= 255 or 0 <= g <= 255 or 0 <= b <= 255:
            return True

    def set_color(self, r, g, b):   #изменяет атрибут __color на соответствующие значения
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *sides):
        is_valid_count = len(sides) == self.sides_count
        return is_valid_count

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

class Circle(Figure):        #Фигура КРУГ
    sides_count = 1

    def __init__(self, color, sides):
        super().__init__(color, sides)
        self.__radius = sides / (2 * 3.14)

    def get_square(self):
       return 3.14 * self.__radius * 2


class Triangle(Figure):      #Фигура ТРЕУГОЛЬНИК
    sides_count = 3

    def __init__(self, color, sides):
        super().__init__(color, sides)

    def get_square(self, color, sides):
        s = (self.__len__() / 2)
        return sqrt(s(s - self.__sides[0])(s - self.__sides[1])(s - self.__sides[2]))

class Cube(Figure):     #Фигура КУБ
    sides_count = 12
    def __init__(self, color, sides):
        super().__init__(color, sides)
        self.__sides = [sides] ** 12

    def get_volume(self):
        return self.sides ** 3


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())