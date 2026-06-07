import random

words = ["apple", "mango", "grapes", "orange", "banana"]

word = random.choice(words)
guessed = []
tries = 6

while tries > 0:
    display = ""

    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "

    print(display)

    if "_" not in display:
        print("You Won!")
        break

    guess = input("Guess a letter: ")

    if guess in word:
        guessed.append(guess)
    else:
        tries -= 1
        print("Wrong guess. Tries left:", tries)

if tries == 0:
    print("You Lost! Word was:", word)
