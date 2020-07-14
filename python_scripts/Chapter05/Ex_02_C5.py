max = None
min = None
while True :
    value = input('Enter a number: ')
    if value == 'done' :
        break
    try :
        ival=int(value)
        if max is None:
            max=ival
        elif min is None:
            min=ival
        elif ival < min :
            min = ival
        elif ival > max :
            max = ival
        continue
    except :
        print('Invalid input!')
        continue
print('All done!')
print('maximum: ', max)
print('minimum: ', min)
