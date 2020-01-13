__author__ = 'Агеев Михаил Михайлович'

import random

"""
4.	Написать программу, которая генерирует в указанных пользователем границах
●	случайное целое число,
●	случайное вещественное число,
●	случайный символ.
Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f',
то вводятся эти символы. Программа должна вывести на экран любой
символ алфавита от 'a' до 'f' включительно.
"""

NUM_INT_1 = int(input("Введите начало диапазона для целого числа: \n"))
NUM_INT_2 = int(input("Введите конец диапазона для целого числа: \n"))
NUM_REAL_1 = int(input("Введите начало диапазона для вещественного числа: \n"))
NUM_REAL_2 = int(input("Введите конец диапазона для вещественного числа: \n"))
SYM_1 = input("Введите начало диапазона для символов: \n")
SYM_2 = input("Введите конец диапазона для символов: \n")
SYMBOLS = "abcdefghijklmnopqrstuvwxyz"

if NUM_INT_1 < NUM_INT_2:
    print(
        f"Рандомное целое число из диапазона: {random.randint(NUM_INT_1, NUM_INT_2)}")
else:
    print(
        f"Рандомное целое число из диапазона: {random.randint(NUM_INT_2, NUM_INT_1)}")

if NUM_INT_1 < NUM_INT_2:
    print(
        f"Рандомное вещественное число из диапазона: {random.uniform(NUM_REAL_1, NUM_REAL_2)}")
else:
    print(
        f"Рандомное вещественное число из диапазона: {random.uniform(NUM_REAL_2, NUM_REAL_1)}")

NUM_SYM_1 = SYMBOLS.find(SYM_1)
NUM_SYM_2 = SYMBOLS.find(SYM_2)
if NUM_SYM_1 < NUM_SYM_2:
    print(f"Рандомный символ: {SYMBOLS[random.randint(NUM_SYM_1, NUM_SYM_2)]}")
else:
    print(f"Рандомный символ: {SYMBOLS[random.randint(NUM_SYM_2, NUM_SYM_1)]}")
