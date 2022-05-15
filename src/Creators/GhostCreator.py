from src.Creators.Creator import Creator
from src.Units.ghostSpecies.RandomGhostClass import RandomGhost
from src.Units.ghostSpecies.AngryGhostClass import AngryGhost
from src.Units.ghostSpecies.NotThatAngryGhostClass import NotThatAngryGhost


class GhostCreator(Creator):
    def Create(self, behaviour, pos, speed, color, game):
        match behaviour:
            case 'Angry':
                product = AngryGhost()
            case 'Random':
                product = RandomGhost()
            case 'NotThatAngry':
                product = NotThatAngryGhost()
        self.setGame(product, game)
        self.setPos(product, pos)
        self.setMovement(product, speed)
        self.setColor(product, color)
        return product

    def setColor(self, product, color):
        product.color = color
