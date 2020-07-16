#Script used to take a word or phrase and count the inputted letter inside the word or phrase

def count_letters():
    word=input('enter word: ')
    x=input('count which letter ?: ')
    count=0
    index=0
    for letter in word :
        if x == word[index] :
            count=count+1
        index = index + 1
    print('word has', count , x)
count_letters()
