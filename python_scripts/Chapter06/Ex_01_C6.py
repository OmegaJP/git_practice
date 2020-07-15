#script that reads a word backwards and list each letter of the word.

word=input('Please enter word: ')
n=0
index=len(word)-1
while index > -1 :
    letter=word[index]
    print(letter)
    index=index-1
    n=n+1
print(word)
print('count: ', n)
