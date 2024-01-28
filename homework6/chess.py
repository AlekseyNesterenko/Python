# Добавьте в пакет, созданный на семинаре шахматный модуль.
# Внутри него напишите код, решающий задачу о 8 ферзях, включающий в себя
# функцию is_attacking(q1,q2), проверяющую, бьют ли ферзи друг друга и 
# check_queens(queens), которая проверяет все возможные пары ферзей.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. 
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, 
# каждое число от 1 до 8 - координаты 8 ферзей. 
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь. 
# Не забудьте напечатать результат.

from random import randint

def check_queens(queens):
    for i in queens:
        for j in queens:
            if i != j:
                if is_attacking(i, j) is True:
                    return False
    return True

def is_attacking(q1,q2):
    if q1[0] != q2[0] and q1[1] != q2[1] and (abs(q1[0] - q2[0]) != abs(q1[1] - q2[1])):
        return False
    else:
        return True
        
# def generate_chess_board() -> list:
#     board = []
#     for raws in range(1, 9):
#         for col in range(1, 9):
#             board.append((raws,col))
#     return board

def find_position() -> list:
    result = []
    while len(result) < 4:
        guess = []
        raw = 1
        while len(guess) < 8:
            col = randint(1,8)
            if (raw, col) not in guess:
                guess.append((raw,col))
                raw += 1
        if check_queens(guess) is True:
            result.append(guess)
    return result


board_list = find_position()
if __name__ == '__main__':
    print(board_list)


# [[(1, 4), (2, 7), (3, 1), (4, 8), (5, 5), (6, 2), (7, 6), (8, 3)], 
#  [(1, 5), (2, 3), (3, 8), (4, 4), (5, 7), (6, 1), (7, 6), (8, 2)], 
#  [(1, 3), (2, 6), (3, 8), (4, 2), (5, 4), (6, 1), (7, 7), (8, 5)], 
#  [(1, 6), (2, 1), (3, 5), (4, 2), (5, 8), (6, 3), (7, 7), (8, 4)]]

# [[(1, 8), (2, 2), (3, 5), (4, 3), (5, 1), (6, 7), (7, 4), (8, 6)], 
#  [(1, 6), (2, 1), (3, 5), (4, 2), (5, 8), (6, 3), (7, 7), (8, 4)], 
#  [(1, 6), (2, 3), (3, 7), (4, 2), (5, 4), (6, 8), (7, 1), (8, 5)], 
#  [(1, 2), (2, 5), (3, 7), (4, 1), (5, 3), (6, 8), (7, 6), (8, 4)]]