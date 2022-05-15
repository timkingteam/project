from src.Creators.Creator import Creator
from src.Units.ghostSpecies.RandomGhostClass import RandomGhost
from src.Units.ghostSpecies.AngryGhostClass import AngryGhost
from src.Units.ghostSpecies.NotThatAngryGhostClass import NotThatAngryGhost


class GhostCreator(Creator):
    def setGhostAttributes(self, product, pos, speed, color, game):
        self.setUnitAttributes(product, game, pos, speed)
        self.setColor(product, color)

    def setColor(self, product, color):
        product.color = color
