# Ваша задача - написать программу, которая принимает на вход директорию и рекурсивно обходит эту директорию и все вложенные директории. 
# Результаты обхода должны быть сохранены в нескольких форматах: JSON, CSV и Pickle. 
# Каждый результат должен содержать следующую информацию:
# Путь к файлу или директории: Абсолютный путь к файлу или директории. 
# Тип объекта: Это файл или директория. 
# Размер: Для файлов - размер в байтах, для директорий - размер, учитывая все вложенные файлы и директории в байтах. 
# Важные детали:
# Для дочерних объектов (как файлов, так и директорий) укажите родительскую директорию.
# Для файлов сохраните их размер в байтах.
# Для директорий, помимо их размера, учтите размер всех файлов и директорий, находящихся внутри данной директории, и вложенных директорий.
# Программа должна использовать рекурсивный обход директорий, чтобы учесть все вложенные объекты.
# Результаты должны быть сохранены в трех форматах: JSON, CSV и Pickle. Форматы файлов должны быть выбираемыми.
# Для обхода файловой системы вы можете использовать модуль os.
# Вам необходимо написать функцию traverse_directory(directory), 
# которая будет выполнять обход директории и возвращать результаты в виде списка словарей. 
# После этого результаты должны быть сохранены в трех различных файлах (JSON, CSV и Pickle) 
# с помощью функций save_results_to_json, save_results_to_csv и save_results_to_pickle.
import json
import csv
import pickle
import os


def traverse_directory(directory):
    results = []

    for root, dirs, files in os.walk(directory):
        for name in files:
            path = os.path.join(root, name)
            type = "File"
            size = os.path.getsize(path)
            results.append({"Path": path, "Type": type, "Size": size})

        for name in dirs:
            path = os.path.join(root, name)
            type = "Directory"
            size = get_dir_size(path)
            results.append({"Path": path, "Type": type, "Size": size})

    return results

def get_dir_size(path):
    total_size = 0

    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            total_size += os.path.getsize(file_path)

    return total_size


def save_results_to_json(result):
    with open('result.json', 'w', encoding='uft-8') as f:
        return json.dump(result, f, indent=4)

def save_results_to_csv(result):
    with open('result.csv', 'w', encoding='utf-8') as f:
        writer = csv.DictWriter(f, ['Path', 'Type', 'Size']) 
        writer.writeheader()
        writer.writerows(result)

def save_results_to_pickle(result):
    with open('result.pickle', 'wb') as f:
        return pickle.dump(result, f)
    


