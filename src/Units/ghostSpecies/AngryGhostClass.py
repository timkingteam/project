from src.Units.ghostSpecies.FindGhostClass import FindGhost


class AngryGhost(FindGhost):
    def get_behaviour(self):
        self.stored_movement = self.direction_to_player(
            self.pos, self.game.pacman.pos) - self.pos
