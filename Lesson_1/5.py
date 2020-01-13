__author__ = 'Агеев Михаил Михайлович'

#5.	Пользователь вводит две буквы. Определить, на каких местах
# алфавита они стоят, и сколько между ними находится букв.

SYM_1 = input("Введите первую букву: \n")
SYM_2 = input("Введите вторую букву: \n")
SYMBOLS = "abcdefghijklmnopqrstuvwxyz"

NUM_SYM_1 = SYMBOLS.find(SYM_1)
print(f"Первая буква стоит на {NUM_SYM_1 + 1} месте.")
NUM_SYM_2 = SYMBOLS.find(SYM_2)
print(f"Первая буква стоит на {NUM_SYM_2 + 1} месте.")
if NUM_SYM_1 > NUM_SYM_2:
    print(f"Между ними {NUM_SYM_1 - NUM_SYM_2 - 1} букв")
else:
    print(f"Между ними {NUM_SYM_2 - NUM_SYM_1 - 1} букв")
