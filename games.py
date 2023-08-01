import hangman
import guessing

print("*********************************")
print("Choose your game!")
print("*********************************")

print("(1) Hangman (2) Guessing")
print("*********************************")
game = int(input("Which game? "))

if game == 1:
    print("*********************************")
    print("Playing Hangman")
    hangman.play()
elif game == 2:
    print("*********************************")
    print("Playing Guessing")
    guessing.play()
