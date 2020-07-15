#Script runs a program that asks numeric values and returns the number of integers and the average of those integers

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
