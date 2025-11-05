from random import randrange


class Dice:
    @staticmethod
    def roll_the_dice():
        dice1 = randrange(1, 7)
        dice2 = randrange(1, 7)
        print(f"(dice 1 = {dice1}, dice 2 = {dice2})")
        print("sum dices: ",dice1 + dice2)
