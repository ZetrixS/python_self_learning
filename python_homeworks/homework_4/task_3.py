# 3) Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся
# элементов исходной последовательности.

list = list(map(int, input("Введите числа через пробел: ").split()))

print(f"Вы ввели: {list}")

list_2 = []
[list_2.append(i) for i in list if i not in list_2]

list_2.sort()

print(f"Неповторяющиеся числа - {list_2}")