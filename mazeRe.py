def makeMaze(w, h):
    actW = w * 2 + 1
    maze = []
    maze.append([1 for _ in range(actW)])
    for _ in range(h):
        l = [1]
        for _ in range(w):
            l.append(0)
            l.append(1)
        maze.append(l)
        maze.append([1 for _ in range(actW)])
    
    return maze

def printMaze(maze):
    for line in maze:
        for char in line:
            if char == 1:
                print("⬛", end = "")
            else: print("⬜", end = "")
        print()
    
maze = makeMaze(5, 5)
printMaze(maze)
