import pygame
import random
# from pygame.locals import *

DIRT_COLOR = (94, 66, 45)
TUNNELED_COLOR = (53, 40, 29)
GRID_COLOR = (137, 137, 137)

class Grid:
    def __init__(self, n):
        self.coords = [[0 for x in range(0,n)] for x in range(0,n)]
        self.goldX = random.randint(0, n-1)
        self.goldY = random.randint(0, n-1)
        self.pitX = random.randint(0, n-1)
        self.pitY = random.randint(0, n-1)
        self.beaconX = random.randint(0, n-1)
        self.beaconY = random.randint(0, n-1)
        self.coords[self.goldX][self.goldY] = 3
        self.coords[self.beaconX][self.beaconY] = 2
        self.coords[self.pitX][self.pitY] = 1

class Miner:
    #note that north, east, south, west are used as NWSE
    def __init__(self):
        self.x = 0
        self.y = 0
        # 1 for North, 2 for east, 3 for south, 4 for west (clockwise)
        self.front = 2

    def move(self, n):
        if self.front == 1: #north
            self.y -= 1
        elif self.front == 2: #east
            self.x -= 1
        elif self.front == 3: #south
            self.y += 1
        elif self.front == 4: #west
            self.x += 1

        if (self.y < 0 or self.y >= n or self.x < 0 or self.x >= n): #has to be greater or equal to for n because index starts at 0
            return False
        return True

    def rotate(self):
        if (self.front == 4):
            self.front = 1
        self.front += 1


    def scan(self, coordVal):
        if (coordVal == 3):
            return 'g'
        elif (coordVal == 2):
            return 'b'
        elif (coordVal == 1):
            return 'p'
        return "NULL"
