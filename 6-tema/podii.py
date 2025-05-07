# У ящику є 10 однакових деталей, позначених номерами 
# 1,2,...,10. Навмання вилучено 6 деталей. Знайти ймовірність того, що серед вилучених деталей виявляться:

# деталь №1;
# деталі №1 та №2.

import itertools
val = [1, 2, 3, 4,5,6,7,8,9]
val1 = [1, 2, 3, 4,5,6,7,8]
com_set = itertools.combinations(val, 5)
com_set1 = itertools.combinations(val1, 4)
n=0
n1=0
for elem in com_set:
    # print(elem)
    n+=1
C59 = n
print(C59)
for elem in com_set1:
    # print(elem)
    n1+=1
C48 = n1
print(C48)
val = [1, 2, 3, 4,5,6,7,8,9,10]
com_set = itertools.combinations(val, 6)
n=0
for elem in com_set:
    # print(elem)
    n+=1
C610 = n
print(C610)
P = C59/C610
P1 = C48/C610
print(P)
print(P1)

#! скорочений варіант розв'язку

import math

# Загальна кількість способів вибрати 6 деталей із 10
C_10_6 = math.comb(10, 6)

# Кількість сприятливих випадків:
# 1. Якщо деталь №1 є (тобто обираємо ще 5 із решти 9)
C_9_5 = math.comb(9, 5)

# 2. Якщо деталі №1 і №2 є (тобто ще 4 з решти 8)
C_8_4 = math.comb(8, 4)

# Ймовірності
P = C_9_5 / C_10_6          # ймовірність, що №1 є
P1 = C_8_4 / C_10_6         # ймовірність, що №1 і №2 є

# Виведення результатів
print(f"P(№1 є) = {P}")
# print(f"P(№1 є) = {P:.3f}")
print(f"P(№1 і №2 є) = {P1}")
# print(f"P(№1 і №2 є) = {P1:.3f}")
