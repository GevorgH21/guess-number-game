import random


class GuessGameEngine:

    def __init__(self):
        self.data = []

    def magic_number_function(self):
        magic_number = random.randint(0, 10)
        selected_number = int(input("Select a number between 0 and 10 for a guessing game:"))
        if selected_number > magic_number:
            print(" Your number was {0}. The number I was thinking of was {1}. Your guess was too high. ".format(
                selected_number, magic_number))
        elif magic_number == selected_number:
            print(" Your number was {0}. The number I was thinking of was {1}. Your guess was perfect. ".format(
                selected_number, magic_number))
        else:
            print(" Your number was {0}. The number I was thinking of was {1}. Your guess was too low. ".format(
                selected_number, magic_number))
