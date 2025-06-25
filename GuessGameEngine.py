import random

class GuessGameEngine:

    def __init__(self):
        self.data = []

    def magic_number_function(self, selected_number):
        magic_number = random.randint(0, 10)
        if selected_number > magic_number:
            return f"Your guess was too high. You picked {selected_number}, I had {magic_number}."
        elif selected_number == magic_number:
            return f"Perfect guess! Both were {magic_number}."
        else:
            return f"Your guess was too low. You picked {selected_number}, I had {magic_number}."

