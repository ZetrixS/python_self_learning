guests = ['Mama', 'Ivan', 'Leonid']
print('Dear ' + guests[0] + ' you are invited to our journey!')
print('Dear ' + guests[1] + ' you are also invited to our journey!')
print('With all our regreats, we must say that '+ guests.pop() + ' cant join us.')
print(guests)
print('Hes place will be taken by Andrey.')
guests.append('Andrey')
print(guests)