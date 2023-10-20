temperature=int(input('enter a temp: '))
if temperature >=100:
    print('boiling')
elif(temperature>=32 and temperature<=99):
    print('liquid')
else:
    print('freezing')