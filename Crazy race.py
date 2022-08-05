import arcade
import random
import math
import time
HEIGHT = 700
WIDTH = 700
TITLE = "Безумные гонки"
CAR_SCALE = 0.6
CAR_SPEED_X = 8
CAR_SPEED_Y = 8
BARREL_SPEED = 4
LIFE = 1


class Let(arcade.Sprite):
    def __init__(self, texture: arcade.Texture, scale: int):
        super().__init__(texture, scale)
        self.angle = 180
        self.change_y = 5
        self.center_y = HEIGHT + random.randint(0, HEIGHT)
        self.center_x = self.get_random_x()
    def get_random_x(self):
        self.list = {1: math.ceil(HEIGHT/6-30), 2: math.ceil(HEIGHT/6*2 - 30), 3: math.ceil(
            HEIGHT/6*3 - 60), 4: math.ceil(HEIGHT/6*4 - 70), 5: math.ceil(HEIGHT/6*5 + 30), 6: math.ceil(HEIGHT - 90)}
        a = random.randint(1, 6)
        self.center_x = self.list[a]
        return self.center_x
    def update(self):
        self.center_y -= self.change_y
        if self.top <= 0:
            self.bottom = HEIGHT + random.randint(0, HEIGHT)
            self.change_y = self.change_y + 0.1
            self.center_x = self.get_random_x()
class Let_2(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        if self.right >= WIDTH:
            self.change_x = self.change_x + 0.1
            self.center_x = -WIDTH - 300


class Boom(arcade.Sprite):
    pass


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
        self.game = LIFE
        self.boom = True
        self.start_time = time.time()
        self.bg = arcade.load_texture("Crazy race\Трасса_2.jpg")
        self.car_1 = Car("Crazy race\car_3.png", CAR_SCALE)
        self.car_2 = Let("Crazy race\car_4.png", CAR_SCALE)
        self.car_3 = Let("Crazy race\car_5.png", CAR_SCALE)
        self.car_4 = Let('Crazy race\car_7.png', CAR_SCALE)
        self.car_5 = Let("Crazy race\car_9.png", CAR_SCALE)
        self.cars = [self.car_2, self.car_3, self.car_4, self.car_5]
        self.let = Let_2("Crazy race\Бочка_2.png", CAR_SCALE/2)
        self.let_2 = Let_2("Crazy race\Бочка_2.png", CAR_SCALE/2)
        self.exploision = Boom("Crazy race\Взрыв_1.png", CAR_SCALE*1.5)
        self.lets = [self.let, self.let_2]
        self.list = {1: HEIGHT/6, 2: HEIGHT/6*2, 3: HEIGHT /
                     6*3, 4: HEIGHT/6*4, 5: HEIGHT/6*5, 6: HEIGHT-50}
        self.let.change_x = BARREL_SPEED
        self.let_2.change_x = BARREL_SPEED

    def set_up(self):
        self.car_1.center_x = WIDTH/5*2
        self.car_1.center_y = HEIGHT/5
        self.let.center_x = -WIDTH - 300
        self.let.center_y = HEIGHT/3
        self.let_2.center_x = -WIDTH - 300
        self.let_2.center_y = HEIGHT/3*2

    def on_draw(self):
        self.clear(arcade.color.FALU_RED)
        arcade.draw_texture_rectangle(
            center_x=WIDTH/2, center_y=HEIGHT/2, height=HEIGHT, width=WIDTH, texture=self.bg)
        self.car_1.draw()
        self.car_2.draw()
        self.car_3.draw()
        self.car_4.draw()
        self.car_5.draw()
        self.let.draw()
        self.let_2.draw()
        arcade.draw_text(f'Время:{int(time.time()-self.start_time)}', 20, HEIGHT-20,
                         arcade.color.GAMBOGE, font_size=20, font_name='Comic Sans MS')
        if self.game == False:
            self.exploision.draw()
            arcade.draw_text("Увы, ты погиб!", WIDTH/4, HEIGHT/2,
                             arcade.color.GAMBOGE, font_size=50, font_name='Comic Sans MS')
        if self.boom == False:
            self.exploision.draw()
            if time.time() - self.boom_time > 1:
                self.boom = True

    def on_update(self, delta_time):
        if self.game:
            self.car_1.update()
            self.car_2.update()
            self.car_3.update()
            self.car_4.update()
            self.car_5.update()
            self.let.update()
            self.let_2.update()
            for car in self.cars:
                for let in self.lets:
                    if arcade.check_for_collision(self.car_1, car):
                        self.exploision.center_x = self.car_1.center_x
                        self.exploision.center_y = self.car_1.center_y
                        self.game = False
                    elif arcade.check_for_collision(self.car_1, let):
                        self.exploision.center_x = self.car_1.center_x
                        self.exploision.center_y = self.car_1.center_y
                        self.game = False
                    elif arcade.check_for_collision(car, let):
                        self.exploision.center_x = car.center_x
                        self.exploision.center_y = car.center_y
                        self.boom = False
                        self.boom_time = time.time()
                        car.center_y = HEIGHT + 300
                        let.center_x = -WIDTH - 300
        else:
            time.sleep(3)
            exit()
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
Kruk = Window(WIDTH, HEIGHT, TITLE)
Kruk.set_up()
arcade.run()