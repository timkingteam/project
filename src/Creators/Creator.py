from pygame.math import Vector2
from src.varuables import *


class Creator:
    def Create():
        raise NotImplementedError

    def setMovement(self, product, speed):
        product.movement = Vector2(0, 0)
        product.stored_movement = Vector2(0, 0)
        product.IsMoving = True
        product.speed = speed
        product.IsMoving = True

    def setPos(self, product, pos):
        product.pos = pos
        product.actual_pos = Vector2(
            product.pos.x * CELL_SIZE + CELL_SIZE//2, product.pos.y * CELL_SIZE + CELL_SIZE//2)

    def setGame(self, product, game):
        product.game = game
