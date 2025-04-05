import random
import time
from wordlist import *
def display_ascii_banner():
    banner = """
 _                                              
| |                                             
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/  
    """
    print("\033[1;34m" + banner + "\033[0m")  # Adding color for better visual appeal
    time.sleep(1)

def choose_difficulty():
    print("Choose difficulty level:")
    print("1. Animals")
    print("2. Fruits")
    print("3. IT Words")
    print("4. English Words")
    while True:
        choice = input("Enter choice (1/2/3/4): ")
        if choice == "1":
            return animals
        elif choice == "2":
            return fruits
        elif choice == "3":
            return it_words
        elif choice == "4":
            return english_words
        else:
            print("Invalid choice. Please select 1, 2, 3, or 4.")

def display_man(wrong_guesses):
    hangman_art = {
        0: (" +---+\n", " |   |\n", "     |\n", "     |\n", "     |\n", "     |\n"),
        1: (" +---+\n", " |   |\n", " O   |\n", "     |\n", "     |\n", "     |\n"),
        2: (" +---+\n", " |   |\n", " O   |\n", " |   |\n", "     |\n", "     |\n"),
        3: (" +---+\n", " |   |\n", " O   |\n", "/|   |\n", "     |\n", "     |\n"),
        4: (" +---+\n", " |   |\n", " O   |\n", "/|\\  |\n", "     |\n", "     |\n"),
        5: (" +---+\n", " |   |\n", " O   |\n", "/|\\  |\n", "/    |\n", "     |\n"),
        6: (" +---+\n", " |   |\n", " O   |\n", "/|\\  |\n", "/ \\  |\n", "     |\n")
    }
    print("\033[1;31m**********\033[0m")  # Adding red color for visual effect
    for line in hangman_art[wrong_guesses]:
        print("\033[1;31m" + line + "\033[0m", end="")
    print("\033[1;31m**********\033[0m")

def display_hint(hint):
    print("\033[1;33mHint:\033[0m", " ".join(hint))

def display_answer(answer):
    print("\033[1;32mAnswer:\033[0m", " ".join(answer))

def play_hangman():
    display_ascii_banner()
    print("\033[1;36mWelcome to Hangman!\033[0m")
    time.sleep(1)
    words = choose_difficulty()
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_game_running = True
    score = 0
    
    while is_game_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("\033[1;35mGuess a letter: \033[0m").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("\033[1;31mPlease enter a single letter.\033[0m")
            continue
        
        if guess in guessed_letters:
            print(f"\033[1;31mYou already guessed the letter {guess}. Try again!\033[0m")
            continue
        
        guessed_letters.add(guess)
        
        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
            score += 10  # Increase score for correct guesses
        else:
            wrong_guesses += 1
        
        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print(f"\033[1;32mCongratulations! You won! Your score: {score}\033[0m")
            is_game_running = False
        elif wrong_guesses == 6:
            display_man(wrong_guesses)
            display_answer(answer)
            print("\033[1;31mYou lost! Better luck next time.\033[0m")
            is_game_running = False

    while True:
        replay = input("Do you want to play again? (yes/no): ").lower().strip()
        if replay == "yes":
            play_hangman()
        elif replay == "no":
            print("Thanks for playing Hangman! Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    play_hangman()
