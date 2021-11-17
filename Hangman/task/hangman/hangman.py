# Hangman
# Modules ----------------------------------------------------------------------
import random


# Functions ---------------------------------------------------------------------
def give_hint():
    """
    This function will iterate over the letters in the "game_word" string to check
    if the "guess_letter" set contains the same letters as the "game_word" string.
    if it does the player has not yet guessed the correct letter in the iteration.
    :return:
    hint is a string of correctly guessed letters and "-" place holders for letters
    that have not yet been guessed correctly.
    """
    global game_word
    global guess_letters
    hint = ""
    for letter in game_word:
        if letter in guess_letters:
            hint = hint + "-"
        else:
            hint = hint + letter
    return hint


# Variables --------------------------------------------------------------------
words = 'python', 'java', 'kotlin', 'javascript'
game_word = random.choice(words)
guess_letters = set(game_word)
already_guessed = set()
playing = False

# Menu loop -------------------------------------------------------------------
print("""H A N G M A N""")
while not playing:
    response = input('Type "play" to play the game, "exit" to quit:')
    if response == "exit":
        break
    elif response == "play":
        playing = True

        # game loop ---------------------------------------------------------
        lives = 8
        while lives > 0:
            print()
            print(give_hint())
            player_guess = input(f"Input a letter: ").strip()
            if player_guess == "exit":
                playing = False
                break
            elif len(player_guess) == 1:
                if player_guess.islower() and player_guess.isalpha():
                    if player_guess in guess_letters:
                        guess_letters.remove(player_guess)
                        already_guessed.add(player_guess)
                    else:
                        if player_guess in already_guessed:
                            print("You've already guessed this letter")
                        else:
                            print("That letter doesn't appear in the word")
                            already_guessed.add(player_guess)
                            lives -= 1
                    if give_hint() == game_word:
                        print()
                        print(give_hint())
                        print("You guessed the word!")
                        break
                else:
                    print("Please enter a lowercase English letter")
            else:
                print("You should input a single letter")
        # Results
        if lives == 0:
            print("You lost!")
        elif lives > 0:
            print("You survived!")
        playing = False
