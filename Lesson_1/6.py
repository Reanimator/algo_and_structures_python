__author__ = 'Агеев Михаил Михайлович'

# 6.	Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

SYM = int(input("Введите номер буквы (от 1 до 26): \n"))
SYMBOLS = "abcdefghijklmnopqrstuvwxyz"

print(f"Ваша буква: {SYMBOLS[SYM - 1]}")
