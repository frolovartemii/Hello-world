import arcade
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
SCREEN_TITLE = "1013"
SCREEN_SPEED_X = -8
SCREEN_SPEED_Y = -4
BALL_SCALE = 0.025
RACKET_SCALE = 0.3
ROCKET_SPEED = -5
class Ball(arcade.Sprite):
    def update(self):
        if self.left < 0:
            if self.change_x < 50:
                self.change_x = -self.change_x + 0.1
            else:
                self.change_x = -self.change_x
        if self.top > SCREEN_HEIGHT:
            self.change_y = -self.change_y - 0.1
        if self.bottom < 0:
            self.change_y = -self.change_y + 0.1
        if self.right > SCREEN_WIDTH:
            self.change_x = -self.change_x - 0.1
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
        self.ball = Ball("ping pong\photo.png", BALL_SCALE)
        self.ball.change_x = SCREEN_SPEED_X
        self.ball.change_y = SCREEN_SPEED_Y
        self.racket = Racket("ping pong\photo_1.png", RACKET_SCALE)
    def set_up(self):
        self.ball.center_x = SCREEN_WIDTH/2
        self.ball.center_y = SCREEN_HEIGHT/2
        self.racket.center_y = SCREEN_HEIGHT/2
        self.racket.center_x = SCREEN_WIDTH/6
    def on_draw(self):
        self.clear(arcade.color.GOLD)
        self.ball.draw()
        self.racket.draw()
    def on_update(self, delta_time):
        self.ball.update()
        self.racket.update()
        if arcade.check_for_collision(self.ball,self.racket):
            self.ball.change_x = -self.ball.change_x
    def on_key_press(self, key: int, modifiers: int):
        if key == arcade.key.W :
            self.racket.change_y = -ROCKET_SPEED
        if key == arcade.key.S:
            self.racket.change_y = ROCKET_SPEED
    def on_key_release(self, key: int, modifiers: int):
        if key == arcade.key.W or key == arcade.key.S:
            self.racket.change_y = 0
window_1 = Window(width=SCREEN_WIDTH, height=SCREEN_HEIGHT, title=SCREEN_TITLE)
window_1.set_up()
arcade.run()
