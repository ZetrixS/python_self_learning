# Задайте список из n чисел последовательности (1 + 1 / n) ** n и выведите на экран их сумму.
# Пример:
# 1 -> 2.0
# 2 -> 4.25
# 3 -> 6.62037037037037


input = int(input('Введите число: '))
input_list = []
count = 1.0
for i in range(input):
    input_list.append(count)
    count += 1

list = []
l = 0
for i in range(input):
    list.append(round((1 + 1 / input_list[l]) ** input_list[l], 2))
    l += 1

c = 0
l_1 = 0

for i in list:
    c += list[l_1]
    l_1 += 1

print(c)
