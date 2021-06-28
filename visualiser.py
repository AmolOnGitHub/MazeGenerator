import arcade

SIZE = 7
ROW_COUNT = SIZE * 2 + 1
COLUMN_COUNT = SIZE * 2 + 1

WIDTH = 800 // ROW_COUNT
HEIGHT = 800 // COLUMN_COUNT

MARGIN = 5

SCREEN_WIDTH = WIDTH * COLUMN_COUNT + MARGIN * 2
SCREEN_HEIGHT = WIDTH * COLUMN_COUNT + MARGIN * 2
SCREEN_TITLE = "Maze Visualiser"

arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
arcade.set_background_color(arcade.color.BLACK)
GridSpriteList = arcade.SpriteList()

def render(maze):
    for row in range(ROW_COUNT):
        for col in range(COLUMN_COUNT):
            num = maze[row][col]
            x = MARGIN + col * WIDTH + WIDTH / 2
            y = MARGIN + row * HEIGHT + HEIGHT / 2 
            
            if num == 1: color = arcade.color.BLACK
            else: color = arcade.color.WHITE
            
            #if (row, col) == currentCoord:
            #    color = arcade.color.AZURE
            
            sprite = arcade.SpriteSolidColor(WIDTH, HEIGHT, color)
            sprite.center_x = x
            sprite.center_y = y
            GridSpriteList.append(sprite)

    arcade.start_render()
    GridSpriteList.draw()
    arcade.finish_render()

arcade.run()
