secret_word = ["MACEDONIA", "SINGAPORE"]
blanks = ["********", "*********"]
lives = 5

def replace(secret_word, blanks, letter):
    
    for i in range(len(secret_word)):
        if letter == secret_word[i]:
            blanks = blanks[0:i] + letter + blanks[i+1:]

    return blanks

def guess():
    
    answer = input("type your guess: ")
    print("your guess is " + answer + "!")

    return answer

def guess_result(secret_word, guess, blanks):

    if guess == secret_word:

        blanks = guess
        print(blanks)
        input("Your guess is correct! puzzle solved\n(press any key to continue)")

        return blanks

    elif (guess in list(secret_word)):
        
        blanks = replace(secret_word, blanks, guess)
        print(blanks)
        input("Your letter guess is correct!\n(press any key to continue)")

        return blanks

    else:

        print(blanks)
        input("Incorrect guess!\n(press any key to continue)")

        return blanks

def playgame(secret_word, blanks):

    print(blanks)
    
    for i in range(lives):
        player_guess = guess()
        blanks = guess_result(secret_word, player_guess, blanks)
        if (blanks == secret_word):
            input("-----PUZZLE SOLVED-----")
            break

    if (blanks != secret_word):
        input("-----NO MORE LIVES-----\ngame over")


#######################################################################


for i in range(2):
    print("\nPUZZLE " + str(i+1) + ": Guess the Country!")
    playgame(blanks = blanks[i], secret_word = secret_word[i])
