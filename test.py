import pygame, sys
from pygame import *
import random

#Initialzing 
pygame.init()

#Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()

#Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0

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