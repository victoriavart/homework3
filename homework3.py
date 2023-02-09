# Задача 16
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X.
# Пример:
# 5
# 1 2 3 4 5
# 3
# # -> 1
# from random import randint
# a = int(input('Введите количество элементов в массиве: '))
# list_1 = []
# for i in range(a):
#    list_1.append(randint(1, a))
# list_1 = [randint(1, a) for i in range(a)]
# print(list_1)
#
# b = int(input('Введите число x: '))
# c = list_1.count(3)
# print(c)

# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих строках
# записаны N целых чисел Ai. Последняя строка содержит число X
# 5
# 1234 5
# # 6 -> 5
#
# from random import randint
# a = int(input('Введите количество элементов в массиве: '))
# list_1 = []
# for i in range(a):
#    list_1.append(randint(1, a))
# list_1 = [randint(1, a) for i in range(a)]
# print(list_1)
# list_1.sort()
#
# def get_unique_numbers(list_1):
#     unique = []
#
#     for number in list_1:
#         if number in unique:
#             continue
#         else:
#             unique.append(number)
#     return unique
#
#
# print(get_unique_numbers(list_1))
#
#
# b = int(input('Введите число x: '))
# c = get_unique_numbers(list_1)[b+1]
# d = get_unique_numbers(list_1)[b-1]
#
#
# if b - d > c - b:
#     print(c)
# elif b - d < c - b:
#     print(d)
# else:
#     print(c)
#     print(d)



# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские,
# либо только русские буквы.

list_1 = {'a': 1, 'e': 1, 'i': 1, 'o': 1, 'u': 1, 'l': 1,
          'n': 1, 's': 1, 't': 1, 'r': 1, 'd': 2, 'g': 2,
          'b': 3, 'c': 3, 'm': 3, 'p': 3, 'f': 4, 'h': 4,
          'v': 4, 'w': 4, 'y': 4, 'k': 5, 'j': 6, 'x': 6,
          'q': 7, 'z': 7}
str = 'castle'
res = 0
for i in str:
    print(i)
    res += list_1[i]
print(res)