# Напишите программу, которая принимает на вход координаты двух точек
#  и находит расстояние между ними в 2D пространстве.

import math
a_1 = float(input('Введите значение A1: '))
a_2 = float(input('Введите значение A2: '))
b_1 = float(input('Введите значение B1: '))
b_2 = float(input('Введите значение B2: '))

distance = math.sqrt(math.pow(b_1 - a_1, 2) +
                     math.pow(b_2 - a_2, 2) * 1.0)
print(round(distance, 3))
