from classes.data import tiles_data
from classes.player import Player

class Board:

    def __init__(self, data: tiles_data):
        self.data = data

    def position_on_the_board(self,player: Player):
        if player.location > 40:
            player.location = player.location % 40
            player.money += 200
