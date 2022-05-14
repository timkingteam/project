import pygame
from pygame.math import Vector2
from src.variables import *
from src.map import *


class Unit:
    def __init__(self):
        self.game
        self.pos
        self.actual_pos
        self.speed
        self.movement
        self.stored_movement
        self.IsMoving

        raise NotImplementedError()

    def Update(self):
        raise NotImplementedError()

    def UpdatePos():
        raise NotImplementedError()

    def Draw():
        raise NotImplementedError()

    def MoveRight(self):
        self.stored_movement = Vector2(1, 0)

    def MoveDown(self):
        self.stored_movement = Vector2(0, 1)

    def MoveLeft(self):
        self.stored_movement = Vector2(-1, 0)

    def MoveUp(self):
        self.stored_movement = Vector2(0, -1)

    def Stay(self):
        self.stored_movement = Vector2(0, 0)

    def InCell(self):
        stay_dir = (self.movement == Vector2(0, 0))
        x_in_cell = ((self.actual_pos.x - CELL_SIZE//2) % CELL_SIZE == 0)
        x_dir = (self.movement == Vector2(1, 0)) or (
            self.movement == Vector2(-1, 0))
        y_in_cell = ((self.actual_pos.y - CELL_SIZE//2) % CELL_SIZE == 0)
        y_dir = (self.movement == Vector2(0, 1)) or (
            self.movement == Vector2(0, -1))
        return ((stay_dir or x_dir) and x_in_cell) or ((stay_dir or y_dir) and y_in_cell)

    def NotOnWall(self):
        for wall in WALLS:
            if (Vector2(self.pos + self.stored_movement) == wall):
                return False
        return True
