import arcade
import random
import time
SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 650
SCREEN_TITLE = "1013"
SCREEN_SPEED_X = -8
SCREEN_SPEED_Y = -4
BALL_SCALE = 0.3
RACKET_SCALE = 0.5
ROCKET_SPEED = -5
TRIES = 5
class Ball(arcade.Sprite):
    def update(self):
        if self.left < 0:
            if self.change_x < 50:
                self.change_x = -self.change_x + 0.05
            else:
                self.change_x = -self.change_x
        if self.top > SCREEN_HEIGHT:
            self.change_y = -self.change_y - 0.05
        if self.bottom < 0:
            self.change_y = -self.change_y + 0.05
        if self.right > SCREEN_WIDTH:
            self.change_x = -self.change_x - 0.05
        self.center_x += self.change_x
        self.center_y += self.change_y
class Racket(arcade.Sprite):
    def update(self):
        self.center_y += self.change_y
        self.angle = 90
        if self.top > SCREEN_HEIGHT:
            self.top = SCREEN_HEIGHT
        if self.bottom < 0:
            self.bottom = 0
class Window(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.ball = Ball("Ping pong\Неоновый круг без фона.png", BALL_SCALE)
        self.ball.change_x = SCREEN_SPEED_X
        self.ball.change_y = SCREEN_SPEED_Y
        self.racket = Racket("Ping pong\Неоновый прямоугольник без фона.png", RACKET_SCALE)
        self.racket_1 = Racket("Ping pong\Неоновый прямоугольник без фона.png", RACKET_SCALE)
        self.racket_1.color = arcade.color.AQUA
        self.racket.tries = TRIES
        self.racket_1.tries = TRIES
        self.bg = arcade.load_texture("Ping pong\Небо_4.jpg")
    def set_up(self):
        b = random.randint(1,2)
        if b == 1:
            self.ball.change_y = -self.ball.change_y
        self.racket.center_y = SCREEN_HEIGHT/2
        self.ball.center_y = SCREEN_HEIGHT/2
        self.racket.center_x = SCREEN_WIDTH/6
        self.racket_1.center_y = SCREEN_HEIGHT/2
        self.racket_1.center_x = SCREEN_WIDTH/6*5
        a = random.randint(1,2)
        if a == 1:
            self.ball.change_x = -self.ball.change_x
            self.ball.center_x = SCREEN_WIDTH/4
        else:
            self.ball.center_x = SCREEN_WIDTH/4*3
        if self.racket.tries == -1:
            self.racket.tries = TRIES
            self.racket_1.tries = TRIES
        if self.racket_1.tries == -1:
            self.racket.tries = TRIES
            self.racket_1.tries = TRIES
    def on_draw(self):
        self.clear(arcade.color.BLACK)
        arcade.draw_texture_rectangle(center_x = SCREEN_WIDTH/2, center_y= SCREEN_HEIGHT/2, height = SCREEN_HEIGHT, width = SCREEN_WIDTH, texture = self.bg)
        self.ball.draw()
        self.racket.draw()
        self.racket_1.draw()
        arcade.draw_text(f" У Оранжевого осталось {self.racket.tries} жизней.", SCREEN_WIDTH/100, SCREEN_HEIGHT/100,arcade.color.FUCHSIA, font_name ='Comic Sans MS')
        arcade.draw_text(f" У Зелёного осталось {self.racket_1.tries} жизней.", SCREEN_WIDTH/100*80, SCREEN_HEIGHT/100, arcade.color.FUCHSIA, font_name ='Comic Sans MS')
        if self.racket.tries == 0:
            arcade.draw_text(" Победил Зелёный!", SCREEN_WIDTH/3, SCREEN_HEIGHT/2,arcade.color.FUCHSIA,font_size = 50)
            to_end = time.time()
            if time.time() - to_end > 3:
                exit()
        if self.racket_1.tries == 0:
            arcade.draw_text(" Победил Оранжевый!", SCREEN_WIDTH/3, SCREEN_HEIGHT/2,arcade.color.FUCHSIA, font_size = 50)
            to_end = time.time()
            if time.time() - to_end > 3:
                exit()
    def on_update(self, delta_time):
        self.ball.update()
        self.racket.update()
        self.racket_1.update()
        flag = True
        if self.ball.left < 0:
            self.racket.tries -= 1
            self.set_up()
        if self.ball.right > SCREEN_WIDTH:
            self.racket_1.tries -= 1
            self.set_up()
        if self.ball.center_x < self.racket.right and self.ball.center_x > self.racket.left:
            if (self.ball.bottom <= self.racket.top and self.ball.top > self.racket.bottom) or (self.ball.top >= self.racket.bottom and self.ball.bottom < self.racket.bottom):
                self.ball.change_y = -self.ball.change_y
                flag = False
        if arcade.check_for_collision(self.ball,self.racket) and flag:
            self.ball.change_x = -self.ball.change_x
            if self.ball.center_x > self.racket.center_x:
                self.ball.left = self.racket.right
            else:
                self.ball.right = self.racket.left
        if self.ball.center_x < self.racket_1.right and self.ball.center_x > self.racket_1.left:
            if (self.ball.bottom <= self.racket_1.top and self.ball.top > self.racket_1.bottom) or (self.ball.top >= self.racket_1.bottom and self.ball.bottom < self.racket_1.bottom):
                self.ball.change_y = -self.ball.change_y
                flag = False
        if arcade.check_for_collision(self.ball,self.racket_1) and flag:
            self.ball.change_x = -self.ball.change_x
            if self.ball.center_x > self.racket_1.center_x:
                self.ball.left = self.racket_1.right
            else:
                self.ball.right = self.racket_1.left
    def on_key_press(self, key: int, modifiers: int):
        if key == arcade.key.W :
            self.racket.change_y = -ROCKET_SPEED
        if key == arcade.key.S:
            self.racket.change_y = ROCKET_SPEED
        if key == arcade.key.UP:
            self.racket_1.change_y = -ROCKET_SPEED
        if key == arcade.key.DOWN:
            self.racket_1.change_y = ROCKET_SPEED
    def on_key_release(self, key: int, modifiers: int):
        if key == arcade.key.W or key == arcade.key.S:
            self.racket.change_y = 0
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.racket_1.change_y = 0
window_1 = Window(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, title=SCREEN_TITLE)
window_1.set_up()
arcade.run()