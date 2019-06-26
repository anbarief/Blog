secret_word = "MACEDONIA"
secret_word_list = ["M", "A", "C", "E", "D", "O", "N", "I", "A"]
blanks = "*********"

for i in range(6):
    print("\nPUZZLE: Guess the Country!")
    print(blanks)
    guess = input("type your guess: ")
    print("your guess is " + guess)

    #Checking the guess
    if (guess == secret_word):
        blanks = guess
        input("GREAT! Puzzle Solved: " + secret_word + " (press any key to continue)")
        break
    elif (guess in secret_word_list):
        for j in range(9):
            if guess == secret_word[j]:
                blanks = blanks[0:j] + guess + blanks[j+1:]
        print(blanks)
        input("Letter guess is correct! (press any key to continue)")
        if blanks == secret_word:
            input("GREAT! Puzzle Solved: " + secret_word + " (press any key to continue)")
            break
    else:
        input("Wrong guess..try again (press any key to continue)")

if blanks != secret_word:
    print("\n\n")
    input("No More Lives: Puzzle Not Solved.. (press any key to continue)")
    
