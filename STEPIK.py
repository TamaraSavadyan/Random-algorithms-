# # ЗАБАВНАЯ ТЕМА ИЗ ФОРУМА
#
# from random import randint
#
# times = 1
# level = float(input('Какой уровень 1 2 3? '))
# if level == 1 or level == 2 or level == 3:
#     score = level
#     print('ПЕРЕХОДИМ НА 1 УРОВЕНЬ')
#     while 2 > level > 0.9:
#         z = randint(1, 2)
#         n1 = randint(1, 5)
#         n2 = randint(1, 5)
#         if z == 1:
#             r = float(input(str(times) + ')' + str(n1) + '+' + str(n2) + '=')) == n1 + n2
#         else:
#             r = float(input(str(times) + ')' + str(n1 + n2) + '-' + str(n1) + '=')) == n1 + n2 - n1
#         if r == 1:
#             print('Правильно')
#             level += 0.1
#             times += 1
#         else:
#             print('Не правильно')
#             times += 1
#     print('ПЕРЕХОДИМ НА 2 УРОВЕНЬ')
#     while 3 > level > 1.9:
#         z = randint(1, 2)
#         n1 = randint(1, 10)
#         n2 = randint(1, 10)
#         if z == 1:
#             r = float(input(str(times) + ')' + str(n1) + '+' + str(n2) + '=')) == n1 + n2
#         else:
#             r = float(input(str(times) + ')' + str(n1 + n2) + '-' + str(n1) + '=')) == n1 + n2 - n1
#         if r == 1:
#             print('Правильно')
#             level += 0.1
#             times += 1
#         else:
#             print('Не правильно')
#             times += 1
#     print('ПЕРЕХОДИМ НА 3 УРОВЕНЬ')
#     while 4 > level > 2.9:
#         z = randint(1, 4)
#         n1 = randint(1, 50)
#         n2 = randint(1, 50)
#         n3 = randint(1, 10)
#         n4 = randint(1, 10)
#         if z == 1:
#             r = float(input(str(times) + ')' + str(n1) + '+' + str(n2) + '=')) == n1 + n2
#         elif z == 2:
#             r = float(input(str(times) + ')' + str(n1 + n2) + '-' + str(n1) + '=')) == n1 + n2 - n1
#         elif z == 3:
#             r = float(input(str(times) + ')' + str(n3) + '*' + str(n4) + '=')) == n3 * n4
#         else:
#             r = float(input(str(times) + ')' + str(n3 * n4) + ':' + str(n4) + '=')) == n3 * n4 / n4
#         if r == 1:
#             print('Правильно')
#             level += 0.1
#             times += 1
#         else:
#             print('Не правильно')
#             times += 1
#     print('Вашь счёт = ' + str(int((level - score) * 10)) + ' из ' + str(times - 1))
# else:
#     print('Такого уровня нету!')
#
# # КОНЕЦ ЗАБАВЫ
# import math
# print(11111 * 1111111)
# print(7/3)
# print(math.pow(2014, 14))
# print(2014**14)
# print((9**19) - int(float(9**19)))

# KolyaNeeds = int(input())
# KatyaInBed_H, KatyaInBed_M = int(input()), int(input())
# KolyaNeeds += KatyaInBed_H * 60 + KatyaInBed_M
# hours = KolyaNeeds // 60
# minutes = KolyaNeeds % 60
# print(hours)
# print(minutes)
# X = int(input()) + 60 * int(input()) + int(input())
# print(X // 60, "\n", X % 60)

# a, b = float(input()), float(input())
# c = input()
# try:
#     if c == '*':
#         print(a * b)
#     elif c == '/':
#         print(a / b)
#     elif c == 'div':
#         print(a // b)
#     elif c == 'pow':
#         print(a ** b)
#     elif c == 'mod':
#         print(a % b)
#     elif c == '+':
#         print(a + b)
#     else:
#         print(a - b)
# except:
#     print("Деление на 0!")
# import math
# room = input()
# if room == 'треугольник':
#     a, b, c = float(input()), float(input()), float(input())
#     p = (a + b + c)/2
#     print(math.sqrt(p*(p-a)*(p-b)*(p-c)))
# elif room == 'прямоугольник':
#     a, b = float(input()), float(input())
#     print(a * b)
# else:
#     r = float(input())
#     print(math.pow(r, 2) * 3.14)
# начало говна
# a, b, c = int(input()), int(input()), int(input())
# if a == b:
#     middle = b
#     if a < c:
#         max = c
#         min = a
#     else:
#         min = c
#         max = a
# elif a == c:
#     middle = c
#     if a < b:
#         max = b
#         min = a
#     else:
#         min = b
#         max = a
# elif b == c:
#     middle = c
#     if a < b:
#         max = b
#         min = a
#     else:
#         min = b
#         max = a
# # конец говна
# if a > b and a > c:
#     max = a
#     if b > c:
#         min, middle = c, b
#     else:
#         min, middle = b, c
# elif b > a and b > c:
#     max = b
#     if a > c:
#         min, middle = c, a
#     else:
#         min, middle = a, c
# elif c > a and c > b:
#     max = c
#     if a > b:
#         min, middle = b, a
#     else:
#         min, middle = a, b
# print(max, "\n", min, "\n", middle)
# # разумный вариант
# a, b, c = int(input()), int(input()), int(input())
# if a < b:
#     a, b = b, a
# if a < c:
#     a, c = c, a
# if b > c:
#     b, c = c, b
# print(a)
# print(b)
# print(c)
#
# number = int(input())
# EndOfWord = 'ов'
# if number % 10 == 1:
#     EndOfWord = ''
# if number % 10 == 2 or number % 10 == 3 or number % 10 == 4:
#     EndOfWord = 'а'
# if number % 100 == 11 or number % 100 == 12 or number % 100 == 13 or number % 100 == 14:
#     EndOfWord = 'ов'
# print(number, 'программист' + EndOfWord)
# ticket = int(input())
# FirstThreeNumbers = ticket // 10**5 + ticket // 10**4 % 10 + ticket // 10**3 % 10
# LastThreeNumbers = ticket % 10 + ticket % 10**2 // 10 + ticket % 10**3 // 100
# if FirstThreeNumbers == LastThreeNumbers:
#     print("Счастливый")
# else:
#     print("Обычный")
# total = 0
# number = int(input())
# while number:
#     total, number = total + number, int(input())
# print(total)

# 1  Выбираем из двух чисел наибольшее и проверяем, делится ли оно на меньшее.
#    Если делится, то это число и есть НОК этих двух чисел.
#
# 2  Если наибольшее число не делится на меньшее, умножаем его на 2
#    и проверяем, делится ли теперь.
#
# 3  Если после умножения на два новое число не делится на меньшее, умножаем
#    на 3,4,5 и так далее до тех пор, пока новое число не станет делится
#    на меньшее. Это новое число и есть НОК (наименьшее общее кратное).
# n, m = int(input()), int(input())
# if n >= m:
#     a, b = n, m
# else:
#     a, b = m, n
# i = 2
# p = a
# while True:
#     if a % b == 0:
#         NOK = a
#         break
#     else:
#         a = p * i
#         i += 1
# print(NOK)
# нормальное решение
# a = int(input())
# b = int(input())
# d = a
# while d % b:
#     d += a
# print(d)
#
# n, m = input().split()
# print(n)
# print(m)
# n = 1
# while n:
#     n = int(input())
#     if 10 <= n <= 100:
#         print(n)
#         continue
#     if n < 10:
#         continue
#     if n > 100:
#         break
# # ТАБЛИЦА УМНОЖЕНИЯ
# a, b, c, d = (int(i) for i in input().split())  # int(input()), int(input()), int(input()), int(input())
# # print(a, b, c, d, end='asds')
# print("", end="\t")
# for i in range(c, d + 1):
#     print(i, end="\t")
# print()
# for i in range(a, b + 1):
#     print(i, end="\t")
#     for j in range(c, d + 1):
#         print(i * j, end="\t")
#     print()
# КОНЕЦ ТАБЛИЦЫ
# # a, b = (int(i) for i in input().split())
# a, b = int(input()), int(input())
# s = 0
# n = 0
# if a % 3 != 0:
#     a += 3 - a % 3
# for i in range(a, b + 1, 3):
#     s += i
#     n += 1
# print(s / n)
# s = input().lower()
# print((s.count('g') + s.count('c')) / len(s) * 100)
# s = 'aaaa'
# print(len(s))
# print(s[3:6])
# print(s[:6])
# print(s[3:])
# print(s[::-1])
# print(s[-3:])
# print(s[:-6])
# print(s[-1:-10:-2])
# if s == s[::-1]:
#     print("ok")

# s = input() + ' '
# s1 = ''
# k = 1
# new_k = []
# new_j = []
# if len(s) == 2:
#     print(s[0] + "1")
# else:
#     for i in range(1, len(s)):
#         if s[i] == s[i - 1]:
#             k += 1
#         else:
#             new_k.append(k)
#             new_j.append(i - 1)
#             k = 1
#     for i in range(0, len(new_k)):
#         s1 += s[new_j[i]] + str(new_k[i])
#     print(s1)
#
# # Нормальное решение этой задачи!!
# g = str(input())
# rep = 1
# out = g[0]
# for i in range(1,len(g)):
#   if (g[i] == g[i-1]):
#     rep +=1
#   else:
#     out = out+str(rep)+g[i]
#     rep=1
# print(out+str(rep))
# students = ['Ivan', 'Masha', 'Sasha']
# students += ['Olga']
# students += 'Olga'
# del students[0:2]
# print(students)
# spisok = [int(i) for i in input().split()]
# summ = 0
# for i in spisok:
#     summ += i
# print(summ)
# # OR
# print(sum(int(i) for i in input().split()))
# spisok = [int(i) for i in input().split()]
# s1 = []
# if len(spisok) == 1 or len(spisok) == 2:
#     for i in spisok:
#         print(i, end=' ')
# else:
#     for i in range(1, len(spisok) - 1):
#         s1.append(spisok[i - 1] + spisok[i + 1])
#     s1.insert(0, spisok[-1] + spisok[1])
#     s1.append(spisok[-2] + spisok[0])
#     for i in s1:
#         print(i, end=' ')

# # авторы не учитывают случай когда 2 элемента в списке, тогда вот красивое решение
# a = [int(i) for i in input().split()]
# if len(a) > 1:
#     for i in range(len(a)):
#         print(a[i - 1] + a[i + 1 - len(a)], end=' ')
# else:
#     print(a[0])
# spis = [int(i) for i in input().split()]
# spis += [9999]
# spis.sort()
# k = 1
# # print(spis)
# for i in range(1, len(spis)):
#     if spis[i] == spis[i - 1]:
#         k += 1
#         # print(k, end='lol ')
#     else:
#         if k > 1:
#             print(spis[i - 1], end=' ')
#             k = 1
#         else:
#             print(end='')
#             k = 1
#
# # красивое решение
# ls = [int(i) for i in input().split()]
# for i in set(ls):
#     if ls.count(i) > 1:
#         print(i, end=' ')

# # прикол с САПЕРом от учителей
# n, m, k = (int(i) for i in input().split())  # чтение размеров поля и числа мин
# a = [[0 for j in range(m)] for i in range(n)]  # заполнение поля нулями
# for i in range(k):
#     row, col = (int(i) - 1 for i in input().split())
#     a[row][col] = -1  # расставляем мины
# for i in range(n):
#     for j in range(m):
#         if a[i][j] == 0:  # в этой клетке мины нет, поэтому считаем число мин вокруг
#             for di in range(-1, 2):
#                 for dj in range(-1, 2):
#                     ai = i + di
#                     aj = j + dj
#                     # (ai, aj)
#                     if 0 <= ai < n and 0 <= aj < m and a[ai][aj] == -1:
#                         a[i][j] += 1
# # вывод результата
# for i in range(n):
#     for j in range(m):
#         if a[i][j] == -1:
#             print('*', end=' ')
#         elif a[i][j] == 0:
#             print('.', end=' ')
#         else:
#             print(a[i][j], end=' ')
#     print()
# # конец прикола
# suma = 0
# s = 0
# while True:
#     n = int(input())
#     suma += n
#     s += n ** 2
#     if suma == 0:
#         break
# print(s)

# n = int(input())
# suma = 0
# numbers = []
# for i in range(1, n + 1):
#     suma += i
#     for j in range(i):
#         numbers.append(i)
#     if suma >= n:
#         break
# for i in range(0, n):
#     print(numbers[i], end=' ')

# другой вариант
# n, x = int(input()), []
# for i in range(n + 1):
#     x += [i] * i
# print(*x[:n])
# print(*x)
# lst, x = [int(i) for i in input().split()], int(input())
# k = 0
# for item in range(len(lst)):
#     if x == lst[item]:
#         print(item, end=' ')
#     else:
#         k += 1
# if k == len(lst):
#     print("Отсутствует")
#
# # прикольное решение без дурацкого счётчика
# lst = [int(i) for i in input().split()]
# x = int(input())
# if not x in lst:
#     print('Отсутствует')
# else:
#     for i in range(len(lst)):
#         if lst[i] == x:
#             print(i, end=' ')ne

# matrix = []
# m = []
# while True:
#     stri = input()
#     if stri == 'end':
#         break
#     else:
#         m = [int(j) for j in stri.split()]
#         matrix.append(m)
#         m = []
# n = len(matrix)  # длина строки
# m = len(matrix[0])  # высота стоблца
# new_matrix = [[0 for j in range(m)] for i in range(n)]
# for i in range(n):
#     for j in range(m):
#         new_matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1] + \
#                            matrix[i + 1 -n][j] + matrix[i][j + 1 - m]
# for i in range(n):
#     for j in range(m):
#         print(new_matrix[i][j], end=' ')
#     print()

# n = int(input())
# matrix = [[0 for j in range(n)] for i in range(n)]
# ass = 1
# side = n
# offset = 0
# while offset < n / 2:
#     # верхняя строка
#     for i in range(side):
#         matrix[offset][offset + i] = ass
#         ass += 1
#     # правый столбец
#     for i in range(side - 1):
#         matrix[1 + offset + i][n - 1 - offset] = ass
#         ass += 1
#     # нижняя строка
#     if n / 2 - offset > 0:
#         for i in range(1, side):
#             matrix[n - 1 - offset][n - 1 - i - offset] = ass
#             ass += 1
#     # левый столбец
#     for i in range(1, side - 1):
#         matrix[n - 1 - i - offset][offset] = ass
#         ass += 1
#     side -= 2
#     offset += 1
# for i in range(n):
#     for j in range(n):
#         print(matrix[i][j], end=' ')
#     print()
#
# def f(x):
#     if x <= -2:
#         return 1 - (x + 2) ** 2
#     elif -2 < x <= 2:
#         return -x / 2
#     else:
#         return (x - 2) ** 2 + 1
#
#
# print(f(4.5))
# print(f(-4.5))
# print(f(1))
#
#
# def modify_list(l):
#     for i in range(len(l) - 1, -1, -1):
#         print(l[i], end='->')
#         if l[i] % 2 != 0:
#             print(i, 'if', end=' ')
#             l.remove(l[i])
#         else:
#             print(i, 'else', end=' ')
#             l[i] = int(l[i] / 2)
#     print()
#
#
# lst = [1, 99, 46, 58, 60, 88, 99]
# lst1 = [1, 3, 7, 9]
# modify_list(lst1)
# print(lst1)
#
# # лаконично
# def modify_list1(l):
#     l[:] = [i//2 for i in l if not i % 2]
#
#
# modify_list1(lst)
# print(lst)
# basket = {'orange', 'pear', 'peach', 'apple', 'banana'}
# for i in basket:
#     print(i, end=' ')
# def update_dictionary(d, key, value):
#     if key in d:
#         d[key] += [value]
#     elif 2 * key in d:
#         d[2 * key] += [value]
#     else:
#         d.setdefault(2 * key, [value])
#
#
# d = {}
# print(update_dictionary(d, 1, -1))  # None
# print(d)  # {2: [-1]}
# update_dictionary(d, 2, 0)
# print(d)  # {2: [-1, -2]}
# update_dictionary(d, 1, -3)
# print(d)
#
#
# # красивые решения
# def update_dictionary1(d, key, value):
#     key += key * (key not in d)
#     d[key] = d.get(key, []) + [value]
#
#
# # автор написал,что здесь присутсвует побитовый сдвиг (??)
# def update_dictionary2(d, key, value):
#     key <<= key not in d
#     d.setdefault(key, []).append(value)
#
"""
lst = [i for i in input().lower().split()]
dict = {}
for key in lst:
    dict[key] = dict.get(key, 0) + 1
#####################
    Мой изначальный говно-код: (какая красота получается с функцией "get")
    if key in dict:
        dict[key] += 1
    else:
        dict.setdefault(key, 1)
#####################
for key, value in dict.items():
    print("%s: %d" % (key, value))
"""
# # красиво
# s = input().lower().split()
# for i in set(s):
#     print(i, s.count(i))
# def f(x):
#     return x ** 2
#
#
# n = int(input())
# dicto = {}
# for i in range(0, n):
#     key = int(input())
#     if key not in dicto:
#         dicto.setdefault(key, f(key))
#         print(f(key))
#     else:
#         print(dicto[key])
# решение с лямбда-функцией как я поняла
# a = [int(input()) for i in range(int(input()))]
# b = {x: f(x) for x in set(a)}
# for i in a:
#     print(b[i])

# import webbrowser, os
# path="C:/Users"
# webbrowser.open(os.path.realpath(path))
# mass = {48, 49, 50, 51, 52, 53, 54, 55, 56, 57}
# with open("C:\\File for Stepik.txt", 'r') as filer:
#     s = filer.readline() + ' '
#     s1 = ''
#     k = 0
#     for i in range(1, len(s)):
#         if ord(s[i]) in mass:
#             k += 1
#             continue
#         else:
#             s1 += s[i - 1 - k] + s[i - 1 - k] * (int(s[i - k:i]) - 1)
#             k = 0
# with open("C:\\File for Stepik1.txt", 'w') as filer:
#     filer.write(s1)
#
# # s = 'G10l1J4G7u1l2i8D13k21' + ' '
# s = 'a1b1c1' + ' '
# s1 = ''
# k = 0
# for i in range(1, len(s)):
#     if ord(s[i]) in mass:
#         k += 1
#         continue
#     else:
#         s1 += s[i - 1 - k] + s[i - 1 - k] * (int(s[i - k:i]) - 1)
#         k = 0
# print(s1)
# with open("C:\\File for Stepik.txt", 'r') as filer:
#     s = filer.read().replace('\n','').lower().split()
#     keyList = []
#     dicto = {}
#     for item in s:
#         dicto.setdefault(item, s.count(item))
#     value_max = s.count(s[0])
#     for key, value in dicto.items():
#         if value_max < value:
#             value_max = value
#     for key, value in dicto.items():
#         if value == value_max:
#             keyList.append(key)
#     keyList.sort()
#     print(keyList[0], value_max)
#
# крутое лаконичное решение
# with open('dataset_3363_3.txt') as inf, open('MostPopularWord.txt','w') as ouf:
#     maxc = 0
#     s = inf.read().lower().strip().split()
#     s.sort()
#     for word in s:
#         counter = s.count(word)
#         if counter > maxc:
#             maxc = counter
#             result_word = word
#     ouf.write(result_word +' ' + str(maxc))
# with open("C:\\File for Stepik.txt", 'r') as filer, open("C:\\File for Stepik1.txt", 'a') as filer1:
#     mathe = []
#     physics = []
#     russian = []
#     mean = 0
#     for line in filer:
#         s = line.replace('\n', '').split(';')
#         mathe.append(float(s[1]))
#         physics.append(float(s[2]))
#         russian.append(float(s[3]))
#         for i in range(1, len(s)):
#             mean += float(s[i])
#         filer1.write(str(mean / 3))
#         filer1.write('\n')
#         mean = 0
#     for i in range(len(mathe)):
#         mean += mathe[i]
#     mathe_mean = mean / len(mathe)
#     mean = 0
#     for i in range(len(physics)):
#         mean += physics[i]
#     physics_mean = mean / len(physics)
#     mean = 0
#     for i in range(len(russian)):
#         mean += russian[i]
#     russian_mean = mean / len(russian)
#     mean = 0
#     filer1.write(str(mathe_mean))
#     filer1.write(' ')
#     filer1.write(str(physics_mean))
#     filer1.write(' ')
#     filer1.write(str(russian_mean))
#     filer1.write(' ')
#
# # аккуратное решение
# koll, a1, b1, c1 = 0, 0, 0, 0
# with open('dataset_3363_4.txt', 'r') as inf:
#     for line in inf:
#         line = line.strip().split(';')
#         a, b, c = int(line[1]), int(line[2]), int(line[3])
#         print((a+b+c)/3)
#         koll += 1
#         a1 += a
#         b1 += b
#         c1 += c
# print((a1/koll), (b1/koll), (c1/koll))
# using tuples for sorting dictionaries by value:
"""
cause = {'a':10, 'c': 22, 'b': 1}
print(sorted([(value, key) for key, value in cause.items()], reverse=True))
import math
import sys

radius = 10
print(math.pi * radius * 2)
for i in sys.argv[1:]:
    print(i, end=' ')

import requests
"""


def count(string):
    string_counts = {}
    for character in string:
        string_counts.setdefault(character, string.count(character))
    return string_counts


print(count("aa bb cccccccc"))
