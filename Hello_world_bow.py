import Enemies
ogr = Enemies.Enemy(8)
Hero = Enemies.Player(10)
def bow_fight (hp_i, hp_e, health_list, damage_bow_i_simple, damage_bow_i_significant, damage_bow_i_max, damage_enemy):
    import random
    import time
    while hp_i > 0 and ogr.hp_e > 0:
        coin = random.randint (1,24)
        coin_1 = random.randint(1,24)
        print(f"Вам выпало {coin}.")
        print(f"Врагу выпало {coin_1}.")
        time.sleep(1)
        if coin == 1:
            Hero.be_attacked(damage_bow_i_simple, "Вы попали в себя.")
            time.sleep(1)
        elif coin > 1 and coin < 12:
            print(" Вы промазали.")
            time.sleep(1)
        elif coin > 11 and coin < 17:
            ogr.be_attacked(damage_bow_i_simple, 'урон')
            time.sleep(1)
        elif coin > 16 and coin < 24:
            ogr.be_attacked(damage_bow_i_significant, 'значительный урон')
            time.sleep(1)
        elif coin == 24:
            ogr.be_attacked(damage_bow_i_max, "максимальный урон")
            time.sleep(1)
        if "кровотечение" in health_list:
            Hero.being_poisoned()
        if len(health_list) > 5:
            Hero.max_len_helth_list()
        if coin_1 == 1:
            ogr.be_attacked(damage_bow_i_simple,"Враг попал в самого себя.")
            time.sleep(1)
        elif coin_1 > 1 and coin_1 < 12:
            print(" Враг промазал.")
            time.sleep(1)
        elif coin_1 > 15:
            Hero.be_attacked(damage_enemy, "Враг попал в вас.")
    if hp_i > hp_e:
        print(" Вы застрелили врага.")
        if hp_i <= 0:
            print(" Но, увы, вы тоже погибли!")
    elif hp_e > hp_i:
        print(" Враг застрелил вас.")
        if hp_e <= 0:
            print(" Но вы успели смертельно ранить противника, и он тоже умер.")
    elif hp_e == hp_i:
        print(" Вы застрелили друг друга.")
    return hp_i, hp_e, health_list
Hero.hp_i, ogr.hp_e, Hero.health_list = bow_fight(Hero.hp_i, ogr.hp_e, Hero.health_list, Hero.damage_bow_i_simple, Hero.damage_bow_i_significant, Hero.damage_bow_i_max, ogr.damage_enemy)