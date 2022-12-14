# Дана последовательность чисел. Получить список уникальных элементов заданной последовательности,
# список повторяемых и убрать дубликаты из заданной последовательности.

# Пример:
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10] и [1, 3, 5] и [1, 2, 5, 3, 10]

from random import randint

list_1 = [randint(1, 10)for i in range(10)]

list_2, list_3 = [], []
for i in set(list_1):
    if list_1.count(i) > 1:
        list_3.append(i)
    else:
        list_2.append(i)
print(f'Изначальный список: {list_1}\n'
      f'Элементы: {list_2}\n'
      f'Дубликаты: {list_3}\n'
      f'Без дубликатов: {list(set(list_1))}')

