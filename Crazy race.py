import arcade
import random
HEIGHT = 700
WIDTH = 700
TITLE = "Безумные гонки"
CAR_SCALE = 0.6
CAR_SPEED_X = 6
CAR_SPEED_Y = 6
class Let(arcade.Sprite):
    def __init__(self, texture:arcade.Texture, scale: int):
        super().__init__(texture, scale)
        self.angle = 180
        self.change_y = 5
        self.center_y = HEIGHT + 100
        self.center_x = self.get_random_x()
    def get_random_x(self):
        self.list = {1: int(HEIGHT/6-30), 2: int(HEIGHT/6*2- 30), 3: int(HEIGHT/6*3- 60), 4: int(HEIGHT/6*4 - 70), 5: int(HEIGHT/6*5 + 30), 6: int(HEIGHT - 90)}
        a = random.randint(1,6)
        self.center_x = self.list[a]
        return self.center_x
    def update(self):
        self.center_y -= self.change_y
        if self.top <= 0:
            self.bottom = HEIGHT
            self.change_y = self.change_y + 0.2
            self.center_x = self.get_random_x()
class Car(arcade.Sprite):
    def update(self):
        self.center_y += self.change_y
        self.center_x += self.change_x
        if self.bottom <= 0:
            self.bottom = 0
        if self.top >= HEIGHT:
            self.top = HEIGHT
        if self.right >= WIDTH:
            self.right = WIDTH
        if self.left <= 0:
            self.left = 0
class Window(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.bg = arcade.load_texture("Crazy race\Трасса_2.jpg")
        self.car_1 = Car("Crazy race\car_3.png", CAR_SCALE)
        self.car_2 = Let("Crazy race\car_4.png", CAR_SCALE)
        self.car_3 = Let("Crazy race\car_5.png", CAR_SCALE)
        self.let = Let("Crazy race\Бочка.png", CAR_SCALE)
        self.let = Let("Crazy race\Бочка.png", CAR_SCALE)
        self.list = {1: HEIGHT/6, 2: HEIGHT/6*2, 3: HEIGHT/6*3, 4: HEIGHT/6*4, 5: HEIGHT/6*5, 6: HEIGHT-50}
    def set_up(self):
        self.car_1.center_x = WIDTH/5*2
        self.car_1.center_y = HEIGHT/5
    def on_draw(self):
        self.clear(arcade.color.FALU_RED)
        arcade.draw_texture_rectangle(center_x = WIDTH/2, center_y= HEIGHT/2, height = HEIGHT, width = WIDTH, texture = self.bg)
        self.car_1.draw()
        self.car_2.draw()
        self.car_3.draw()
    def on_update(self, delta_time):
        self.car_1.update()
        self.car_2.update()
        self.car_3.update()
        if self.car_2.center_x == self.car_3.center_x:
            self.car_3.center_x = self.car_3.get_random_x()
    def on_key_press(self, key: int, modifiers: int):
        if key == arcade.key.W:
            self.car_1.change_y = CAR_SPEED_Y
        if key == arcade.key.S:
            self.car_1.change_y = -CAR_SPEED_Y
        if key == arcade.key.D:
            self.car_1.angle = -20
            self.car_1.change_x = CAR_SPEED_X
        if key == arcade.key.A:
            self.car_1.angle = 20
            self.car_1.change_x = -CAR_SPEED_X
    def on_key_release(self, key: int, modifiers: int):
        if key == arcade.key.W or key == arcade.key.S:
            self.car_1.change_y = 0
        if key == arcade.key.D or key == arcade.key.A:
            self.car_1.change_x = 0
            self.car_1.angle = 0
Kruk = Window(WIDTH, HEIGHT,TITLE)
Kruk.set_up()
arcade.run()