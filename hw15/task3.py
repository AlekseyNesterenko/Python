# Добавьте к ним логирование ошибок и полезной информации. 
# Написать 5-10 тестов для каждого задания при помощи 
# любой понравившейся библиоткеки(pytest, unittest, doctest).

import csv
import json
from random import randint
import logging
import unittest
import traceback

FORMAT = '%(asctime)s | %(levelname)s | %(message)s'


logging.basicConfig(format=FORMAT,
                    filename=f"task3.log", 
                    filemode='a',
                    level=logging.DEBUG,
                    encoding='utf-8')

def save_to_json(func):
    ''' 
    Декоратор выполняет следующие действия:
    Читает данные из CSV-файла.
    Для каждой строки данных вычисляет корни квадратного уравнения с помощью функции find_roots.
    Сохраняет результаты в формате JSON в файл results.json. 
    Каждая запись JSON содержит параметры a, b, c и результаты вычислений.
    Таким образом, после выполнения функций generate_csv_file и find_roots 
    в файле results.json будет сохранена информация о параметрах и результатах вычислений для каждой строки данных из CSV-файла.'''
    def wrapper(file_name):
        with open('results.json', 'w', encoding='utf-8') as f:
            cont = func(file_name)
            json.dump(cont, f, indent=4)
            logging.debug(f'Все решения сохранены в файле results.json')
    return wrapper


def generate_csv_file(file_name: str, rows: int):
    '''Генерирует по три случайны числа в каждой строке, 
    от 100-1000 строк, и записывать их в CSV-файл. 
    Функция принимает два аргумента:
    file_name (строка) - имя файла, в который будут записаны данные.
    rows(целое число) - количество строк (записей) данных, которые нужно сгенерировать.'''

    data = [[randint(1, 20),randint(-10, 10),randint(-10, 10)] for _ in range(rows)]
    with open(file_name, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)
    logging.debug(f'Создан файл {file_name} и сгенерированы {rows} строк по 3 числа в каждой')



@save_to_json
def find_roots(file_name):
    '''
    Функция принимает три аргумента:
    a, b, c (целые числа) - коэффициенты квадратного уравнения.
    Функция возвращает:
    None, если уравнение не имеет корней (дискриминант отрицателен).
    Одно число, если уравнение имеет один корень (дискриминант равен нулю).
    Два числа (корни), если уравнение имеет два корня (дискриминант положителен)'''
    cont = []
    with open(file_name, 'r') as f:
        data = [list(map(int, line.strip('\n').split(','))) for line in f]
    for args in data:
        a, b, c = args
        d = b ** 2 - 4 * a * c
        if d < 0:
            result = None
            logging.debug(f'Решено квадратноо уравнение: {a}x**2 + {b}x + {c}. Ответ: {result}')
        elif d == 0:
            result = (-b) / (2 * a)
            logging.debug(f'Решено квадратноо уравнение: {a}x**2 + {b}x + {c}. Ответ: {result}')
        else:
            result = [(-b - d**(1/2))/(2*a),(-b + d**(1/2))/(2*a)]
            logging.debug(f'Решено квадратноо уравнение: {a}x**2 + {b}x + {c}. Ответ: {result}')
        cont.append({'a': args[0], 'b': args[1], 'c': args[2], 'answer': result})
    return cont

if __name__ == '__main__':
    try:
        generate_csv_file('input_data.csv', 5)
        find_roots("input_data.csv")
    except Exception as e:
        logging.error(f'Произошла ошибка {e.__class__}')
        print('Ошибка:\n', traceback.format_exc())