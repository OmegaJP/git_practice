#python script that opens the file mbox-short and prints it out in uppercase

file = open('mbox-short.txt')
for line in file :
    nline= line.rstrip()
    print(nline.upper())
