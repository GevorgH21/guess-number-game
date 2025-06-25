from GuessGameEngine import GuessGameEngine

if __name__ == "__main__":
    guessEngine = GuessGameEngine()
    try:
        selected = int(input("Select a number between 0 and 10 for a guessing game: "))
        result = guessEngine.magic_number_function(selected)
        print(result)
    except ValueError:
        print("Please enter a valid number.")

