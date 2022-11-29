# Напишите программу вычисления арифметического выражения заданного строкой.
# Используйте операции +,-,/,*. приоритет операций стандартный.
# Добавьте возможность использования скобок, меняющих приоритет операций.


from decimal import Decimal


def calculations(input):
   
    numbers_1 = ''
    numbers_2 = ''

    for character in input:
        if character.isdigit() or character == '.':
            numbers_1 += character
        elif character == '-':
            numbers_1 += ' '+character
            numbers_2 == '+'
        elif character == ' ':
            continue
        else:
            numbers_2 += character
            numbers_1 += ' '
    return list(map(Decimal, numbers_1.split())), list(numbers_2)


def calc(numbers_1, numbers_2):
    while len(numbers_1) > 1:
        temp = 0
        prod_div = min(numbers_2.index('*')if '*' in numbers_2 else len(numbers_2),
                       numbers_2.index('/')if '/' in numbers_2 else len(numbers_2))
        add = numbers_2.index('+')if '+' in numbers_2 else len(numbers_2)
        if prod_div != len(numbers_2):
            if numbers_2[prod_div] == '*':
                temp = numbers_1[prod_div]*numbers_1[prod_div+1]
            elif numbers_2[prod_div] == '/':
                if numbers_1[prod_div+1] == 0:
                    print('Выражение не имеет решений')
                    exit()
                temp = numbers_1[prod_div]/numbers_1[prod_div+1]
            del numbers_1[prod_div]
            numbers_1[prod_div] = temp
            del numbers_2[prod_div]
        elif add != len(numbers_2):
            if numbers_2[add] == '+':
                temp = numbers_1[add]+numbers_1[add+1]
            del numbers_1[add]
            numbers_1[add] = temp
            del numbers_2[add]
    return numbers_1


input_u = input('Введите выражение: ')
numbers_1, numbers_2 = calculations(input_u)
print(calc(numbers_1,numbers_2))

