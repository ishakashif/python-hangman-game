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
    print("****************")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("****************")
def display_hint(hint):
    print(hint)
def display_answer(answer):
    pass
def main():
    answer = random.choice(words)
    hint = " ".join("_" * len(answer))
    wrong_guesses = 0# Hangman in Python
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
    print("****************")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("****************")
def display_hint(hint):
    print(" ".join(hint))
def display_answer(answer):
    print(" ".join(answer))
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
        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
    display_answer(answer)


if __name__ == "__main__":
    main()

#work


