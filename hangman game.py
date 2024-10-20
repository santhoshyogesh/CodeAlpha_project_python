import random

def hangman():
    words = ["python", "hangman", "programming", "challenge", "codeofalpha"]
    word = random.choice(words)
    guessed = "_" * len(word)
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    print("Welcome to Hangman!")
    print("You have {} incorrect guesses allowed.".format(max_incorrect_guesses))

    while incorrect_guesses < max_incorrect_guesses and "_" in guessed:
        print("\nCurrent word: ", " ".join(guessed))
        print("Guessed letters: ", " ".join(guessed_letters))
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Good guess!")
            guessed = "".join([guess if word[i] == guess else guessed[i] for i in range(len(word))])
        else:
            incorrect_guesses += 1
            print("Incorrect guess. You have {} guesses left.".format(max_incorrect_guesses - incorrect_guesses))

    if "_" not in guessed:
        print("\nCongratulations! You guessed the word: {}".format(word))
    else:
        print("\nGame Over! The word was: {}".format(word))

if __name__ == "__main__":
    hangman()
