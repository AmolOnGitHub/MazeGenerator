import arcade
import maze as mzgen
import time

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

        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                x = MARGIN + column * WIDTH + WIDTH / 2
                y = MARGIN + row * HEIGHT + HEIGHT / 2 

                color = arcade.color.BLACK
                if column % 2 == 1 and row % 2 == 1: color = arcade.color.WHITE
                    
                sprite = arcade.Sprite("white.png", image_width=WIDTH, image_height=HEIGHT)
                sprite.color = color
                sprite.center_x = x
                sprite.center_y = y
                self.grid_sprite_list[row].append(sprite)

    def on_update(self, delta_time):
        if self.maze.stack != []:
            self.maze.step()
            for row in range(ROW_COUNT):
                for column in range(COLUMN_COUNT):
                    num = self.maze.grid[row][column]

                    color = arcade.color.BLACK
                    if num == 0: color = arcade.color.WHITE
                    if (row, column) == self.maze.current:
                        color = arcade.color.AZURE

                    self.grid_sprite_list[row][column].color = color

    def on_draw(self):
        arcade.start_render()
        for row in self.grid_sprite_list:
            row.draw()

Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
arcade.run()
