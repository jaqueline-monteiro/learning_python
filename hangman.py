def play():
    print("*********************************")
    print("***Welcome to the Hangman Game!***")
    print("*********************************")

    secret_word = "apple".upper()
    guessed_letters = ["_" for letter in secret_word]

    hanged = False
    guessed = False
    errors = 0

    print(guessed_letters)

    while (not hanged and not guessed):

        guess = input("Which letter? ")
        guess = guess.strip().upper()

        if guess in secret_word:
            index = 0
            for letter in secret_word:
                if guess == letter:
                    guessed_letters[index] = letter
                index += 1
        else:
            errors += 1

        hanged = errors == 6
        guessed = "_" not in guessed_letters
        print(guessed_letters)

    if guessed:
        print("You won!!")
    else:
        print("You lost!!")
    print("End of the game")

if __name__ == "__main__":
    play()
