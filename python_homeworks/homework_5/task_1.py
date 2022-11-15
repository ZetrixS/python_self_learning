# Напишите программу, удаляющую из текста все слова, в которых присутствуют все буквы "абв".

text = 'Проверка абв условий хреньабв программы полнабвая'

def function(text):
    text = list(filter(lambda x: 'абв' not in x, text.split()))
    return " ".join(text)

text = function(text)
print(text)