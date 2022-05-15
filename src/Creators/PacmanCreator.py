from src.Creators.Creator import Creator
from src.Units.PacmanClass import Pacman


class PacmanCreator(Creator):
    def Create(self, pos, speed, game):
        product = Pacman()
        self.setGame(product, game)
        self.setPos(product, pos)
        self.setMovement(product, speed)
        self.setDead(product)
        return product

    def setDead(self, product):
        product.dead = False
