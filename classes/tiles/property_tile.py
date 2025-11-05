from classes.tiles.tile import Tile
from classes.data import tiles_data
from classes.player import Player

class PropertyTile(Tile):


    def __init__(self,data:tiles_data):
        self.data = data

    def property(self):
        print(f"name: {tiles_data}")