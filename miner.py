import random

# from pygame.locals import *


DIRT_COLOR = (94, 66, 45)
TUNNELED_COLOR = (53, 40, 29)
GRID_COLOR = (137, 137, 137)

class Grid:
    def __init__(self, n, gold, beacons, pits):
        # 3 is a pot of gold, 2 is a beacon, 1 is a pit
        self.coords = [[0 for x in range(0,n)] for x in range(0,n)]
        self.goldX = gold[0]-1
        self.goldY = gold[1]-1
        self.coords[gold[0]-1][gold[1]-1] = 3
        self.beacons = beacons
        self.pits = pits
        for beacon in beacons:
            self.coords[beacon[0]-1][beacon[1]-1] = 2
        for pit in pits:
            self.coords[pit[0]-1][pit[1]-1] = 1
        
        

class Miner:
    #note that north, east, south, west are used as NWSE
    def __init__(self):
        self.x = 0
        self.y = 0
        # 1 for North, 2 for east, 3 for south, 4 for west (clockwise)
        self.front = 2
        self.scanned_pits = []
        self.scanned_beacons = []
        self.prev = []        

    def move(self, n):
        # add edge detection
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
        # add edge detection
        if (coordVal == 3):
            return 'g'
        elif (coordVal == 2):
            return 'b'
        elif (coordVal == 1):
            return 'p'
        return "NULL"

class SmartMiner(Miner):
    def action(self, grid):
        pass

class RandomMiner():
    def action(self, grid):
        pass