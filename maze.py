import random

def makeMaze(size):
    actSize = size * 2 + 1
    maze = []
    maze.append([1 for _ in range(actSize)])
    for _ in range(size):
        l = [1]
        for _ in range(size):
            l.append(0)
            l.append(1)
        maze.append(l)
        maze.append([1 for _ in range(actSize)])
    
    return maze

def printMaze(maze):
    for line in maze:
        for char in line:
            if char == 1:
                print("⬛", end = "")
            else: print("⬜", end = "")
        print()
    
def conv(coords):
    x = coords[0] * 2 + 1
    y = coords[1] * 2 + 1
    return (x, y)

def coordNotSafe(coord, w, h):
    x = coord[0]
    y = coord[1]
    if x < 0 or x > w - 1:
        return True
    if y < 0 or y > h - 1:
        return True
    return False

size = 5

maze = makeMaze(size)
stack = [(0, 0)]
visited = [(0, 0)]

while stack != []:
    currentCoords = stack.pop()
    x, y = currentCoords
    neighbours = [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]

    c = 0
    while c < len(neighbours):
        coord = neighbours[c]
        if coordNotSafe(coord, size, size) or coord in visited:
            neighbours.remove(coord)
        else: c += 1

    if len(neighbours) == 0: pass
    else:
        stack.append(currentCoords)

        new = random.choice(neighbours)
        newC = conv(new)
        curC = conv(currentCoords)
        wallX = int((newC[0] + curC[0]) / 2)
        wallY = int((newC[1] + curC[1]) / 2)

        maze[wallX][wallY] = 0
        stack.append(new)
        visited.append(new)

printMaze(maze)
