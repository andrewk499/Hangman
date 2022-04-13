import random
from words import words


def get_valid_word(words):
    word = random.choice(words)
    while "-" in word or " " in word:
        word = random.choice(words)

    return word.upper()


def print_display(display):  # displays the progress of the word being guessed
    for i in display:
        print(i, end=" ")


def get_guess():
    guess = input("\nPlease guess a letter: ").upper()
    while guess.isalpha() == False or len(guess) != 1:
        guess = input("FOOL! I said A LETTER. Enter a letter, clown: ").upper()

    return guess


def hangman():
    word = get_valid_word(words)
    word_letters = list(word)
    letter_count = len(word_letters)  # gets the number of letters
    display = []
    used_letter = set()  # keeps of all letters that have been previously guess.

    for i in range(letter_count):
        display.append("_")

    print("Let the Hangman game begin!")
    print_display(display)

    attempt_count = 0  # tracks the number of attempts
    attempts_allowed = 6

    # run loop until the number of attempts allowed is met
    while attempt_count < attempts_allowed:
        guess = get_guess()
        while (
            guess in used_letter
        ):  # checks to make sure letter has not been previously guessed
            print(f"Sorry, you have already guessed the letter {guess}")
            guess = get_guess()

        used_letter.add(guess)  # add the new letter to the set

        matches = 0

        for j in range(len(word_letters)):
            if guess == word_letters[j]:
                display[j] = word_letters[j]
                matches += 1

        if matches > 0:
            print(f"Yay! You got {matches} letter(s)")
        else:
            attempt_count += 1
            print(
                f"Sorry, no letters matched. You have {attempts_allowed - attempt_count} attempt(s) left."
            )

        print_display(display)

        if word_letters == display:
            print("Congratulations! You have won :)")
            return

    print(f"Hangman is DEAD :(. The word was {word}.")


hangman()
