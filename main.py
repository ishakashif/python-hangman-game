# Hangman in Python
import random
from functions import *
from words import *
def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter a letter: ")
        if len(guess) > 1 or not guess.isalpha():
            print("Invalid input")
            continue
        if guess in guessed_letters:
            print(f"You already guessed '{guess}'")
            continue
        guessed_letters.add(guess)
        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1
        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer.upper())
            print("YOU WIN!")
            is_running = False
            playing_again = input("Would you like to play again? (Y/N): ")
            if playing_again.upper() == 'Y':
                play_again()
            else:
                is_running = False
        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer.upper())
            print("YOU LOSE!")
            is_running = False
            playing_again = input("Would you like to play again? (Y/N): ")
            if playing_again.upper() == 'Y':
                play_again()





if __name__ == "__main__":
    main()

#works


