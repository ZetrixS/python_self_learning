# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка,
# стоящих на нечётной позиции.

list = [1, 2, 3, 4, 5,6]
l = 0
count = 0

for i in list:
    if l % 2 != 0:
        count += i
    l += 1

print(count)