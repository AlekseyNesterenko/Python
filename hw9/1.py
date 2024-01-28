import csv
import json
from random import randint

def save_to_json(func):
    '''Создайте декоратор save_to_json(func), который будет оборачивать функцию find_roots. 
    Декоратор выполняет следующие действия:
    Читает данные из CSV-файла, переданного в аргументе функции, исходя из аргумента args[0].
    Для каждой строки данных вычисляет корни квадратного уравнения с помощью функции find_roots.
    Сохраняет результаты в формате JSON в файл results.json. 
    Каждая запись JSON содержит параметры a, b, c и результаты вычислений.
    Таким образом, после выполнения функций generate_csv_file и find_roots 
    в файле results.json будет сохранена информация о параметрах и результатах вычислений для каждой строки данных из CSV-файла.'''
    def wrapper(file_name):
        with open('results.json', 'w', encoding='utf-8') as f:
            cont = func(file_name)
            json.dump(cont, f, indent=4)
    return wrapper


def generate_csv_file(file_name: str, rows: int):
    '''Создайте функцию generate_csv_file(file_name, rows), 
    которая будет генерировать по три случайны числа в каждой строке, 
    от 100-1000 строк, и записывать их в CSV-файл. 
    Функция принимает два аргумента:
    file_name (строка) - имя файла, в который будут записаны данные.
    rows(целое число) - количество строк (записей) данных, которые нужно сгенерировать.'''

    data = [[randint(1, 20),randint(-10, 10),randint(-10, 10)] for _ in range(rows)]
    with open(file_name, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)



@save_to_json
def find_roots(file_name):
    '''Создайте функцию find_roots(a, b, c), которая будет находить корни квадратного уравнения 
    вида ax^2 + bx + c = 0. Функция принимает три аргумента:
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
        elif d == 0:
            result = (-b) / (2 * a)
        else:
            result = [(-b - d**(1/2))/(2*a),(-b + d**(1/2))/(2*a)]
        cont.append({'a': args[0], 'b': args[1], 'c': args[2], 'answer': result})
    return cont

if __name__ == '__main__':
    generate_csv_file("input_data.csv", 101)
    find_roots("input_data.csv")