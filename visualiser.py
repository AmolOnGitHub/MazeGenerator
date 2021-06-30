import arcade
import maze as mzgen
import time
import pathfinder
import colorsys

SIZE = 20
ROW_COUNT = SIZE * 2 + 1
COLUMN_COUNT = SIZE * 2 + 1

WIDTH = 800 // ROW_COUNT
HEIGHT = 800 // COLUMN_COUNT

MARGIN = 5

SCREEN_WIDTH = WIDTH * COLUMN_COUNT + MARGIN * 2
SCREEN_HEIGHT = WIDTH * COLUMN_COUNT + MARGIN * 2
SCREEN_TITLE = "Maze Visualiser"

class Window(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.BLACK)
        self.maze = mzgen.Maze(SIZE)

        self.grid_sprite_list = [arcade.SpriteList() for _ in range(ROW_COUNT)]

        self.path = [] 
        self.tempPath = []
        self.current = None

        self.maze_finished = False
        self.start_path = False
        self.path_finished = False
        self.path_found = False
        self.coloring_done = False

        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                x = MARGIN + column * WIDTH + WIDTH / 2
                y = MARGIN + row * HEIGHT + HEIGHT / 2 

                color = arcade.color.BLACK
                if column % 2 == 1 and row % 2 == 1: color = arcade.color.LIGHT_GRAY
                    
                sprite = arcade.Sprite("white.png", image_width=WIDTH, image_height=HEIGHT)
                sprite.color = color
                sprite.center_x = x
                sprite.center_y = y
                self.grid_sprite_list[row].append(sprite)

    def on_update(self, delta_time):
        # Maze Visualisation
        if self.maze.stack == []:
            self.maze_finished = True
        if self.maze.stack != []:
            self.maze.step()
            for row in range(ROW_COUNT):
                for column in range(COLUMN_COUNT):
                    num = self.maze.grid[row][column]

                    color = arcade.color.BLACK
                    if num == 0: color = arcade.color.LIGHT_GRAY
                    if (row, column) == self.maze.current:
                        color = arcade.color.BLUEBERRY

                    self.grid_sprite_list[row][column].color = color

        # Path Visualisation
        if self.maze_finished and self.start_path and not self.path_finished:
            if not self.path_found:
                destination = (SIZE * 2 - 1, SIZE * 2 - 1)
                self.path = pathfinder.findPath(self.maze.grid, destination)
                self.tempPath = self.path.copy()
                self.path_found = True
            
            if self.current is None: previous = self.tempPath[-1]
            else: previous = self.current
            self.current = self.tempPath.pop(-1)

            self.grid_sprite_list[previous[0]][previous[1]].color = (237, 47, 47)
            self.grid_sprite_list[self.current[0]][self.current[1]].color = (66, 245, 78)         

            if len(self.tempPath) == 0: self.path_finished = True
        
        # Adds gradient to path visualisation
        if self.path_finished and not self.coloring_done:
            c = 0
            l = len(self.path)
            while c < l:
                x, y = self.path[l - c - 1]
                hue = c / l
                color = colorsys.hsv_to_rgb(hue, 0.7, 0.6)
                colorRGB = tuple(round(x * 255) for x in color)
                self.grid_sprite_list[x][y].color = colorRGB
                c += 1
            self.coloring_done = True
            
    def on_draw(self):
        arcade.start_render()
        for row in self.grid_sprite_list:
            row.draw()

    def on_key_press(self, symbol, modifiers):
        if self.maze_finished and symbol == arcade.key.SPACE:
            self.start_path = True

Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
arcade.run()
