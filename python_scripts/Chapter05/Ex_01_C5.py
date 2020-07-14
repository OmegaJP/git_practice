num = 0
tot = 0.0
while True :
    value = input('Enter a number: ')
    if value == 'done':
        break
    try:
        fvalue = float(value)
        num=num+1
        tot=fvalue+tot
        continue
    except:
        print('Invalid Input.')
        continue

print('All done!')
ave= tot/num
print(num, ave)
