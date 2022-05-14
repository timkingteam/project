import pygame
from pygame.math import Vector2
from src.varuables import *
from src.map import *
import random
from src.UnitClass import Unit


class Ghost(Unit):
    def __init__(self, pos, speed, behaviour, color, game):
        self.game = game
        self.pos = pos
        self.actual_pos = Vector2(
            self.pos.x * CELL_SIZE + CELL_SIZE//2, self.pos.y * CELL_SIZE + CELL_SIZE//2)
        self.speed = speed
        self.movement = Vector2(0, 0)
        self.stored_movement = Vector2(0, 0)
        self.IsMoving = True
        self.behaviour = self.get_behaviour(behaviour)
        self.color = color

    def Update(self):
        self.UpdatePos()

    def UpdatePos(self):
        if self.InCell():
            self.random_movement()
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

    def random_movement(self):
        random.choice(self.behaviour)()

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
