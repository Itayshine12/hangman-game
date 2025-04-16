import random
from colorama import init, Fore

init(autoreset=True)

CATEGORIES = {
    "Animals": [
        "zebra", "rabbit", "lion", "tiger", "elephant", "giraffe", "bear", "dog", "cat", "kangaroo"
    ],
    "Food": [
        "pizza", "burger", "salad", "steak", "sushi", "banana", "cherry", "cheese", "cookie", "grape"
    ],
    "Tech": [
        "keyboard", "computer", "internet", "python", "screen", "laptop", "server", "router", "mouse", "monitor"
    ]
}

HANGMAN_PICS = [
    '''
     +---+
         |
         |
         |
        ===''', '''
     +---+
     O   |
         |
         |
        ===''', '''
     +---+
     O   |
     |   |
         |
        ===''', '''
     +---+
     O   |
    /|   |
         |
        ===''', '''
     +---+
     O   |
    /|\\  |
         |
        ===''', '''
     +---+
     O   |
    /|\\  |
    /    |
        ===''', '''
     +---+
     O   |
    /|\\  |
    / \\  |
        ==='''
]

def choose_mode():
    print("\nChoose game mode:")
    print("1. Single Player (random word from category)")
    print("2. Two Players (one sets the word, the other guesses)")
    while True:
        choice = input("Enter 1 or 2: ").strip()
        if choice in ['1', '2']:
            return int(choice)
        print(Fore.YELLOW + "Invalid choice. Please enter 1 or 2.")

def choose_category():
    print("\n📂 Choose a category:")
    for idx, cat in enumerate(CATEGORIES, 1):
        print(f"{idx}. {cat}")
    while True:
        choice = input("Enter category number: ").strip()
        if choice.isdigit() and 1 <= int(choice) <= len(CATEGORIES):
            category = list(CATEGORIES.keys())[int(choice) - 1]
            return random.choice(CATEGORIES[category]), category
        print(Fore.YELLOW + "Invalid selection. Try again.")

def display_board(word, guessed, attempts):
    print("\n" + Fore.CYAN + "=" * 40)
    print(Fore.YELLOW + HANGMAN_PICS[attempts])
    print(Fore.CYAN + "Word: ", end='')
    print(" ".join([letter if letter in guessed else "_" for letter in word]))
    print(Fore.CYAN + "Guessed Letters: " + Fore.MAGENTA + " ".join(sorted(guessed)))
    print(Fore.CYAN + "=" * 40)

def get_word_from_player():
    print(Fore.BLUE + "\n🧑‍🤝‍🧑 Player 1: Please enter a secret word (letters only):")
    while True:
        word = input("Word: ").strip().lower()
        if word.isalpha():
            print("\n" * 50)  # Hide the word
            return word
        print(Fore.YELLOW + "Only letters allowed. Try again.")

def play_game():
    score = 0

    while True:
        mode = choose_mode()

        if mode == 1:
            word, category = choose_category()
            print(Fore.GREEN + f"\n🎮 Starting game in category: {category}")
        else:
            word = get_word_from_player()
            print(Fore.GREEN + "\n🎮 Player 2: Time to guess the word!")

        guessed = set()
        attempts = 0
        max_attempts = len(HANGMAN_PICS) - 1

        while attempts < max_attempts:
            display_board(word, guessed, attempts)
            guess = input("🔤 Guess a letter: ").strip().lower()

            if len(guess) != 1 or not guess.isalpha():
                print(Fore.YELLOW + "⚠️  Enter a valid single letter.")
                continue
            if guess in guessed:
                print(Fore.YELLOW + "⛔ You already guessed that.")
                continue

            guessed.add(guess)

            if guess not in word:
                print(Fore.RED + "❌ Wrong guess!")
                attempts += 1
            else:
                print(Fore.GREEN + "✅ Correct!")
                score += 5

            if all(letter in guessed for letter in word):
                display_board(word, guessed, attempts)
                print(Fore.GREEN + f"\n🎉 You WON! The word was: {word}")
                print(Fore.CYAN + f"🏆 Score: {score}")
                break
        else:
            display_board(word, guessed, attempts)
            print(Fore.RED + f"\n💀 You lost! The word was: {word}")
            print(Fore.CYAN + f"🎯 Final Score: {score}")

        again = input("\n🔁 Play again? (Y/N): ").strip().lower()
        if again != 'y':
            print(Fore.BLUE + "\n👋 Thanks for playing Hangman! See you next time!\n")
            break

if __name__ == "__main__":
    play_game()

input("Press Enter to exit...")
