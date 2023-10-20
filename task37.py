month = input('enter a month: ')
if month in ('january','february','march', 'april','may'):
    print('spring')
elif month in ('june','july','August'):
    print('summer')
elif month in ('September','October','November'):
    print('fall')
elif month in ('December'):
    print('winter')
else:
    print('invalid month')
