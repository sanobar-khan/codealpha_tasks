import random

def choose_word():
    words = ["python", "hangman", "developer", "programming", "challenge"]
    return random.choice(words)

def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def hangman():
    word = choose_word()
    guessed_letters = set()
    attempts = 6  # Number of incorrect guesses allowed

    print("\n🎯 Welcome to Hangman!\n")
    
    while attempts > 0:
        print("📌 Word: ", display_word(word, guessed_letters))
        print(f"🔢 Attempts left: {attempts}")
        
        guess = input("\n🔤 Guess a letter: ").lower().strip()
        
        if len(guess) != 1 or not guess.isalpha():
            print("❌ Invalid input. Please enter a single letter.\n")
            continue

        if guess in guessed_letters:
            print("⚠️ You have already guessed this letter! Try a different one.\n")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("✅ Correct guess!\n")
            if all(letter in guessed_letters for letter in word):
                print(f"🎉 Congratulations! You guessed the word: **{word.upper()}** 🎉\n")
                return
        else:
            attempts -= 1
            print("❌ Wrong guess! Try again.\n")

    print(f"💀 Game Over! The word was: **{word.upper()}**\n")

# Run the game
hangman()
