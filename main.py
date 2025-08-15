# Hangman in Python
import random
words = ("apple", "orange", "banana", "coconut", "pineapple")

#dictionary of key: ()
hangman_art = {0:("   ",
                  "   ",
                  "   "),
               1:(" ○ ",
                  "   ",
                  "   "),
               2:(" ○ ",
                  " ︳ "),
               3:(" ○ ",
                  "/︳ ",
                  "   "),
               4:(" ○ ",
                  "/︳\\",
                  "   "),
               5:(" ○ ",
                  "/︳\\",
                  "/  "),
               6:(" ○ ",
                  "/︳\\",
                  "/ \\")}

def display_man(wrong_guesses):
    pass
def display_hint(hint):
    pass
def display_answer(answer):
    pass
def main():
    answer = random.choice(words)
    hint = " ".join("_" * len(answer))
    print(hint)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter a letter: ")
    display_answer(answer)


if __name__ == "__main__":
    main()


