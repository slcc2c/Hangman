def hangman(word):
    blanks = '_'*len(word)
    guesses = ''
    parts = ['head','left arm', 'right arm', 'body', 'left leg', 'right leg']
    strikes = 0
    strike = True
    game_over = False

    #start game
    print(blanks)
    while(not game_over):
        guess = input('pick a letter')
        if(guess in guesses):
            print('already guessed')
            continue
        guesses += guess
        temp_blanks = ''
        for letter, space in zip(word, blanks):
            if(letter == guess):
                strike = False
                temp_blanks += guess
            else:
                temp_blanks += space
        strikes += int(strike)
        blanks = temp_blanks
        if('_' not in blanks):
            game_over = True
            print('You won!')
            print(word)
        else:
            print(parts[strikes:])
            print(guesses)
            print(blanks)

word = input('Word?')
hangman(word)