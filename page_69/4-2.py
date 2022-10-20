# 4-2. Животные: создайте список из трех (и более) животных, обладающих
# общей характеристикой. Используйте цикл for для вывода названий всех животных.
# • Измените программу так, чтобы вместо простого названия выводилось сообщение,
# включающее это название, например «A dog would make a great pet».
# • Добавьте в конец программы строку с описанием общего свойства. Например, можно
# вывести сообщение «Any of these animals would make a great pet!».

animals = ['cat', 'panteer', 'tiger']
for animal in animals:
    print('The ' + animal + ' is very great pet!')
print('I would like to have one of this.')
