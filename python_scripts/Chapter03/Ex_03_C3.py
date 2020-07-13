grade=input('Enter grade please: ')
try:
    if float(grade) > 1.0 :
        print('Out of range')
    elif float(grade)  >= 0.9 :
        print( grade , 'Excellent')
    elif float(grade) >= 0.8 :
        print( grade , 'Notable')
    elif float(grade) >= 0.7 :
        print( grade , 'Good')
    elif float(grade) >= 0.6 :
        print( grade , 'Suficcient')
    elif float(grade) > 0.0 :
        print( grade , 'Insufficient')
    elif float(grade) < 0.0 :
        print('Out of range')
except:
    print('Please enter a valid number')
    quit()
