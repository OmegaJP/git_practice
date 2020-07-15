word=input('Please enter word: ')
index=len(word)-1
while index < -1 :
    letter=word[index]
    print(letter)
    index=index-1
print(word)
