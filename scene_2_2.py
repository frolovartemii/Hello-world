from Controllers_2 import *
def intro(alarm, Bandits_3, bandits_leader, Cook, Hostler, Messenger, cooking_time):
    print(" Вы подходите к костру, но держитесь на отдаление, чтобы вас не заметили.")
    if alarm == True:
        print(" Так как поднята тревога, все разбойники сидят возле костра и внимательно за всем следят. Возле костра сидят:")
        if Bandits_3 == False:
            print(" Трое простых бандитов")
        if bandits_leader == False:
            print(" Громила")
        if Cook == False:
            print(" Повар (женщина)")
        if Hostler == False:
            print(" Конюх")
        if Messenger == False:
            print(" Разбойник-бегун")
    elif alarm == False:
        print(" Возле костра сидят:")
        if Cook == False and cooking_time >= 5:
            print(" Повар (женщина)")
        if Cook == False and cooking_time <= 3:
            print(" Повар (женщина)")
        if Bandits_3 == False:
            print(" Трое простых разбойников")
        if Hostler == False:
            print(" Конюх")
        if Messenger == False:
            print(" Разбойник-бегун")
def frame_1(Bandits_3, bandits_leader, Cook, Hostler, Messenger, geksogen, intro_7, intro_8):
    if Bandits_3 == False or bandits_leader == False and alarm == False or Cook == False or Hostler == False or Messenger == False:
        print(" 1 - Напасть на разбойников.")
    if geksogen == True:
        print(" 2 - Начать шантажировать бандитов.")
    print(" 3 - Подойти к палатке.")
    print(" 4 - Пойти на кухню.")
    print(" 5 - Подойти к арсеналу.")
    if intro_7 == False:
        print(" 6 - Подойти к деревянному сооружению.")
    else:
        print(" 6 - Подойти к конюшне.")
    if intro_8 == False:
        print(" 7 - Подойти к сараю.")
    if intro_8 == True:
        print(' 8 - Подойти к складу.')
    print(" 9 - Осмотреть инвентарь.")
    f = input(">")
    return f
def frame_2():
    print(" Доработать!")