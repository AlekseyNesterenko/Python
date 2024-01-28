# Разработать класс Matrix, представляющий матрицу и обеспечивающий базовые операции с матрицами.
# Атрибуты класса:
# rows (int): Количество строк в матрице.
# cols (int): Количество столбцов в матрице.
# data (list): Двумерный список, содержащий элементы матрицы.
# Добавьте к ним логирование ошибок и полезной информации. 
# Написать 5-10 тестов для каждого задания при помощи 
# любой понравившейся библиоткеки(pytest, unittest, doctest).

import logging
import unittest

FORMAT = '%(asctime)s | %(levelname)s | %(message)s'


logging.basicConfig(format=FORMAT,
                    filename=f"task2.log", 
                    filemode='a',
                    level=logging.DEBUG,
                    encoding='utf-8')

class Matrix:

    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.data = [[0 for _ in range(cols)] for _ in range(rows)]
        logging.debug(f'Создана матрица размером {rows}x{cols}')

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return f'Matrix({self.rows}, {self.cols})'
    
    def __eq__(self, other):
        '''
        Метод, определяющий операцию "равно" для двух матриц. 
        Сравнивает две матрицы и возвращает True, 
        если они имеют одинаковое количество строк и столбцов, а также все элементы равны. 
        Иначе возвращает False
        '''
        self_data = [sorted(i) for i in self.data]
        other_data = [sorted(i) for i in other.data]
        result = (self.rows == other.rows and 
                self.cols == other.cols and 
                self_data == other_data)
        logging.debug(f'Сравнение двух матриц: {self} и {other}. Результат: {result}')
        return result

    def __add__(self, other):
        '''
        Метод, определяющий операцию сложения двух матриц. 
        Проверяет, что обе матрицы имеют одинаковые размеры (количество строк и столбцов). 
        Если размеры совпадают, создает новую матрицу, 
        где каждый элемент равен сумме соответствующих элементов входных матриц.
        '''
        if self.rows == other.rows and self.cols == other.cols:
            result = Matrix(self.rows, self.cols)
            result.data = [[self.data[i][j] + other.data[i][j]  
                            for j in range(len(self.data[0]))] 
                            for i in range(len(self.data))]
        else:
            logging.error(f'При сложении двух матриц возникла ошибка. {ValueError}(Сложение матриц невозможно)')
            raise ValueError('Сложение матриц невозможно')
        logging.debug(f'Сложение матрицы {self} и матрицы {other}. Результат: {result}')
        return result


    def __mul__(self, other):
        '''
        Метод, определяющий операцию умножения двух матриц. 
        Проверяет, что количество столбцов в первой матрице равно количеству строк во второй матрице. 
        Если условие выполняется, создает новую матрицу, где элемент на позиции [i][j] 
        равен сумме произведений элементов соответствующей строки из первой матрицы и столбца из второй матрицы.
        '''
        try:
            if self.cols == other.rows:
                result = Matrix(self.rows, self.cols)
                for i in range(self.rows):
                    for j in range(other.cols):
                        for k in range(self.cols):
                            result.data[i][j] += self.data[i][k] * other.data[k][j]
            else:
                logging.error(f'При умножении двух матриц возникла ошибка. {ValueError}(Умножение матриц невозможно)')
                raise ValueError('Умножение матриц невозможно')
            logging.debug(f'Умножение матрицы {self} и матрицы {other}. Результат: {result}')
            return result
        except IndexError as e:
            logging.error(f'При умножении двух матриц возникла ошибка. {IndexError}(list index out of range)')
            raise IndexError('list index out of range')

# Выполняем операцию умножения матриц
matrix3 = Matrix(3, 2)
matrix3.data = [[1, 2], [3, 4], [5, 6]]

matrix4 = Matrix(2, 3)
matrix4.data = [[7, 8, 4], [9, 10, 5]]

result = matrix3 * matrix4
print(result)

matrix5 = Matrix(4, 3)