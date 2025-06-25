import random

class GuessGameEngine:

    def __init__(self):
        self.data = []

    def magic_number_function(self, selected_number):
        magic_number = random.randint(0, 10)
        if selected_number > magic_number:
            print(f"Your number was {selected_number}. The number I was thinking of was {magic_number}. Your guess was too high.")
        elif magic_number == selected_number:
            print(f"Your number was {selected_number}. The number I was thinking of was {magic_number}. Your guess was perfect.")
        else:
            print(f"Your number was {selected_number}. The number I was thinking of was {magic_number}. Your guess was too low.")

