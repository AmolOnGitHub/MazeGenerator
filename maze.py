import random
import time

def makeMaze(size):
    actW = size * 2 + 1
    maze = []
    maze.append([1 for _ in range(actW)])
    for _ in range(size):
        l = [1]
        for _ in range(size):
            l.append(0)
            l.append(1)
        maze.append(l)
        maze.append([1 for _ in range(actW)])
    
    return maze
    
def conv(coords):
    x = coords[0] * 2 + 1
    y = coords[1] * 2 + 1
    return (x, y)

def coordNotSafe(coord, size):
    x = coord[0]
    y = coord[1]
    if x < 0 or x > size - 1:
        return True
    if y < 0 or y > size - 1:
        return True
    return False

class Maze:
    def __init__(self, size):
        self.grid = makeMaze(size)
        self.size = size
        self.stack = [(0, 0)]
        self.visited = [(0, 0)]
        self.current = (1, 1)
        self.counter = 0
    
    def step(self):
        self.counter += 1
        currentCoord = self.stack.pop()
        self.current = conv(currentCoord)
        x, y = currentCoord
        neighbours = [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]
        c = 0
        
        while c < len(neighbours):
            coord = neighbours[c]
            if coordNotSafe(coord, self.size) or coord in self.visited:
                neighbours.remove(coord)
            else: c += 1
        
        if len(neighbours) != 0:
            self.stack.append(currentCoord)

            new = random.choice(neighbours)
            newC = conv(new)
            curC = conv(currentCoord)

            wallX = int((newC[0] + curC[0]) / 2)
            wallY = int((newC[1] + curC[1]) / 2)

            self.grid[wallX][wallY] = 0
            self.stack.append(new)
            self.visited.append(new) 

    def printMaze(self):
        for line in self.grid:
            for char in line:
                if char == 1:
                    print("⬛", end = "")
                else: print("⬜", end = "")
            print()
