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
def play_again():
    is_running = True
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
