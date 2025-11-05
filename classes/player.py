class Player:

    def __init__(self, name, location, money, property: list):
        self.name = name
        self.location = location
        self.money = money
        self.property = property

    def adding_property(self,tiel):
        self.property.append(tiel)

    def payment(self, amount):
        self.money -= amount

    def get_money(self,amount):
        self.money += amount

    def update_location(self,dices):
        self.location += dices

