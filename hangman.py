def play():
    print("*********************************")
    print("Welcome to Hangman!")
    print("*********************************")

    secret_word = "banana"
    guessed_letters = ["_", "_", "_", "_", "_", "_"]

    hanged = False
    guessed = False

    print(guessed_letters)

    while(not hanged and not guessed):

        guess = input("Which letter? ")
        guess = guess.strip()

        index = 0
        for letter in secret_word:
            if(guess.upper() == letter.upper()):
                guessed_letters[index] = letter
            index = index + 1

        print(guessed_letters)

    print("End of the game")

if(__name__ == "__main__"):
    play()
