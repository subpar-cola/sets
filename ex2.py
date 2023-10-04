names = {'Joe', 'Ed', 'Fred'}
name = input('Enter a name: ')
if name in names:
    print (f'"{name}" exists in {names}')
else:
    print (f'"{name}" does not exist in {names}')
