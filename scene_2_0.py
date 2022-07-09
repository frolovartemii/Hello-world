from Controllers_2 import *
def frame_0(Stels_exit, fight_exit,fight_exit_time, Bandits_3, fight_education):
    if Stels_exit == True:
        print(" Выбравшись из склепа, вы находите дорожку и идёте по ней. Через несколько минут ходьбы вы замечаете свет в лесу и звуки, идущие от этого света. Приблизевшись вы понимаете, что это лагерь бандитов. Он огорожен большим забором по периметру, внутри вы видите палатку слева от входа, костёр с людьми по центру, справа что-то напоминающее кухню, за палаткой стоят живые виселицы, за ними виднеется какое-то странное деревянное строение, справа от костра, за кухней стоят стенды с оружием и какие-то ящики, за арсеналом расположенн деревянный сарай и в конце лагеря расположенны ворота, которые ведут дальше по тропе.")
    elif fight_exit == True:
        print(" Выйдя на улицу, вы видите перед собой лес и ночное небо. Вы присели отдохнуть недалеко от выхода и через несколько минут вы заметили несколько теней, которые двигались в вашу сторону. Вы встали и взяли в руки меч, в этот момент из кустов выскочили трое разбойников и набросились на вас.")
        if fight_education == False:
            print(" Это ваша первая боёвка в этой игре. В данной игре они строятся на механике QTE. Вам надо будет быстро писать слова, которые выведет компьютер.")
            fight_education = True
        while a != "1":
            a = input(" Введите 1 чтобы начать битву.")
            if a == "1":
                print(" Молодец, ты победил/а!")
                fight_exit_time += 1
                Bandits_3 = True
                print(" После боя вы решаете поскорее уйти отсюда. Вы находите дорожку, недалеко от склепа и идёте по ней. Через несколько минут ходьбы вы замечаете свет в лесу и звуки, идущие от этого света. Приблизевшись вы понимаете, что это лагерь бандитов. Он огорожен большим забором по периметру, внутри вы видите палатку слева от входа, костёр с людьми по центру, справа что-то напоминающее кухню, за палаткой стоят живые виселицы, за ними виднеется какое-то странное деревянное строение, справа от костра, за кухней стоят стенды с оружием и какие-то ящики, за арсеналом расположенн деревянный сарай и в конце лагеря расположенны ворота, которые ведут дальше по тропе.")
            else:
                print(" Введено неверно.")
    return fight_exit_time, Bandits_3, fight_education
def frame_intro(Stunning_exit):
    if Stunning_exit == True:
        print(" Вы подходите к одному из выходов/входов в лагерь. Из него можно заметить холм, в которов находиться склеп, из которого вы выбрались.")
    else:
        print(" Вы подходите к входу в лагерь.")
def frame_1():
    print(" Что будете делать?")
    if backtracking_2_1 == False:
        print(" 1 - Подойти к палатке.")
    if backtracking_2_2 == False:
        print(" 2 - Подойти к костру.")
    if backtracking_2_3 == False:
        print(" 3 - Подойти к кухни.")
    print(" 4 - Попытаться обойти лагерь через лес.")
    a = input(">")
    return a
def forest_exit():
    print(" Вы пошли в глушь леса. Вы спокойно обходите лагерь. Вдруг вы начинаете слышать какое-то постукивание из леса. Пытаетесь приглядеться, но ничего не видите. Вы продолжаете путь. Перед вами резко пробегает тень размером с волка и прячется в кусатх возле забора лагеря. Из того места куда она убежала идёт трескающийся звук. Вы слегка отходите от забора, пытаясь обойти кусты с неизвестной тварью. Вы начинаете слышать трескающийся звук ещё с нескольких сторон, звуки приближаются. Вы замечаете перед собой небольшие кусты и прячетесь там. Мимо вас проходят три таких же тени размером с волков. Когда они уходят дальше вы вздыхаете с облегчением. Вы разворачиваетесь и планируете вернуться обратно ближе к лагерю. Но видите перед собой раскрытую пасть, в которой зубы расположены по спиралями. Вы не успеваете даже крикнуть, как вас разрывают тысячи зубов. \n КОНЕЦ!")
    exit()
def frame_2(backtracking_2_1,backtracking_2_2,backtracking_2_3,backtracking_2_5,backtracking_2_6,backtracking_2_7,backtracking_2_8, backtracking_2_4, intro_9):
    backtracking_2_1 = False
    backtracking_2_2 = False
    backtracking_2_3 = False
    backtracking_2_5 = False
    backtracking_2_6 = False
    backtracking_2_7 = False
    backtracking_2_8 = False
    backtracking_2_4 = False
    if intro_9 == True:
        print(" Вы подошли ко входу в лагерь.")
    return backtracking_2_1,backtracking_2_2,backtracking_2_3,backtracking_2_5,backtracking_2_6,backtracking_2_7, backtracking_2_8, backtracking_2_4
def go_tent(backtracking_2_2, backtracking_2_3, backtracking_2_4,backtracking_2_5,backtracking_2_6,backtracking_2_7,backtracking_2_8,backtracking_2_9):
    backtracking_2_2 = True
    backtracking_2_3 = True
    backtracking_2_4 = True
    backtracking_2_5 = True
    backtracking_2_6 = True
    backtracking_2_7 = True
    backtracking_2_8 = True
    backtracking_2_9 = True
    return backtracking_2_2, backtracking_2_3, backtracking_2_4,backtracking_2_5,backtracking_2_6,backtracking_2_7,backtracking_2_8,backtracking_2_9
def go_horsehouse(backtracking_2_1,backtracking_2_2,backtracking_2_3,backtracking_2_4,backtracking_2_5,backtracking_2_6,backtracking_2_8,backtracking_2_9):
    backtracking_2_1 = True
    backtracking_2_2 = True
    backtracking_2_3 = True
    backtracking_2_4 = True
    backtracking_2_5 = True
    backtracking_2_6 = True
    backtracking_2_8 = True
    backtracking_2_9 = True
    return backtracking_2_1,backtracking_2_2,backtracking_2_3,backtracking_2_4,backtracking_2_5,backtracking_2_6,backtracking_2_8,backtracking_2_9
def go_bonfire(backtracking_2_1,backtracking_2_7,backtracking_2_3,backtracking_2_4,backtracking_2_5,backtracking_2_6,backtracking_2_8,backtracking_2_9):
    backtracking_2_1 = True
    backtracking_2_7 = True
    backtracking_2_3 = True
    backtracking_2_4 = True
    backtracking_2_5 = True
    backtracking_2_6 = True
    backtracking_2_8 = True
    backtracking_2_9 = True
    return backtracking_2_1,backtracking_2_7,backtracking_2_3,backtracking_2_4,backtracking_2_5,backtracking_2_6,backtracking_2_8,backtracking_2_9
def go_kitchen(backtracking_2_1,backtracking_2_7,backtracking_2_2,backtracking_2_4,backtracking_2_5,backtracking_2_6,backtracking_2_8,backtracking_2_9):
    backtracking_2_1 = True
    backtracking_2_7 = True
    backtracking_2_2 = True
    backtracking_2_4 = True
    backtracking_2_5 = True
    backtracking_2_6 = True
    backtracking_2_8 = True
    backtracking_2_9 = True
    return backtracking_2_1,backtracking_2_7,backtracking_2_2,backtracking_2_4,backtracking_2_5,backtracking_2_6,backtracking_2_8,backtracking_2_9
def go_gate(backtracking_2_1,backtracking_2_7,backtracking_2_2,backtracking_2_4,backtracking_2_5,backtracking_2_3,backtracking_2_8,backtracking_2_9):
    backtracking_2_1 = True
    backtracking_2_7 = True
    backtracking_2_2 = True
    backtracking_2_4 = True
    backtracking_2_5 = True
    backtracking_2_3 = True
    backtracking_2_8 = True
    backtracking_2_9 = True
    return backtracking_2_1,backtracking_2_7,backtracking_2_2,backtracking_2_4,backtracking_2_5,backtracking_2_3,backtracking_2_8,backtracking_2_9
def go_arsenal(backtracking_2_1,backtracking_2_7,backtracking_2_2,backtracking_2_4,backtracking_2_3,backtracking_2_6,backtracking_2_8,backtracking_2_9):
    backtracking_2_1 = True
    backtracking_2_7 = True
    backtracking_2_2 = True
    backtracking_2_4 = True
    backtracking_2_3 = True
    backtracking_2_6 = True
    backtracking_2_8 = True
    backtracking_2_9 = True
    return backtracking_2_1,backtracking_2_7,backtracking_2_2,backtracking_2_4,backtracking_2_3,backtracking_2_6,backtracking_2_8,backtracking_2_9
def go_warehouse(backtracking_2_1,backtracking_2_7,backtracking_2_2,backtracking_2_4,backtracking_2_5,backtracking_2_6,backtracking_2_3,backtracking_2_9):
    backtracking_2_1 = True
    backtracking_2_7 = True
    backtracking_2_2 = True
    backtracking_2_4 = True
    backtracking_2_5 = True
    backtracking_2_6 = True
    backtracking_2_3 = True
    backtracking_2_9 = True
    return backtracking_2_1,backtracking_2_7,backtracking_2_2,backtracking_2_4,backtracking_2_5,backtracking_2_6,backtracking_2_3,backtracking_2_9
def go_enter(backtracking_2_1,backtracking_2_7,backtracking_2_2,backtracking_2_4,backtracking_2_5,backtracking_2_6,backtracking_2_8,backtracking_2_3):
    backtracking_2_1 = True
    backtracking_2_7 = True
    backtracking_2_2 = True
    backtracking_2_4 = True
    backtracking_2_5 = True
    backtracking_2_6 = True
    backtracking_2_8 = True
    backtracking_2_3 = True
    return backtracking_2_1,backtracking_2_7,backtracking_2_2,backtracking_2_4,backtracking_2_5,backtracking_2_6,backtracking_2_8,backtracking_2_3
def go_prison(backtracking_2_1,backtracking_2_7,backtracking_2_2,backtracking_2_3,backtracking_2_5,backtracking_2_6,backtracking_2_8,backtracking_2_9):
    backtracking_2_1 = True
    backtracking_2_7 = True
    backtracking_2_2 = True
    backtracking_2_3 = True
    backtracking_2_5 = True
    backtracking_2_6 = True
    backtracking_2_8 = True
    backtracking_2_9 = True
    return backtracking_2_1,backtracking_2_7,backtracking_2_2,backtracking_2_3,backtracking_2_5,backtracking_2_6,backtracking_2_8,backtracking_2_9