import random

from templates import HANGMAN_FULL, BODY_PARTS
from utils import single_letter_choice, generate_hangman_picture


print("WELCOME TO HANGMAN!")
print("Play easy or hard round? (e/h)")

choice = " "
while choice not in "eh":  # prompt user to choose "easy" or "hard"
    choice = single_letter_choice(">> ")

# The word lists below were sourced from:
# https://eslgrammar.org/list-of-nouns/

if choice == "e":
    with open("words/EASY_NOUNS.txt") as f:
        words = f.read().splitlines()
else:
    with open("words/HARD_NOUNS.txt") as f:
        words = f.read().splitlines()

MAX_GUESSES = len(BODY_PARTS)  # maximum number of guesses user can make
word = random.choice(words)  # randomly select a word
guessed_letters = set()  # set of the letters user has already guessed
found_letters = set()  # set of the letters in the word the user has found
guess_count = 0  # how many guesses the user has used
dead = False  # did the user end alive or dead?
message = None  # message to be shown on the next screen

while not dead:
    picture = generate_hangman_picture(guess_count)
    # generates hangman image based on current number of guesses taken
    print(picture + "\n")
    if message:
        print(message + "\n")

    word_template = "".join(l if l in found_letters else "_" for l in word)
    # replaces unguessed letters with underscores

    print("WORD: " + word_template)
    guess = single_letter_choice("Enter your guess >> ").lower()
    while guess in guessed_letters:
        # loop until user guesses letter that has not already been guessed
        guess = single_letter_choice("(already guessed) >> ").lower()

    guessed_letters.add(guess)  # log guess

    if guess in word:
        found_letters.add(guess)  # log found letter
        message = f"Letter \"{guess}\" was found!"
        if all(l in found_letters for l in word):
            # if all letters are found, break out of loop
            break
    else:
        message = "Oh no! That letter was not found."
        guess_count += 1  # increment guess count
        if guess_count >= MAX_GUESSES:
            # user has exceeded maximum guesses (hangman is complete)
            dead = True

    print("\n" * 20)

print("\n----------\n")

if dead:
    print(HANGMAN_FULL + "\n")
    print(f"YOU LOST! The word was: {word}")

else:
    print(f"CONGRATULATIONS! You found the word. ({word})")
