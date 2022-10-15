# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
# для всех значений предикат.

# ¬ -  NOT, !,~, НЕ, отрицание, инверсия
# ⋁ - OR, |, ИЛИ, логическое сложение, дизъюнкция
# ⋀ - AND, &, И, логическое умножение, конъюнкция

# not (X or Y or Z) = not X and not Y and not Z

x = int(input('Введите число x: '))
y = int(input('Введите число y: '))
z = int(input('Введите число z: '))

a = not (x or y or z)
b = not x and not y and not z
result = a == b
if result == True:
    print('Утверждение истинно')
else:
    print('Утверждение ложно')
