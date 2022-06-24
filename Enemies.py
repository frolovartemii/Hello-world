import time
class Enemy:
    def __init__(self, hp):
        self.hp_e = hp
        self.damage_enemy = 2
    def be_attacked(self, enemy_attack, name_damage):
        if name_damage != "Враг попал в самого себя." and name_damage != 'Враг промазали.':
            self.hp_e -= enemy_attack
            if name_damage == "урон":
                print(f" Вы попали во врага и нанесли {name_damage}. Враг имеет {self.hp_e} очков здоровья.")
            elif name_damage == "значительный урон":
                print(f" Вы попали врагу в уязвимое место и нанесли значительный урон. Враг имеет {self.hp_e} очков здоровья.")
            elif name_damage == "максимальный урон":
                print(" Вы попали крайне точно врагу в уязвимое место и нанесли максимальный урон. Враг имеет {self.hp_e} очков здоровья.")
        elif name_damage == "Враг попал в самого себя.":
            self.hp_e -= enemy_attack
            print(" Враг попал по себе. У него осталось {self.hp_e} очков здоровья.")

class Player(Enemy):
    def __init__(self, hp):
        self.hp_i = hp
        self.damage_bow_i_simple = 3
        self.damage_bow_i_significant = 6
        self.damage_bow_i_max = 10
        self.health_list = []
    def be_attacked(self, damage_enemy, name_damage):#be_attacked(damage_enemy = ogr.damage_enemey)
        if name_damage != "Вы попали в себя.":
                self.hp_i -= damage_enemy
                print(f" Враг попал и нанёс {damage_enemy}. У вас осталось {self.hp_i} очков здоровья.")
        elif name_damage == "Вы попали в себя.":
            print(" Вместо того чтобы попасть в противника у вас получилось попасть в себя. У вас началось кровотечение, пока вы его не излечите, оно будет отбирать немного здоровья после каждого хода.")
            self.hp_i -= self.hp_i//100*5
            self.health_list.append("кровотечение")
    def being_poisoned(self):
        self.hp_i -= 1
        print(f" Вы потеряли часть здоровья из-за кровотечения.{self.hp_i}")
    def max_len_helth_list(self):
        self.hp_i = 0
        print(" Из-за обилия сильных повреждений вы умераете.")
