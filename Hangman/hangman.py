import os
import random

def play_hangman():
    # Geting the path to the wordlist.txt file which is located in the same directory as this script
    wordlist_path = os.path.join(os.path.dirname(__file__), "wordlist.txt")

    # Opening the wordlist file and reading all words into a list
    with open(wordlist_path, "r") as file:
        words = [line.strip() for line in file]

    # List of categories included in the game
    categories = [
        "Python Core",
        "Data Structures",
        "OOP Concepts",
        "Web Development",
        "Git & DevOps",
        "AI/ML Terms",
        "Linux CLI"
    ]

    # Selection of a random word from the list for the player to guess
    word_to_guess = random.choice(words)

    # Hangman ASCII art for each stage of the game (7 stages)
    HANGMANPICS = [
        '''
         +---+
         |   |
             |
             |
             |
             |
        =========''', '''
         +---+
         |   |
         O   |
             |
             |
             |
        =========''', '''
         +---+
         |   |
         O   |
         |   |
             |
             |
        =========''', '''
         +---+
         |   |
         O   |
        /|   |
             |
             |
        =========''', '''
         +---+
         |   |
         O   |
        /|\\  |
             |
             |
        =========''', '''
         +---+
         |   |
         O   |
        /|\\  |
        /    |
             |
        =========''', '''
         +---+
         |   |
         O   |
        /|\\  |
        / \\  |
             |
        ========='''
    ]

    # Welcome message and game instructions
    print("\n Welcome to the Developer's Hangman Game! ")
    print(" Category: Tech Vocabulary\n")
    print(" Categories included in this game:")
    for cat in categories:
        print(f" - {cat}")
    print("\nStart guessing... You have 7 lives!\n")

    # Set to keep track of letters the player has guessed
    guessed_letters = set()

    # Set of letters in the word to guess
    correct_letters = set(word_to_guess)

    # Number of lives the player has (7 wrong guesses allowed)
    lives = 7

    # Main game loop runs while player still has lives
    while lives > 0:
        # Displaying the word with guessed letters shown and others as underscores
        display_word = [letter if letter in guessed_letters else '_' for letter in word_to_guess]
        print("Word: ", ' '.join(display_word))

        # Displaying the hangman picture corresponding to current lives left
        print(HANGMANPICS[7 - lives])

        # Shows remaining lives and letters guessed so far
        print(f"Lives Left: {lives}")
        print(f"Guessed Letters: {', '.join(sorted(guessed_letters))}")

        # Prompt the player to guess a letter
        guess = input("\nGuess a letter: ").lower()

        # Validate input: must be a single alphabet letter
        if not guess.isalpha() or len(guess) != 1:
            print(" Please enter a single alphabet letter!\n")
            continue

        # Checks if letter was already guessed
        if guess in guessed_letters:
            print("⚠️ You've already guessed that letter!\n")
            continue

        # Adds the guessed letter to the set
        guessed_letters.add(guess)

        # Check if the guess is correct
        if guess in correct_letters:
            print("✅ Good guess!\n")

            # Check if all letters have been guessed
            if correct_letters.issubset(guessed_letters):
                print("🎉 Congratulations! You’ve guessed the word:", word_to_guess)
                break
        else:
            # Wrong guess, reduce a life
            print("Wrong guess!\n")
            lives -= 1

    # If player runs out of lives, game over message
    else:
        print(HANGMANPICS[-1])
        print(" Game Over! The word was:", word_to_guess)

def main():
    # Main loop to allow replaying the game
    while True:
        play_hangman()
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again not in ('yes', 'y'):
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    main()
