import pygame
from pygame.math import Vector2
from src.varuables import *
from src.map import *
from src.Units.UnitClass import Unit


class Pacman(Unit):

    def Update(self):
        self.UpdatePos()
        self.EatCoin()

    def Draw(self):
        pygame.draw.circle(self.game.gameDisplay, YELLOW,
                           (self.actual_pos.x, self.actual_pos.y), CELL_SIZE//2)
        pygame.draw.polygon(self.game.gameDisplay, BLACK, ((self.actual_pos.x, self.actual_pos.y), (
            self.actual_pos.x + 10, self.actual_pos.y + 5), (self.actual_pos.x + 10, self.actual_pos.y - 5)))

    def UpdatePos(self):
        if self.InCell():
            self.movement = self.stored_movement
            self.IsMoving = self.NotOnWall()
        if self.IsMoving:
            self.actual_pos += self.movement * self.speed
        self.pos = Vector2(self.actual_pos.x//CELL_SIZE,
                           self.actual_pos.y//CELL_SIZE)

    def Die(self):
        self.dead = True

    def EatCoin(self):
        MAP[int(self.pos.y)][int(self.pos.x)] = 2
