# 4-6. Нечетные числа: воспользуйтесь третьим аргументом функции range() для создания
# списка нечетных чисел от 1 до 20. Выведите все числа в цикле for.

numbers = list(range(1, 20, 2))
print(numbers)
for i in numbers:
    print(i)