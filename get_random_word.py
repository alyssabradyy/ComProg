word = "awesome"
guessed = "_" *len(word)
guessed = list(guessed)
lstGuessed = []
letter = input("guess letter: ")
while True:
    if letter in lstGuessed:
        letter = ''
        print("Already guessed!")
    elif letter in word:
        index = word.index(letter)
        guessed[index] = letter
        word[index] = '_'
    else:
        print(''.join(guessed))
        if letter != '':
            lstGuessed.append(letter)
        letter = input("guess letter: ")
    
    if '_' not in guessed:
        print("You won!")
        break