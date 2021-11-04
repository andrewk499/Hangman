import random
from words import words

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def print_display(display): #displays the progress of the word being guessed
    for i in display:
        print(i, end=" ")

def hangman(): 
    word = get_valid_word(words)
    word_letters = list(word)
    letter_count = len(word_letters) #gets the number of letters 
    display = []

    for i in range(letter_count):
        display.append("_")
    

    print("Let the Hangman game begin!")
    print_display(display)

    attempt_count = 0 #tracks the number of attempts
    attempts_allowed = 6

    #run loop until the number of attempts allowed is met
    while attempt_count < attempts_allowed: 
        guess = input("\nPlease guess a letter: ").upper()
        matches = 0

        for j in range(len(word_letters)):
            if guess == word_letters[j]:
                display[j] = word_letters[j]
                matches += 1
                
        if matches > 0:
            print(f"Yay! You got {matches} letter(s)")
        else:
            attempt_count += 1
            print(f"Sorry, no letters matched. You have {attempts_allowed - attempt_count} attempts left.")

        print_display(display)

        if word_letters == display:
            print("Congratulations! You have won :)")
            return
    
    print(f"Hangman is DEAD :(. The word was {word}.")

hangman()