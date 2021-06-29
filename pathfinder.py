import maze as mzgen
import math

class PriorityQueue(object):
    def __init__(self):
        self.queue = []
  
    def iter(self):
        return self.queue

    def isEmpty(self):
        return len(self.queue) == 0
  
    def insert(self, data):
        self.queue.append(data)
  
    def delete(self):
        minF = 0
        for i in range(1, len(self.queue)):
            if self.queue[i].f < self.queue[minF].f:
                minF = i

        item = self.queue[minF]
        self.queue.remove(item)
        return item

    def edit(self, node, newNode):
        index = self.queue.index(node)
        self.queue[index] = newNode

class Node():
    def __init__(self, parent = None, position = None, destination = None):
        self.parent = parent
        self.position = position

        if parent is None:
            self.destination = destination
        else: self.destination = parent.destination

        self.g = 0
        if parent is not None:
            self.g = parent.g + 1

        self.h = hS(self.destination, self.position)
        self.f = self.g + self.h

    def getNeighbours(self):
        x, y = self.position
        neighbours = [
            Node(self, (x + 1, y), None),
            Node(self, (x - 1, y), None),
            Node(self, (x, y + 1), None),
            Node(self, (x, y - 1), None),
        ]
        return neighbours

def printMaze(maze):
    for line in maze:
        for char in line:
            if char == 0: print("⬜", end = "")
            elif char == 1: print("⬛", end = "")
            elif char == 2: print("🟥", end = "")
            elif char == 3: print("🟩", end = "")
        print()

def hS(destination, convCoord):
    x1, y1 = destination
    x2, y2 = convCoord
    return math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

def findPath(maze, destination):
    open = PriorityQueue()
    open.insert(Node(None, (1, 1), destination))
    closed = []

    while not open.isEmpty():
        current = open.delete()

        if current.position == destination:
            break
        else:
            closed.append(current)
            ns = current.getNeighbours()

            # Deletes any neighbours that are on a black square
            c = 0
            while c < len(ns):
                x, y = ns[c].position
                if maze[x][y] == 1: ns.pop(c)
                else: c += 1

            for n in ns:
                for node in open.iter():
                    if n.position == node.position and n.g < node.g:
                        open.edit(node, n)

                inClosed = False
                for node in closed:
                    if node.position == n.position:
                        inClosed = True

                if not inClosed:
                    open.insert(n)

    path = []
    node = current
    while node.position != (1, 1):
        path.append(node.position)
        node = node.parent
    return path
