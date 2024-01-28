"""
Программа для проверки корректности даты, введенной пользователем. 
На вход будет подаваться дата в формате "день.месяц.год". 
Ваша задача - создать программу, которая проверяет, является ли введенная дата корректной или нет.

Ваша программа должна предоставить ответ 
"True" (дата корректна) или 
"False" (дата некорректна) в зависимости от результата проверки.
"""

__all__ = ['check_date']


__DAYS_IN_MONTHS = {
    1: 31, 2: 28, 3: 31, 4: 30, 
    5: 31, 6: 30, 7: 31, 8: 31, 
    9: 30, 10: 31, 11: 30, 12: 31,
}

def check_date(date: str) -> bool:
    day, month, year = [int(x) for x in date.split('.')]
    return (1 <= year <= 9999 
            and 1 <= month <= 12 
            and __day_valid(day, month, year))

def __day_valid(day, month, year) -> bool:
    if __is_year_leap(year) and month == 2:
        return 1 <= day <= 29
    return 1 <= day <= __DAYS_IN_MONTHS[month]


def __is_year_leap(year) -> bool:
    return (year % 4 == 0 and year % 100 != 0 or year % 400 == 0)


date_to_prove = '12.0.2022'

if __name__ == '__main__':
    print(check_date(date_to_prove))