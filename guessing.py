import random

def play():
    print("*********************************")
    print("Welcome to the Guessing Game!")
    print("*********************************")

    secret_number = random.randrange(1, 101)
    total_attempts = 0
    points = 1000

    print("What's the difficulty level?")
    print("*********************************")
    print("(1) Easy (2) Medium (3) Hard")
    print("*********************************")
    level = int(input("Choose the level: "))

    if level == 1:
        total_attempts = 20
    elif level == 2:
        total_attempts = 10
    else:
        total_attempts = 5

    for round in range(1, total_attempts + 1):
        print("*********************************")
        print("Attempt {} of {}".format(round, total_attempts))
        
        print("*********************************")
        guess_str = input("Enter a number between 1 and 100: ")
        print("*********************************")
        print("You entered:", guess_str)
        guess = int(guess_str)

        if guess < 1 or guess > 100:
            print("*********************************")
            print("You must enter a number between 1 and 100!")
            continue

        correct = guess == secret_number
        higher = guess > secret_number
        lower = guess < secret_number

        if correct:
            print("*********************************")
            print("You guessed it and scored {} points!".format(points))
            break
        else:
            if higher:
                print("*********************************")
                print("You missed! Your guess was higher than the secret number.")
            elif lower:
                print("*********************************")
                print("You missed! Your guess was lower than the secret number.")
            points_lost = abs(secret_number - guess)
            points -= points_lost
    
    print("*********************************")
    print("End of the game")

if __name__ == "__main__":
    play()
