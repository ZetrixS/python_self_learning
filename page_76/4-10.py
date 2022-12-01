# 4-10. Срезы: добавьте в конец одной из программ, написанных в этой главе, фрагмент,
# который делает следующее.
# • Выводит сообщение «The first three items in the list are:», а затем использует срез для
# вывода первых трех элементов из списка.
# • Выводит сообщение «Three items from the middle of the list are:», а затем использует
# срез для вывода первых трех элементов из середины списка.
# • Выводит сообщение «The last three items in the list are:», а затем использует срез для
# вывода последних трех элементов из списка.

countryes = ['Scotland','Norway', 'Greenland', 'Northrend', 'Outland']
print('The first three are ', countryes[:3])
print('The last three are ', countryes[-3:])
print('The middle three are ', countryes[1:4])