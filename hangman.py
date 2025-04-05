# hangman personal

import random # the random module is imported to generate a random word from the list of words

# list of words
words = ["python", "java", "computer", "hacker", "painter", "artist", "musician", "writer", "dancer", "singer"]

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
    print(banner)

# dictionary of hangman art to be displayed when the player makes a wrong guess it's in a key-value pair format
hangman_art = { 0: (" +---+\n",
                     " |   |\n",
                     "     |\n",
                     "     |\n",
                     "     |\n",
                     "     |\n"),
                1: (" +---+\n",
                    " |   |\n",
                    " O   |\n",
                    "     |\n",
                    "     |\n",
                    "     |\n"),
                2: (" +---+\n",
                    " |   |\n",
                    " O   |\n",
                    " |   |\n",
                    "     |\n",
                    "     |\n"),
                3: (" +---+\n",
                    " |   |\n",
                    " O   |\n",
                    "/|   |\n",
                    "     |\n",
                    "     |\n"),
                4: (" +---+\n",
                    " |   |\n",
                    " O   |\n",
                    "/|\\  |\n",
                    "     |\n",
                    "     |\n"),
                5: (" +---+\n",
                    " |   |\n",
                    " O   |\n",
                    "/|\\  |\n",
                    "/    |\n",
                    "     |\n"),
                6: (" +---+\n",
                    " |   |\n",
                    " O   |\n",
                    "/|\\  |\n",
                    "/ \\  |\n",
                    "     |\n")
}

def display_man (wrong_guesses):

    print("**********")
    for line in hangman_art[wrong_guesses]:
        print(line, end="") # the end parameter is used to prevent the print function from adding a newline character
    print("**********")

def display_hint(hint):

    print("Hint:"," ".join(hint)) # the join method is used to join the elements of the hint list with a space in between

def display_answer(answer):
    print("Answer:"," ".join(answer))

def play_hangman():

    display_ascii_banner()
    # Initial setup
    answer = random.choice(words) # a random word is selected from the list of words
    hint = ["_"] * len(answer) 
    wrong_guesses = 0 # this variable will store the number of wrong guesses made by the player
    guessed_letters = set() # this set will store the letters that the player has guessed
    is_game_running = True # this variable is used to determine if the game is over or not
    score = 0 # this variable will store the score of the player

    while is_game_running:
       
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Guess a letter: ").lower() # the player is asked to guess a letter and the input is converted to lowercase
        
        if len(guess) != 1 or not guess.isalpha(): # this condition checks if the input is a single letter isalpha() checks if the input is an alphabet
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print(f"You already guessed the letter{guess}. Try again!")
            continue

        guessed_letters.add(guess) # the guessed letter is added to the set of guessed letters to keep track of the letters that have been guessed

        if guess in answer:
            for i in range(len(answer)): # this loop is used to check if the guessed letter is present in the answer
                if answer[i] == guess: # if the guessed letter is present in the answer, it is added to the hint list
                    hint[i] = guess # the hint list is updated with the guessed letter
            score += 10  # Increase score for correct guesses
        else:
            wrong_guesses += 1 # if the guessed letter is not present in the answer, the number of wrong guesses is incremented

        if "_" not in hint: # this condition checks if the player has guessed all the letters in the answer
            display_man(wrong_guesses)
            display_answer(answer)
            print(f"Congratulations! You won! Your score: {score}")
            is_game_running = False

        elif wrong_guesses == 6: # this condition checks if the player has made 6 wrong guesses
            display_man(wrong_guesses)
            display_answer(answer)
            print("You lost! Better luck next time.")
            is_game_running = False

if __name__ == "__main__":
    play_hangman()