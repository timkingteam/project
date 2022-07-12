import random
from src.Units.GhostClass import Ghost


class RandomGhost(Ghost):
    def get_behaviour(self):
        variants = [self.MoveDown, self.MoveRight,
                    self.MoveUp, self.MoveLeft]
        random.choice(variants)()
