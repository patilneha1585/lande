import random

# List of 5 predefined words
words = ["apple", "tiger", "house", "snake", "plant"]

# Choose a random word
word = random.choice(words)
guessed_word = ["_"] * len(word)
attempts = 6
guessed_letters = []

print("🎮 Welcome to Hangman!")
print("Guess the word, one letter at a time.")
print("You have 6 incorrect guesses.\n")

while attempts > 0:
    print("Word:", " ".join(guessed_word))
    print("Incorrect attempts remaining:", attempts)
    print("Guessed letters:", guessed_letters)

    guess = input("\nEnter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter a single alphabet letter.")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Correct guess!")
        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        print("❌ Incorrect guess!")
        attempts -= 1

    # Check if word is fully guessed
    if "_" not in guessed_word:
        print("\n🎉 Congratulations! You guessed the word:", word)
        break

# If player runs out of attempts
if attempts == 0:
    print("\n💀 Game Over! The word was:", word)
