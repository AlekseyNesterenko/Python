class Range:
    def __init__(self, stop_value):
        self.stop_value = stop_value

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)
    
    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.param_name, value)

    def __delete__(self, isinstance):
        raise AttributeError(f'Свойство "{self.param_name}" нельзя удалить')
    
    def validate(self, value):
        if value <= self.stop_value:
            if str(self.param_name) == 'self.height':
                raise NegativeValueError(f'Высота должна быть положительной, а не {value}')
            if str(self.param_name) == 'self.width':
                raise NegativeValueError(f'Ширина должна быть положительной, а не {value}')

class NegativeValueError(Exception):
    pass


class Rectangle:
    # width = Range(0)
    # height = Range(0)
    """
    Класс, представляющий прямоугольник.

    Атрибуты:
    - width (int): ширина прямоугольника
    - height (int): высота прямоугольника

    Методы:
    - perimeter(): вычисляет периметр прямоугольника
    - area(): вычисляет площадь прямоугольника
    - __add__(other): определяет операцию сложения двух прямоугольников
    - __sub__(other): определяет операцию вычитания одного прямоугольника из другого
    - __lt__(other): определяет операцию "меньше" для двух прямоугольников
    - __eq__(other): определяет операцию "равно" для двух прямоугольников
    - __le__(other): определяет операцию "меньше или равно" для двух прямоугольников
    - __str__(): возвращает строковое представление прямоугольника
    - __repr__(): возвращает строковое представление прямоугольника, которое может быть использовано для создания нового объекта
    """

    def __init__(self, width, height=None):
        if height is None:
            raise NegativeValueError(f'Ширина должна быть положительной, а не {width}')
        if height <= 0:
            raise NegativeValueError(f'Высота должна быть положительной, а не {height}')
        if width <= 0:
            raise NegativeValueError(f'Ширина должна быть положительной, а не {width}')
        self.width = width
        if height is None:
            self.height = width
        else:
            self.height = height
    
    @property
    def height(self):
        return self.height
    
    @height.setter
    def height(self, value):
        if value <= 0:
            raise NegativeValueError(f'Высота должна быть положительной, а не {value}')
            

    @property
    def width(self):
        return self.width
    
    @width.setter
    def width(self, value):
        if value <= 0:
            raise NegativeValueError(f'Ширина должна быть положительной, а не {value}')
            
        
    def perimeter(self):
        """
        Вычисляет периметр прямоугольника.

        Возвращает:
        - int: периметр прямоугольника
        """
        return 2 * (self.width + self.height)

    def area(self):
        """
        Вычисляет площадь прямоугольника.

        Возвращает:
        - int: площадь прямоугольника
        """
        return self.width * self.height

    def __add__(self, other):
        """
        Определяет операцию сложения двух прямоугольников.

        Аргументы:
        - other (Rectangle): второй прямоугольник

        Возвращает:
        - Rectangle: новый прямоугольник, полученный путем сложения двух исходных прямоугольников
        """
        width = self.width + other.width
        perimeter = self.perimeter() + other.perimeter()
        height = perimeter // 2 - width
        return Rectangle(width, height)

    def __sub__(self, other):
        """
        Определяет операцию вычитания одного прямоугольника из другого.

        Аргументы:
        - other (Rectangle): вычитаемый прямоугольник

        Возвращает:
        - Rectangle: новый прямоугольник, полученный путем вычитания вычитаемого прямоугольника из исходного
        """
        if self.perimeter() < other.perimeter():
            self, other = other, self
        width = abs(self.width - other.width)
        perimeter = self.perimeter() - other.perimeter()
        height = perimeter // 2 - width
        return Rectangle(width, height)

    def __lt__(self, other):
        """
        Определяет операцию "меньше" для двух прямоугольников.

        Аргументы:
        - other (Rectangle): второй прямоугольник

        Возвращает:
        - bool: True, если площадь первого прямоугольника меньше площади второго, иначе False
        """
        return self.area() < other.area()

    def __eq__(self, other):
        """
        Определяет операцию "равно" для двух прямоугольников.

        Аргументы:
        - other (Rectangle): второй прямоугольник

        Возвращает:
        - bool: True, если площади равны, иначе False
        """
        return self.area() == other.area()

    def __le__(self, other):
        """
        Определяет операцию "меньше или равно" для двух прямоугольников.

        Аргументы:
        - other (Rectangle): второй прямоугольник

        Возвращает:
        - bool: True, если площадь первого прямоугольника меньше или равна площади второго, иначе False
        """
        return self.area() <= other.area()

    def __str__(self):
        """
        Возвращает строковое представление прямоугольника.

        Возвращает:
        - str: строковое представление прямоугольника
        """
        return f"Прямоугольник со сторонами {self.width} и {self.height}"

    def __repr__(self):
        """
        Возвращает строковое представление прямоугольника, которое может быть использовано для создания нового объекта.

        Возвращает:
        - str: строковое представление прямоугольника
        """
        return f"Rectangle({self.width}, {self.height})"
    

r = Rectangle(-2)