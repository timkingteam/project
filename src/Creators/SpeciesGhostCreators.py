from src.Creators.GhostCreator import GhostCreator
from src.Units.ghostSpecies.RandomGhostClass import RandomGhost
from src.Units.ghostSpecies.AngryGhostClass import AngryGhost
from src.Units.ghostSpecies.NotThatAngryGhostClass import NotThatAngryGhost


class AngryGhostCreator(GhostCreator):
    def Create(self, pos, speed, color, game):
        product = AngryGhost()
        self.setGhostAttributes(product, pos, speed, color, game)
        return product


class RandomGhostCreator(GhostCreator):
    def Create(self, pos, speed, color, game):
        product = RandomGhost()
        self.setGhostAttributes(product, pos, speed, color, game)
        return product


class NotThatAngryGhostCreator(GhostCreator):
    def Create(self, pos, speed, color, game):
        product = NotThatAngryGhost()
        self.setGhostAttributes(product, pos, speed, color, game)
        return product
