guests = ['Mama', 'Ivan', 'Leonid']
print(guests)
print('Our journey is becoming bigger.')
print('Luba, ' + 'Andrey, ' + 'Olga ' + 'will join us also.')
guests.insert(0, 'Luba')
guests.insert(2, 'Andrey')
guests.append('Olga')
print(guests)
print('Its very funny, but we only have two places left.')
print(guests.pop() + ' goodby!')
print(guests.pop() + ' goodby!')
print(guests.pop() + ' goodby!')
print(guests.pop() + ' goodby!')
del guests[0]
del guests[0]
print(guests)