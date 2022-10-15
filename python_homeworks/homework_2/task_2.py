# Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


input = int(input('Введите число: '))
list = []
count = 1
for i in range(input):
    list.append(count)
    count += 1
print(list)


def calculation(number):
    sum = 1
    for i in range(1, number):
        sum += sum*i
    return sum


l = 0
for i in list:
    list[l] = calculation(list[l])
    l += 1
print('Ваши произведения -', list)
