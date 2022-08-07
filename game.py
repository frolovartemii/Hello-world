import arcade
HEIGHT = 800
WIDTH = 1200
TITLE = "Egg_eater"
SNAKE_CRAWLING = 5
class Egg(arcade.Sprite):
    pass
class Snake(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        if self.right >= WIDTH + 50:
            self.right = WIDTH + 50
        if self.left <= 0:
            self.left = 0
class Fallen_egg(arcade.Sprite):
    pass
class Window(arcade.Window):
    def __init__(self, width,height,title):
        super().__init__(width,height,title)
        self.bg = arcade.load_texture("Egg_eater\фон.jpg")
        self.snake = Snake("Egg_eater\Змей.png", 0.5)
    def set_up(self):
        self.snake.center_x = WIDTH/2
        self.snake.center_y = 0
    def on_draw(self):
        arcade.draw_texture_rectangle(center_x=WIDTH/2, center_y=HEIGHT/2, height=HEIGHT, width=WIDTH, texture= self.bg)
        self.snake.draw()
    def on_update(self, delta_time):
        self.snake.update()
    def on_key_press(self, key: int, modifiers: int):
        if key == arcade.key.D:
            self.snake.change_x = SNAKE_CRAWLING
        if key == arcade.key.A:
            self.snake.change_x = -SNAKE_CRAWLING
    def on_key_release(self, key: int, modifiers: int):
        if key == arcade.key.D or key == arcade.key.A:
            self.snake.change_x = 0
Kruk = Window(width = WIDTH, height=  HEIGHT,title =  TITLE)
Kruk.set_up()
arcade.run()