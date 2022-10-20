# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

input = int(input('Введите число для получения последовательности фибоначчи: '))


def fibonacci(n):
    list = []
    a, b = 1, 1
    for i in range(n):
        list.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range(n+1):
        list.insert(0, a)
        a, b = b, a - b
    return list


print(fibonacci(input))
