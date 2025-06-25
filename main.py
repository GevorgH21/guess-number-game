import os
from GuessGameEngine import GuessGameEngine

class Main:
    guessEngine = GuessGameEngine()

    if os.environ.get("CI_MODE") == "true":
        selected = 5  # automatic guess for CI
        print(f"Auto-selected number in CI: {selected}")
    else:
        selected = int(input("Select a number between 0 and 10 for a guessing game: "))

    guessEngine.magic_number_function(selected)

