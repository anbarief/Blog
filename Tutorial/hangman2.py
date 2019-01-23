secretWords = ["SAMOA", "ZIMBABWE", "JAPAN", "SCOTLAND", "MACEDONIA"]
blanks = ["∗∗∗∗∗", "∗∗∗∗∗∗∗∗", "∗∗∗∗∗", "∗∗∗∗∗∗∗∗", "∗∗∗∗∗∗∗∗∗"]
totalScore = []

for i in range(5):

    puzzleWord = secretWords[i]
    puzzleBlanks = blanks[i]

    for j in range(6):

        print("\nPUZZLE " + str(i+1) + " Guess the Country!")
        print(puzzleBlanks)
        guess = input("type your guess: ")
        print("your guess is " + guess)

        #Checking the guess
        if (guess == puzzleWord):

            puzzleBlanks = guess
            input("GREAT! Puzzle Solved: " + puzzleWord + " (press any key to continue)")
            break

        elif (guess in list(puzzleWord)):

            for k in range(len(puzzleWord)):
                if guess == puzzleWord[k]:
                    puzzleBlanks = puzzleBlanks[0:k] + guess + puzzleBlanks[k+1:]

            print(puzzleBlanks)
            input("Guess is correct! (press any key to continue)")

            if puzzleBlanks == puzzleWord:

                input("GREAT! Puzzle Solved: " + puzzleWord + " (press any key to continue)")
                break

        else:

            input("Wrong guess..try again (press any key to continue)")

    if puzzleBlanks == puzzleWord:

        scoreList = [puzzleWord, 6 - (j)]
        totalScore.append( scoreList )

    else:

        input("No More Lives: Puzzle Not Solved.. (press any key to continue)")
        scoreList = [puzzleBlanks, 0]
        totalScore.append( scoreList )

    print("\n\n")

for i in range(5):

    print(totalScore[i][0] + ", score: " + str(totalScore[i][1]))
