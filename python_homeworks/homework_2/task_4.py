# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

file_list = [45, 20, 4, 92, 10, 5, 79, 39, 63,
             67, 2, 52, 83, 59, 18, 41, 11, 22, 90, 3]
print(file_list)

input_1 = int(input('Введите число: '))
list = []
count = input_1 - (input_1*2)
for i in range(input_1*2+1):
    list.append(count)
    count += 1
print(list)

l = 0
k = 0
list_count = 1

if file_list[l] == k:
    list_count *= list[k]
    l += 1
    k += 1
else:
    l += 1
    k += 1
print(list_count)
