data_to_write = '''
import csv
import json
from random import randint

def save_to_json(func):
    def wrapper(file_name):
        with open('results.json', 'w', encoding='utf-8') as f:
            cont = func(file_name)
            json.dump(cont, f, indent=4)
    return wrapper


def generate_csv_file(file_name: str, rows: int):
    data = [[randint(1, 20),randint(-10, 10),randint(-10, 10)] for _ in range(rows)]
    with open(file_name, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)



@save_to_json
def find_roots(file_name):
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
'''

with open('__init__.py', 'w', encoding='utf-8') as f:
    f.write(data_to_write)
