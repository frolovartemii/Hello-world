def bow_fight(hp_i, hp_e, damage_enemy, health_list, damage_bow_i_simple, damage_bow_i_significant, damage_bow_i_max):
    import random
    coin = random.randint (1,24)
    print(coin)
    while hp_i != 0 or hp_e != 0:
        if coin == 1:
            print("Вместо того чтобы попасть в противника у вас получилось попасть себе в ногу. Вы двигаетесь гораздо медленнее пока не излечите рану.")
            hp_i -= damage_enemy
            health_list.append("кровотечение")
        elif coin > 1 and coin < 12:
            print("Вы промазали.")
        elif coin > 11 and coin < 17:
            print("Вы попали и нанесли урон.")
            hp_e -= damage_bow_i_simple
        elif coin > 16 and coin < 24:
            print("Вы попали и нанесли значительный урон.")
            hp_e -= damage_bow_i_significant
        elif coin == 24:
            print("Неужели? Вам выпал максимум? Тогда вы попали и нанесли максимальный урон своим оружием.")
            hp_e -= damage_bow_i_max
        if "кровотечение" in health_list:
            hp_i -= hp_i//100*5
        if len(health_list) > 5:
            hp_i = 0
    return hp_i, hp_e, damage_enemy, health_list, damage_bow_i_simple, damage_bow_i_significant, damage_bow_i_max

# num = 5
# def add(num):
#     num+=5
#     return num
# print(num)
# num=add(num)
# print(num)
