import random
from src.ghostSpecies.FindGhostClass import FindGhost


class NotThatAngryGhost(FindGhost):
    def get_behaviour(self):
        if random.choice([True, False]):
            variants = [self.MoveDown, self.MoveRight,
                        self.MoveUp, self.MoveLeft]
            random.choice(variants)()
        else:
            self.stored_movement = self.direction_to_player(
                self.pos, self.game.pacman.pos) - self.pos
