from src.Creators.Creator import Creator
from src.Units.PacmanClass import Pacman


class PacmanCreator(Creator):
    def Create(self, pos, speed, game):
        product = Pacman()
        self.setUnitAttributes(product, game, pos, speed)
        self.setDead(product)
        return product

    def setDead(self, product):
        product.dead = False
