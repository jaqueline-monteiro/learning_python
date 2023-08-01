def play():
    print("*********************************")
    print("Welcome to Hangman!")
    print("*********************************")

    secret_word = "banana"

    hanged = False
    guessed = False

    while not hanged and not guessed:
        print("*********************************")
        guess = input("Guess a letter: ")
        guess = guess.strip()
        print("*********************************")
        print("Playing...")

        index = 0
        for letter in secret_word:
            if guess.upper() == letter.upper():
                print("*********************************")
                print("Found the letter {} at position {}".format(letter, index))
            index += 1
    print("End of the game")

if __name__ == "__main__":
    play()
