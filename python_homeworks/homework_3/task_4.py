# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

input = int(input('Введите число: '))

list = []

while input != 0:
    list.append(input % 2)
    input //= 2
list.reverse()


for i in list:
    print(i, end='')
