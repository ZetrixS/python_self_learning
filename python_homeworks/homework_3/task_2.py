# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.

list = [2, 3, 4, 5, 6]
list_2 = []

massive_count = 0
i = 0
s = len(list)

while (massive_count < len(list) / 2):

    list_2.append(list[i] * list[s-1])
    i += 1
    s -= 1
    massive_count += 1

print(list_2)
