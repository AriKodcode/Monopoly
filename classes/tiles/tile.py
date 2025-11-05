from abc import ABC, abstractmethod
from classes.player import Player
from classes.data import tiles_data


class Tile(ABC):
    @abstractmethod
    def tile(self, player:Player):
        if tiles_data[player.location] in player.property:
            return f"you need to pay rent: {tiles_data[player.location]["rent"]}"
        else:
            return f"the property is available to buy. the price is {tiles_data[player.location]["price"]}"
