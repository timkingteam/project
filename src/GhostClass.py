import pygame
from pygame.math import Vector2
from src.varuables import *
from src.map import *
from src.UnitClass import Unit


class Ghost(Unit):
    def __init__(self, pos, speed, color, game):
        self.game = game
        self.pos = pos
        self.actual_pos = Vector2(
            self.pos.x * CELL_SIZE + CELL_SIZE//2, self.pos.y * CELL_SIZE + CELL_SIZE//2)
        self.speed = speed
        self.movement = Vector2(0, 0)
        self.stored_movement = Vector2(0, 0)
        self.IsMoving = True
        self.color = color

    def Update(self):
        self.UpdatePos()

    def UpdatePos(self):
        if self.InCell():
            self.get_behaviour()
            self.movement = self.stored_movement
            self.IsMoving = self.NotOnWall()
        if self.IsMoving:
            self.actual_pos += self.movement * self.speed
        self.pos = Vector2(self.actual_pos.x//CELL_SIZE,
                           self.actual_pos.y//CELL_SIZE)

    def Draw(self):
        pygame.draw.circle(self.game.gameDisplay, self.color,
                           (self.actual_pos.x, self.actual_pos.y), CELL_SIZE//2)
        pygame.draw.rect(self.game.gameDisplay, self.color, ((
            self.actual_pos.x - 11, self.actual_pos.y), (22, 11)))

    def get_behaviour(self):
        raise NotImplementedError
