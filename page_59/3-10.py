# 3-10. Все функции: придумайте информацию, которую можно было бы хранить в списке.
# Например, создайте список гор, рек, стран, городов, языков… словом, чего угодно. 
# Напишите программу, которая создает список элементов, а затем вызывает каждую функцию,
# упоминавшуюся в этой главе, хотя бы один раз.

wishes = ['health', 'wealth', 'immortality']
print(wishes)
print(sorted(wishes))
print(wishes)
print(sorted(wishes, reverse=True))
wishes.reverse()
print(wishes)
wishes.reverse()
print(wishes)
wishes.sort()
print(wishes)
wishes.sort(reverse=True)
print(wishes)
print(len(wishes))
wishes.append('strength')
print(wishes)
