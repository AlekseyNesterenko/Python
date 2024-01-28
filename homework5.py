# Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины: 
# имена str, 
# ставка int, 
# премия str с указанием процентов вида 10.25%.
# В результате result получаем словарь с именем в качестве ключа и суммой премии в качестве значения.

# names = ["Alice", "Bob", "Charlie"]
# salary = [5000, 6000, 7000]
# bonus = ["10%", "5%", "15%"]

# result = {i[0]: i[1] * int(i[2][:-1])/100 for i in zip(names, salary, bonus)}

# print(result)




# Напишите функцию get_file_info, которая принимает на вход строку - абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

import os.path

def get_file_info(file_path):
    path, name_extension = os.path.split(file_path)
    name, extension = os.path.splitext(name_extension)
    return (path, name, extension)

file_path = 'file_in_current_directory.txt'

print(get_file_info(file_path='file_in_current_directory.txt'))

# Вывод: ('C:/Users/User/Documents/', 'example', '.txt')








# Создайте функцию генератор чисел Фибоначчи fibonacci.

# def fibonacci():
#     number, number_next  = 0, 1
#     while True:
#         yield number
#         res = number + number_next
#         number, number_next = number_next, res


# f = fibonacci()
# for i in range(10):
#     print(next(f))
