import random



class Grid:
    #param n SIZE OF GRID
    #param gold LOCATION OF GOLD (x,y)
    #param beacons ARRAY TUPLE COORDS OF BEACONS [(x,y),(x,y)]
    #param pits ARRAY TUPLE COORDS OF PITS      [(x,y),(x,y)]
    def __init__(self, n, gold, beacons, pits):
        # index starts at 1,1 for beacons and pits
        self.n = n
        self.coords = [[None for x in range(0,n)] for x in range(0,n)]
        self.goldX = gold[0]-1
        self.goldY = gold[1]-1
        self.coords[gold[0]-1][gold[1]-1] = 'G'
        self.beacons = beacons
        self.pits = pits

        for pit in pits:
            self.coords[pit[0]-1][pit[1]-1] = 'B'

        for beacon in self.beacons:
            distance = 0
            # check if beacon is near gold, saved in array
            if (beacon[0]-1 == self.goldX or beacon[1]-1 == self.goldY):
                distance = (abs(beacon[0]-1 - self.goldX), abs(beacon[1]-1 - self.goldY))  [beacon[0]-1 == self.goldX]    
            
            self.coords[beacon[0]-1][beacon[1]-1] = distance

            # check if pit is in the way of the beacon
            for pit in self.pits:
                if (pit[0] == beacon[0] and abs(beacon[1] - pit[1]) <= distance): # if the pit is on the same row and within the distance between the beacon and the gold
                    self.coords[beacon[0]-1][beacon[1]-1] = 0
                elif (pit[1] == beacon[1] and abs(beacon[0] - pit[0]) <= distance): # same but column
                    self.coords[beacon[0]-1][beacon[1]-1] = 0
                    
        
class Miner:
    #note that north, east, south, west are used as NWSE
    def __init__(self):
        self.x = 0
        self.y = 0
        # 1 for North, 2 for east, 3 for south, 4 for west (clockwise)
        self.front = 2
        self.rotateCtr = 0
        self.scanCtr = 0
        self.moveCtr = 0

    #param grid whole grid object
    def move(self, grid):
        self.moveCtr += 1

        #MOVE NORTH
        if self.front == 1: 
            if (self.y != 0):
                self.y -= 1

        #MOVE EAST
        elif self.front == 2: 
            if (self.x != grid.n):
                self.x += 1

        #MOVE SOUTH
        elif self.front == 3:
            if (self.y != grid.n):
                self.y += 1

        #MOVE WEST
        elif self.front == 4: 
            if (self.x != 0):
                self.x -= 1

        #has to be greater or equal to for n because index starts at 0
        if (self.y < 0 or self.y >= grid.n or self.x < 0 or self.x >= grid.n): 
            return False
        return True

    #ROTATE FUNCTION
    def rotate(self):
        self.rotateCtr+= 1

        self.front += 1
        if (self.front == 5):
            self.front = 1

    #SCANS THE ONE GRID AHEAD OF THE MINER
    def scan(self, grid):
        self.scanCtr += 1
        coordVal = 'NULL'

        #SCAN NORTH
        if (self.front == 1):
            if (self.x == 0):
                coordVal = "OUT OF BOUNDS"
            else:
                coordVal = grid.coords[self.x-1][self.y]
            print("NORTH")

        #SCAN EAST       
        elif (self.front == 2):
            if (self.y == grid.n):
                coordVal = "OUT OF BOUNDS"
            else:
                coordVal = grid.coords[self.x][self.y+1]
            print("EAST")
        #SCAN SOUTH
        elif (self.front == 3):
            if (self.x == grid.n):
                coordVal = "OUT OF BOUNDS"
            else:
                coordVal = grid.coords[self.x+1][self.y]
            print("SOUTH")
        #SCAN WEST
        elif (self.front == 4):
            if (self.y == 0):
                coordVal = "OUT OF BOUNDS"
            else:
                coordVal = grid.coords[self.x][self.y-1]
            print("WEST")
        #????
        if isinstance(coordVal, int):
            return 'B'
        return coordVal


class RandomMiner(Miner):
    def action(self, grid):
        choice = random.randint(0,2)
        if (choice == 0):
            self.move(grid)
        elif (choice == 1):
            self.scan(grid)
        elif (choice == 2):
            self.rotate()

class SmartMiner(Miner):

    def __init__(self):
        self.scanned_pits = []
        self.scanned_beacons = []
        self.prev = []

    def action(self, grid):
        self.scan(grid[self.x][self.y])
        self.rotate()
        pass

