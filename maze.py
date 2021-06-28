import random
import blessed

def coordNotSafe(coord, w, h):
    x = coord[0]
    y = coord[1]
    if x < 0 or x > w - 1:
        return True
    if y < 0 or y > h - 1:
        return True
    return False

def WallsNotSafe(coord, visited):
    x, y = coord
    neighbours = [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y), (x - 1, y - 1), (x + 1, y - 1), (x - 1, y + 1), (x + 1, y + 1)]
    for neighbour in neighbours:
        if neighbour in visited:
            return True
    return False

term = blessed.Terminal()

w = 7
h = 7
maze = [["░" for _ in range(w)] for _ in range(h)]

maze[0][0] = "█"
stack = [(0, 0)]
visited = [(0, 0)]

while stack != []:
    currentCoords = stack.pop()
    x, y = currentCoords
    neighbours = [(x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)]

    c = 0

    print(term.red(str(currentCoords)))

    while c < len(neighbours):
        coord = neighbours[c]
        cNS = coordNotSafe(coord, w, h)
        ciV = coord in visited
        wNS = WallsNotSafe(coord, visited[:-3])

        print(f"{term.green(str(coord))} {cNS}, {ciV}, {wNS}")
        if cNS or ciV or wNS:
            neighbours.remove(coord)
        else: c += 1
        
    if len(neighbours) == 0: continue
    else:
        stack.append(currentCoords)
        new = random.choice(neighbours)
        maze[new[0]][new[1]] = "█"
        stack.append(new)
        visited.append(new)

    for line in maze:
        print("".join(line))

print("terminated")
