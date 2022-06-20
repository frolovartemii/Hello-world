from random import choices
from Controllers import *
def intro(race, name):
    print(" Вы вышли в коридор. Потолок  обвалился, и единственный путь - это путь наверх. Вы поднимаетесь по обваленному потолку и выходите в большой зал, освящённый лунным светом. Вы видите выход! Но какой-то особо большой булыжник перегораживает вам вид. Приглядевшись вы понимаете, что это не булыжник, а зверь. Он достаточно больших размеров и на вид как смесь медведя с барсуком.")
    if race == "человек":
        print(f" {name} - Бурмедь. Жестокая тварь. Смерть от бурмедя ещё называют сладкой смертью, потому что когда он тебя съест, ты будешь чувствовать сладкий запах от его зубов. ")
    if race == "эльф":
        print(f" {name} - Филфас. Убийственный сладкоежка.")
def scene4_frame_1(third_hall, rise, body_3):
    print("Что будете делать?")
    if third_hall == False:
        print(" 1 - Осмотреть помещение.")
    if rise == True:
        print(" 2 - Вернуться в прошлый зал.")
    if third_hall == True and body_3 == False:
        print(" 3 - Осмотреть тела.")
    if third_hall == True and body_3 == True:
        print(" 3 - Подойти к телам.")
    if third_hall == True:
        print(" 4 -Подойти под отверстие.")
    choice = input(">")
    return choice
def scene4_frame_2(name):
    print(f" Осматривая логово зверя вы заметили трупы возле противоположной стены от выхода ({name} Если приманить туда зверя, то можно будет прошмыгнуть в выход) и отверстие в потолке по центру комнаты ({name} - Если поставить туда что-то выскокое, то можно будет запрыгнуть наверх.).")
    third_hall = True
    return third_hall
def scene4_frame_3(rise, backtracking_1, backtracking_2, backtracking_4):
    print(" Вы вернулись в прошлый зал.")
    rise = False
    backtracking_1 = True
    backtracking_2 = True
    backtracking_4 = True
    return rise, backtracking_1, backtracking_2, backtracking_4
def scene4_frame_4(body_3, name, Head, Margancovka):
    print(" Вы подходите к стене и видите двоих мёртвых эльфов. Одна девушка и один мужчина.")
    a = ""
    b = ""
    body_3_1 = False
    body_3_2 = False
    while body_3 == False:
        if body_3_1 == False:
            print(" 1 - Осмотреть женщину.")
        if body_3_2 == False:
            print(" 2 - Осмотреть мужчину")
        a = input(">")
        if a == "1" and body_3_1:
            print(f" {name} - Эльфийка-медик. Умерла достаточно давно, молодая.")
            while b != "1":
                b = input(" 1 - Обыскать эльфийку.")
                if b == "1":
                    print(f" У эльфийки вы нашли медицинскую ткань и марганцовку. Вы намотали часть медицинской ткани на рану на голове. ({name} - Марганцовку и остаток ткани можно использовать чтобы получить огонь, если смешать марганцовку с глицерином, пропиленгликоля и водой или с сахаром.")
                    body_3_1 = True
                    Head = True
                    Margancovka = True
                else:
                    print(" Нет такого варианта.")
        elif a == "2" and body_3_2:
            if race == "":
                print("")
            if race == "":
                print("")
            while b != "1":
                print(" 1 - Чтобы обыскать эльфа")
                
        else:
            print(" Нет такого варианта.") 