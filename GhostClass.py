import pygame
from pygame.math import Vector2
from variables import *
from map import *
import random
from UnitClass import Unit


class Ghost(Unit):
    def __init__(self, pos, speed, behaviour, color, game):
        self.game = game
        self.pos = pos
        self.speed = speed
        self.behaviour = self.get_behaviour(behaviour)
        self.color = color
        self.direction = Vector2(0, 0)
        self.stored_direction = Vector2(0, 0)
        self.actual_pos = Vector2(
            self.pos.x * CELL_SIZE + CELL_SIZE//2, self.pos.y * CELL_SIZE + CELL_SIZE//2)

    def Update(self):
        self.UpdatePos()

    def UpdatePos(self):
        if self.InCell():
            self.random_direction()
            self.direction = self.stored_direction
            self.IsMoving = self.NotOnWall()
        if self.IsMoving:
            self.actual_pos += self.direction * self.speed
        self.pos = Vector2(self.actual_pos.x//CELL_SIZE,
                           self.actual_pos.y//CELL_SIZE)

    def MoveUp(self):
        self.stored_direction = Vector2(1, 0)

    def Draw(self):
        pygame.draw.circle(self.game.gameDisplay, self.color,
                           (self.actual_pos.x, self.actual_pos.y), CELL_SIZE//2)
        pygame.draw.rect(self.game.gameDisplay, self.color, ((
            self.actual_pos.x - 11, self.actual_pos.y), (22, 11)))

    def random_direction(self):
        random.choice(self.behaviour)()

    def MoveUp(self):
        self.stored_direction = Vector2(0, -1)

    def Stay(self):
        self.stored_direction = Vector2(0, 0)

    def get_behaviour(self, type):
        match type:
            case 'Normal':
                return [self.MoveDown, self.MoveRight,
                        self.MoveUp, self.MoveLeft]
            case 'DownRight':
                return [self.MoveDown, self.MoveDown, self.MoveRight,
                        self.MoveRight, self.MoveUp, self.MoveLeft]
            case 'DownLeft':
                return [self.MoveDown, self.MoveDown, self.MoveRight,
                        self.MoveUp, self.MoveLeft, self.MoveLeft]
