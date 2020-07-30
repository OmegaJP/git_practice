#Python script that reads through a file and search for a value and determines the average of the number

file = open('mbox-short.txt')
num= 0
count= 0
for line in file:
    if line.startswith('X-DSPAM-Confidence:'):
        index=line.find(':')
        slice=line[index+1:]
        num=num+float(slice)
        count=count+1
        average= num/count
print('X-DSPAM-Average: ', average)
