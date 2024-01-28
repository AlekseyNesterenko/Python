# Напишите функцию для транспонирования матрицы transposed_matrix, 
# принимает в аргументы matrix, и возвращает транспонированную матрицу.
# Пример использования На входе:


# def transpose(matrix=[]):
#     transposed_matrix = [list(i) for i in zip(*matrix)]
#     return transposed_matrix
        
    

# matrix = [[1, 2, 3],
#          [4, 5, 6], 
#          [7, 8, 9]]

# transposed_matrix = transpose(matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(matrix)
# print(transposed_matrix)




# Напишите функцию key_params, принимающую на вход только ключевые параметры и возвращающую словарь, 
# где ключ - значение переданного аргумента, а значение - имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.
# Пример использования.
# На входе:


# def key_params(**kwargs) -> dict:
#     result ={}
#     for key, value in kwargs.items():
#             if isinstance(value, (int, str, float, bool, tuple)):
#                   value                
#             else:
#                   value = str(value)
#             result[value] = key
#     return result


# params = key_params(a=1, b='hello', c=[1, 2, 3], d={}, f = None)
# print(params)




# На выходе:
# {1: 'a', 'hello': 'b', '[1, 2, 3]': 'c', '{}': 'd'}




# У вас есть банковская карта с начальным балансом равным 0 у.е. Вы хотите управлять этой картой, 
# выполняя следующие операции, для выполнения которых необходимо написать следующие функции:

# check_multiplicity(amount): Проверка кратности суммы при пополнении и снятии.
# deposit(amount): Пополнение счёта.
# withdraw(amount): Снятие денег.
# exit(): Завершение работы и вывод итоговой информации о состоянии счета и проведенных операциях.

# Пополнение счета:

# Функция deposit(amount) позволяет клиенту пополнять свой счет на определенную сумму. 
# Пополнение счета возможно только на сумму, которая кратна MULTIPLICITY.

# Снятие средств:

# Функция withdraw(amount) позволяет клиенту снимать средства со счета. 
# Сумма снятия также должна быть кратной MULTIPLICITY. 
# При снятии средств начисляется комиссия в процентах от снимаемой суммы, которая может варьироваться от MIN_REMOVAL до MAX_REMOVAL.

# Завершение работы:

# Функция exit() завершает работу с банковским счетом. 
# Перед завершением, если на счету больше RICHNESS_SUM, начисляется налог на богатство в размере RICHNESS_PERCENT процентов.

# Проверка кратности суммы:

# Функция check_multiplicity(amount) проверяет, кратна ли сумма amount заданному множителю MULTIPLICITY. 
# Реализуйте программу для управления банковским счетом, используя библиотеку decimal для точных вычислений.

import decimal

MULTIPLICITY = 50
PERCENT_REMOVAL = decimal.Decimal(15) / decimal.Decimal(1000)
MIN_REMOVAL = decimal.Decimal(30)
MAX_REMOVAL = decimal.Decimal(600)
PERCENT_DEPOSIT = decimal.Decimal(3) / decimal.Decimal(100)
COUNTER4PERCENTAGES = 3
RICHNESS_PERCENT = decimal.Decimal(10) / decimal.Decimal(100)
RICHNESS_SUM = decimal.Decimal(10_000_000)

bank_account = decimal.Decimal(0)
count = 0
operations = []


# def check_multiplicity(amount) -> bool:
#     if amount % MULTIPLICITY == 0:
#         return True
#     else:
#         return False

# def deposit(amount):
#     global bank_account
#     if check_multiplicity(amount):
#         bank_account += amount
#         result = f'Пополнение карты на {amount} у.е. Итого {bank_account} у.е.'
#         operations.append(result)
#         return
#     else:
#         return print(f'Сумма должна быть кратной {MULTIPLICITY} у.е.')

# def withdraw(amount):
#     global bank_account
    
#     comission = amount * PERCENT_REMOVAL
#     if comission == int(comission):
#         comission = round(comission, 0)
#     if comission < MIN_REMOVAL:
#         comission = MIN_REMOVAL
#     elif comission > MAX_REMOVAL:
#         comission = MAX_REMOVAL
#     outcome = amount + comission
#     if check_multiplicity(amount):
#         if outcome < bank_account:
#             bank_account -= outcome
#             result = f'Снятие с карты {amount} у.е. Процент за снятие {comission} у.е.. Итого {bank_account} у.е.'
#             operations.append(result)
#         else:
#             result = f'Недостаточно средств. Сумма с комиссией {outcome} у.е. На карте {bank_account} у.е.'
#             operations.append(result)
#             return
#     else:
#         print(f'Сумма должна быть кратной {MULTIPLICITY} у.е.')
#         result = f'Недостаточно средств. Сумма с комиссией {outcome} у.е. На карте {bank_account} у.е.'
#         operations.append(result)
#         return 

# def exit():
#     global bank_account
#     if bank_account >= RICHNESS_SUM:
#         rich_tax = round(bank_account * RICHNESS_PERCENT, 4)
#         bank_account -= rich_tax
#         result = f'Вычтен налог на богатство {RICHNESS_PERCENT}% в сумме {rich_tax} у.е. Итого {bank_account} у.е.'
#         operations.append(result)
#     result = f'Возьмите карту на которой {bank_account} у.е.'
#     operations.append(result)
#     return

def check_multiplicity(amount):
    """Проверка кратности суммы"""
    if (amount % MULTIPLICITY) != 0:
        print(f'Сумма должна быть кратной {MULTIPLICITY} у.е.')
        return False
    return True

def deposit(amount):
    """Пополнение счета"""
    global bank_account, count
    if not check_multiplicity(amount):
        print(f'Сумма должна быть кратной {MULTIPLICITY} у.е.')
        return False  # Операция не выполнена из-за некратной суммы
    count += 1
    bank_account += amount
    operations.append(f'Пополнение карты на {amount} у.е. Итого {bank_account} у.е.')
    return True


def withdraw(amount):
    """Снятие денег"""
    global bank_account, count
    percent = amount * PERCENT_REMOVAL
    percent = MIN_REMOVAL if percent < MIN_REMOVAL else MAX_REMOVAL if percent > MAX_REMOVAL else percent
    if bank_account >= amount + percent:
        count += 1
        bank_account = bank_account - amount - percent
        operations.append(f'Снятие с карты {amount} у.е. Процент за снятие {int(percent)} у.е.. Итого {int(bank_account)} у.е.')
    else:
        operations.append(
            f'Недостаточно средств. Сумма с комиссией {amount + int(percent)} у.е. На карте {int(bank_account)} у.е.')

def exit():
    global bank_account, operations
    if bank_account > RICHNESS_SUM:
        percent = bank_account * RICHNESS_PERCENT
        bank_account -= percent
        operations.append(
            f'Вычтен налог на богатство {RICHNESS_PERCENT}% в сумме {percent} у.е. Итого {bank_account} у.е.')
    operations.append(f'Возьмите карту на которой {bank_account} у.е.')




deposit(173)
withdraw(21)
exit()

print(operations)

#  ['Пополнение карты на 10000 у.е. Итого 10000 у.е.', 
#   'Снятие с карты 4000 у.е. Процент за снятие 60 у.е.. Итого 5940 у.е.']




