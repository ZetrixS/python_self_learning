# 3-8. Повидать мир: вспомните хотя бы пять стран, в которых вам хотелось бы побывать.
# • Сохраните названия стран в списке. Проследите за тем, чтобы список не хранился
# в алфавитном порядке.
# • Выведите список в исходном порядке. Не беспокойтесь об оформлении списка, просто
# выведите его как обычный список Python.
# • Используйте функцию sorted() для вывода списка в алфавитном порядке без изменения списка.
# • Снова выведите список, чтобы показать, что он по-прежнему хранится в исходном
# порядке.
# • Используйте функцию sorted() для вывода списка в обратном алфавитном порядке
# без изменения порядка исходного списка.
# • Снова выведите список, чтобы показать, что исходный порядок не изменился.
# • Измените порядок элементов вызовом reverse(). Выведите список, чтобы показать,
# что элементы следуют в другом порядке.
# • Измените порядок элементов повторным вызовом reverse(). Выведите список, чтобы
# показать, что список вернулся к исходному порядку.
# • Отсортируйте список в алфавитном порядке вызовом sort(). Выведите список, чтобы
# показать, что элементы следуют в другом порядке.
# • Вызовите sort() для перестановки элементов списка в обратном алфавитном порядке.
# Выведите список, чтобы показать, что порядок элементов изменился.

from audioop import reverse


countryes = ['Scotland','Norway', 'Greenland', 'Northrend', 'Outland']
print(countryes)
print(sorted(countryes))
print(countryes)
print(sorted(countryes, reverse=True))