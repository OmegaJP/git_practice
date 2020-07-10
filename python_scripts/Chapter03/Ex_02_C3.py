hours= input('Enter the working hours: ')
rate=input('Enter pay rate: ')
try
if float(hours) > 40 :
    pay= float(hours)*float(rate)*1.5
else :
    pay= float(hours)*float(rate)
print('Your pay is of: ', pay)
except
print('Please enter a correct number')
quit()
