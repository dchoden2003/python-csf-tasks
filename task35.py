day = str(input('enter a day: '))
if day in ("Monday",'Tuesday','Wednesday','Thursday'):
 print('weekdays')
elif day in ('Friday'):
 print('TGIF')

elif day in ('saturday' or day =='sunday'):
 print('weekend')
else:
 print('invalid input')