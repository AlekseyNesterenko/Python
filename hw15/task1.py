# Создайте базовый класс Animal, который имеет атрибут name, представляющий имя животного.
# Создайте классы Bird, Fish и Mammal, которые наследуются от базового класса Animal и добавляют дополнительные атрибуты и методы.
# Создайте класс-фабрику AnimalFactory, который будет создавать экземпляры животных разных типов на основе переданного типа и параметров. 
# Добавьте к ним логирование ошибок и полезной информации. 
# Написать 5-10 тестов для каждого задания при помощи 
# любой понравившейся библиоткеки(pytest, unittest, doctest).

import logging
import unittest

FORMAT = '%(asctime)s | %(levelname)s | %(message)s'


logging.basicConfig(format=FORMAT,
                    filename=f"task1.log", 
                    filemode='a',
                    level=logging.DEBUG,
                    encoding='utf-8')

class Animal:
    '''
    Класс Animal, который имеет атрибут name, представляющий имя животного.
    '''
    def __init__(self, name):
        self.name = name

class Fish(Animal):
    '''
    Fish имеет атрибут max_depth (максимальная глубина обитания) и метод depth, 
    который возвращает категорию глубины рыбы (мелководная, средневодная, глубоководная) 
    в зависимости от значения max_depth.
    Если максимальная глубина обитания рыбы (max_depth) меньше 10, 
    то она относится к категории "Мелководная рыба".
    Если максимальная глубина обитания рыбы больше 100, 
    то она относится к категории "Глубоководная рыба".
    В противном случае, рыба относится к категории "Средневодная рыба".
    '''
    def __init__(self, name, max_depth):
        super().__init__(name)
        self.max_depth = max_depth
    
    def depth(self):
        if self.max_depth < 10:
            return f'Меловодная рыба'
        elif self.max_depth > 100:
            return f'Глубоководная рыба'
        else:
            return f'Средневодная рыба'

class Bird(Animal):
    '''
    Bird имеет атрибут wingspan (размах крыльев) 
    и метод wing_length, который возвращает длину крыла птицы.
    '''
    def __init__(self, name, wingspan):
        super().__init__(name)
        self.wingspan = wingspan
    
    def wing_length(self):
        return self.wingspan / 2

class Mammal(Animal):
    '''
    Mammal имеет атрибут weight (вес) и метод category, 
    который возвращает категорию млекопитающего (Малявка, Обычный, Гигант) 
    в зависимости от веса. 
    Если вес объекта меньше 1, то он относится к категории "Малявка".
    Если вес объекта больше 200, то он относится к категории "Гигант".
    В противном случае, объект относится к категории "Обычный".
    '''
    def __init__(self, name, weight):
        super().__init__(name)
        self.weight = weight
    
    def category(self):
        if self.weight < 1:
            return f'Малявка'
        elif self.weight > 200:
            return f'Гигант'
        else:
            return f'Обычный'


        
class AnimalFactory():
    '''
    Класс-фабрику AnimalFactory, который будет создавать 
    экземпляры животных разных типов на основе переданного типа и параметров.
    '''

    @staticmethod
    def create_animal(animal_type, *args):
        '''
        Принимает следующие аргументы:
        animal_type (строка) - тип животного (один из: 'Bird', 'Fish', 'Mammal').
        *args - переменное количество аргументов, представляющих параметры для конкретного типа животного. 
        Количество и типы аргументов могут различаться в зависимости от типа животного.
        Метод create_animal должен создавать и возвращать экземпляр животного заданного типа с переданными параметрами.
        Если animal_type не соответствует 'Bird', 'Fish' или 'Mammal', функция вызовет ValueError с сообщением 'Недопустимый тип животного'.
        '''
        if animal_type == 'Bird':
            logging.debug(f'Создан класс {animal_type} с атрибутами {args}')
            return Bird(*args)
        elif animal_type == 'Fish':
            logging.debug(f'Создан класс {animal_type} с атрибутами {args}')
            return Fish(*args)
        elif animal_type == 'Mammal':
            logging.debug(f'Создан класс {animal_type} с атрибутами {args}')
            return Mammal(*args)
        else:
            logging.error(f'При попытке создать класс {animal_type} возникла ошибка:'\
                        f'{ValueError}(Недопустимый тип животного)')
            raise ValueError('Недопустимый тип животного')
            
animal1 = AnimalFactory.create_animal('Bird', 'Орел', 200)
animal2 = AnimalFactory.create_animal('Fish', 'Лосось', 50)
animal3 = AnimalFactory.create_animal('Mammal', 'Слон', 5000)
animal4 = AnimalFactory.create_animal('Spider', 'Elephant', 5000)

        