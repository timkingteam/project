import pygame
from pygame.math import Vector2
from src.varuables import *
from src.map import *
from src.Units.UnitClass import Unit


class Ghost(Unit):
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
