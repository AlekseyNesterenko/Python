# Напишите программу, которая получает целое число num и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

# num = 0
# hexar_dict = {'0':'0', '1':'1' , '2':'2' , '3': '3' , '4':'4' , '5':'5' , '6':'6' , '7':'7' , '8':'8' , '9':'9',
#               '10':'A', '11':'B', '12':'C', '13':'D', '14':'E', '15':'F'}

# def hexar( num: int, dict) -> str:
#     res = ""
#     while num > 0:
#         res = dict.get(str(num % 16)) + res
#         num //= 16
#     return res


# print(f'Шестнадцатеричное представление числа: {hexar(num, hexar_dict)}')
# print(f'Проверка результата: {hex(num)}')


# На вход автоматически подаются две строки frac1 и frac2 вида a/b - дробь с числителем и знаменателем.
# Напишите программу, которая должна возвращать сумму и произведение дробей.
# Для проверки своего кода используйте модуль fractions.
import fractions


frac1 = "1/2"
frac2 = "1/3"

numerator1 = int(frac1.split('/')[0])
denominator1 = int(frac1.split('/')[1])

numerator2 = int(frac2.split('/')[0])
denominator2 = int(frac2.split('/')[1])

print(f'Сумма дробей: {(numerator1 *denominator2) + (numerator2 * denominator1) }/{denominator1 * denominator2}')
print(f'Произведение дробей: {numerator1 * numerator2}/{denominator1 * denominator2}')

f1 = fractions.Fraction(numerator1, denominator1)
f2 = fractions.Fraction(numerator2, denominator2)

print(f'Сумма дробей: {f1 + f2}')
print(f'Произведение дробей: {f1 * f2}')
