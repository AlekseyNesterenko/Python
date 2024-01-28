# В большой текстовой строке text подсчитать количество встречаемых слов и вернуть 10 самых частых. 
# Не учитывать знаки препинания и регистр символов.
# Слова разделяются пробелами. Такие слова как don t, it s, didn t итд (после того, как убрали знак препинания апостроф) считать двумя словами.
# Цифры за слова не считаем.
# Отсортируйте по убыванию значения количества повторяющихся слов.


# text = "Python 3.9 is the latest version of Python. It's awesome!"

# import re
# from collections import Counter

# def count_most_common_words(text):
#     # Удаление знаков препинания и приведение к нижнему регистру
#     text = text.replace("'", " ")
#     text = re.sub(r'[^\w\s]', '', text).lower()
    
#     # Раздел на слова
#     words = text.split()
    
#     # Фильтрация и подсчет слов, исключая цифры
#     word_counts = Counter(filter(lambda word: not word.isdigit(), words))

#     return word_counts.most_common(10)

# print(count_most_common_words(text))


# На вход подается словарь со списком вещей для похода в качестве ключа и их массой max_weight в качестве значения.
# Определите какие вещи влезут в рюкзак backpack передав его максимальную грузоподъёмность.
# Результат должен быть в виде словаря {предмет:вес} с вещами в рюкзаке и сохранен в переменную backpack.
# Достаточно получить один допустимый вариант и сохранить в переменную backpack. Не выводите backpack на экран.


items = {
    "ключи": 0.3,
    "кошелек": 0.2,
    "телефон": 0.5,
    "зажигалка": 0.1
}
max_weight = 1.0

# backpack = {}
# for item, weight in items.items():
#     if weight <= max_weight:
#         backpack[item] = weight
#         max_weight -= weight
# print(backpack)

def choose_items(items, max_weight):
    backpack = {}
    total_weight = 0.0

    sorted_items = sorted(items.items(), key=lambda x: x[1])

    for item, weight in sorted_items:
        if total_weight + weight <= max_weight:
            backpack[item] = weight
            total_weight += weight
    
    return backpack
backpack = choose_items(items, max_weight)
print(backpack)

# На вход подается словарь со списком вещей для похода в качестве ключа и их массой max_weight в качестве значения.
# Определите какие вещи влезут в рюкзак backpack передав его максимальную грузоподъёмность.
# В переменную backpack сохраните словарь {предмет:вес} с вещами в рюкзаке.
# В переменную result выведите список, содержащий все возможные варианты backpack. Напечатайте переменную result.
# *Верните все возможные варианты комплектации рюкзака.











# Дан список повторяющихся элементов lst. Вернуть список с дублирующимися элементами. 
# В результирующем списке не должно быть дубликатов.

# lst = [1, 2, 3, 2, 4, 5, 4]

# list_no_duplicate = []

# for el in lst:
#     count = lst.count(el)
#     if count > 1 and el not in list_no_duplicate:
#         list_no_duplicate.append(el)
# print(list_no_duplicate)

