from templates import HANGMAN_TEMPLATE, BODY_PARTS


def single_letter_choice(prompt: str):
    choice = ""
    while len(choice) != 1 or not choice.isalpha():
        # continually prompt until user inputs a single alphabetical letter
        choice = input(prompt)

    return choice


def generate_hangman_picture(guess_count: int):
    picture = str(HANGMAN_TEMPLATE)
    for i in range(guess_count):
        # replace all numbers with associated body parts
        picture = picture.replace(str(i), BODY_PARTS[i])
    for i in range(guess_count, len(BODY_PARTS)):
        # replace every remaining number with a blank space
        picture = picture.replace(str(i), " ")

    return picture
