from Controllers import *
def intro_2(Sight):
    if Sight == False:
        print(" За то время что вы провели здесь ваши глаза адоптировались, теперь вы видите лучше.")
        Sight = True
    print(" Вы очутились в небольшом зале. Зал слегка светлее прошлой комнаты. В нескольких метрах перед собой вы видите винтовую лестницу.")
    return Sight
def scene2_frame_1(first_hall, stair, body_1, hole, race, money, exit_1):
    print("Что будете делать?")
    if first_hall == False:
        print(" 1 - Осмотреть зал.")
    if stair == False:
        print(" 2 - Подняться по лестинце.")
    if body_1 == False and first_hall and money == False:
        print(" 3 - осмотреть тело мертвеца.")
    if hole == False and first_hall:
        if race == "человек":
            print(" 4 - осмотреть углубленние.")
        if race == "эльф":
            print(" 4 - осмотреть место платы солнцу.")
    if exit_1 == True:
        if race == "эльф" and first_hall == True:
            print(" 5 - вернуться в зал торжества.")
        else:
            print(" 5 - вернуться в первую комнату.")
    choise = input(">")
    return choise
def scene2_frame_2(race, name, first_hall):
    print(" Осматривая зал вы находите старый труп эльфа, котороый практичекси стал скелетом, а также углубление в одной из стен.")
    if race == "эльф":
        print(f"({name})- Понятно что это за место, склеп служителей солнца. Всегда их ритуал погребения казался мне странным, вы собираетесь всей семьёй, включая детей. Вначале кладёте покойника на стол. Потом устраиваете пир на этом же столе, а выходя по окнчанию пира из комнаты, становитесь угрюмыми и грустными, а покойника засовываете в эту нору и сжигаете, при чём ещё же надо сделать в норе отверстие наружу, чтобы прах его разлетелся по миру прославляя солнце. Хотя каких фанатиков только нет в мире.")
    first_hall = True
    return first_hall
def scene2_frame_3(race, name, money, body_1, poach, body_1_money, powder_poach, sugar):
    print(" Эльф пролежал тут много времени. Ранений не видно, хотя тут трудно определить были они или нет. Скорее всего умер от голода или от жажды.")
    if race == "эльф":
        print(f"({name})- Эльф не похож ни на служителя солнца, ни на воина.")
    a = 0
    b = ""
    while b != "2":
        if body_1_money == False and money == False:
            print(" 1 - Обыскать эльфа.")
        if body_1_money == True and money == False:
            print(" 1 - Забрать монеты.")
        print(" 2 - Отойти от тела.")
        b = input(">")
        if b == "1" and money == False:
            if body_1_money == True:
                if poach == True:
                    while a != 1:
                        if powder_poach == True:
                            print(" Вы вернули порох из мешочка обратно в пороховой ящик и набрали в мешочек монеты.")
                            money = True
                            powder_poach = False
                            break
                        elif sugar == True:
                            print(" Вы вернули сахар обратно в хранилище продуктов и набрали в мешочек монеты.")
                            money = True
                            sugar = False
                            break
                        elif powder_poach == False and sugar == False:
                            print(" Вы набрали в мешочек монеты.")
                            money = True
                            break
                else:
                    print(" Вам некуда сложить монеты.")
            if body_1_money == False:
                print(" Единственная полезная вещь, которая есть у эльфа, золотые монеты.")
                body_1_money = True
                if poach == True:
                    while b != "1":
                        a = input(" 1 - Засыпать в мешочек монеты. \n 2 - Оставить монеты. \n>")
                        if a == "1" and powder_poach == True:
                            print(" Вы вернули порох из мешочка обратно в пороховой ящик и набрали в мешочек монеты.")
                            powder_poach = False
                            money = True
                            break
                        elif a == "1" and sugar == True:
                            print(" Вы вернули сахар обратно в хранилище продуктов и набрали в мешочек монеты.")
                            sugar = False
                            money = True
                            break
                        elif a == "1" and powder_poach == False and sugar == False:
                            print(" Вы набрали в мешочек монеты.")
                            money = True
                            break
                        elif a == "2":
                            break
                        else:
                            print("Выберите 1 или 2.")
                else:
                    print(" Вам некуда сложить монеты.")
        elif b == "2":
            print(" Вы отошли от тела.")
        else:
            print(" Не спорь с рассказчиком.")
    return money, body_1, body_1_money, powder_poach, sugar
def scene2_frame_4(stair):
    print(" Вы поднимаетесь по винтовой лестнице вверх.")
    stair = True
    return stair
def scene2_frame_5(race, exit_1, backtracking_2, backtracking_3, backtracking_4):
    if race == "эльф":
        print(" Вы вернулись в зал торжества.")
    if race == "человек":
        print(" Вы вернулись в первую комнату.")
    backtracking_2 = True
    backtracking_3 = True
    backtracking_4 = True
    exit_1 = False
    return exit_1, backtracking_2, backtracking_3, backtracking_4
def scene2_frame_6(a, b, c, d, race, powder_case, powder_poach, powder_line, Margancovka, sugar, main_exit, hands):
    answer = ""
    answer_2 = ""
    if a == 0:
        if race == "человек":
            print(" Вы осматриваете углубленние. В конце углубления решётка. Из неё идёт слабый синий свет. Между вами и решёткой в углублении лежит свёрток бумаги.")
        if race == "эльф":
            print(" Вы осматриваете место платы солнцу. В конце углубления находится решётка, из неё идёт слабый сиий свет. В середине норы лежит свёрток бумаги.")
        a +=1
    while answer != "3":
        if powder_line == False:
            print(" 1 - Залезть в углубление.") 
        if b == 0:
            print(" 2 - Достать свёрток бумаги.")
        else:
            print(" 2 - Прочесть свёрток повторно.")
        print(" 3 - Отойти.")
        if powder_case == True:
            print(" 4 - попытаться засунуть коробку с порохом внутрь.")
        if powder_line == True and Margancovka and sugar:
            print(" 5 - поджечь порох")
        answer = input(">")
        if answer == "1" and powder_line == False:
            if hands == False:
                print(" Прекрасная идея была залезть сюда в наручниках. Решётку не вибить (как минимум твоей головой), а когда ты это осознал и полез назад, твои наручники зацепиль за небольшой выступ вверху углубления. Пытаясь вытащить руки, ты так сильно их тянул что оторвал часть верха углубления. Произошло небольшой обвал, ты остался жив! Только выход из углубления перегародился и теперь ты умрёшь от жажды. \n КОНЕЦ! ")
                exit()
            else:
                while answer_2 != "2":
                    if c == 0:
                        print(" 1 - Попытаться выбить решётку.")
                    print(" 2 - Вылезти.")
                    if powder_poach == True and powder_line == False:
                        print(" 3 - выложить порох.")
                    answer_2 = input(">")
                    if answer_2 == "1" and c == 0: 
                        print(" Вы попробовали со всей силы выбить решётку. Увы, у вас ничего не вышло, ваших сил явно недостаточно, чтобы выбить её.")
                        c += 1
                    elif answer_2 == "2":
                        print(" Вы вылезли из углубления.")
                    elif answer_2 == "3":
                        print(" Вы высыпали порох из мешочка в конец углубления, поближе к решётке и провели небольшую линию из пороха к началу углубления. Осталось поджечь.")
                        powder_line = True
                        powder_poach = False
                    else:
                        print(" Не спорь с рассказчиком. Выбирай то что дают.")
        elif answer == "2":
            if b == 0:
                print(" Вы достали свёрток, внутри написанно...")
                print("*** Айхорн, эту записку я пишу на случай, если твой план провалится. В том что ты сбежала из этого склепа я не сомневаюсь, но я сомневаюсь, что у вас получится спасти меня. У меня сломана нога, а филфас, особенно молодой, защищает свою територрию до последнего вздоха. Так что я считаю, что не стоит рисковать так ради меня. Эту записку я планирую выкинуть через место платы солнцу, в надежде что кто=нибудь её найдёт и отговорит от этого самоубийственного плана..\n  Тоте. ***")
            if b >= 1:
                print("*** Айхорн, эту записку я пишу на случай, если твой план провалится. В том что ты сбежала из этого склепа я не сомневаюсь, но я сомневаюсь, что у вас получится спасти меня. У меня сломана нога, а филфас, особенно молодой, защищает свою територрию до последнего вздоха. Так что я считаю, что не стоит рисковать так ради меня. Эту записку я планирую выкинуть через место платы солнцу, в надежде что кто=нибудь её найдёт и отговорит от этого самоубийственного плана..\n  Тоте. ***")
            b += 1
        elif answer == "3":
            print(" Вы отошли от углубления")
        elif answer == "4" and powder_case == True:
            print(" Вы пытаетесь запихать ящик в углубление, но он никак туда не залезает. Ящик слишком большой для этого углубления.")
            d += 1
        elif answer == "5" and powder_line == True and Margancovka and sugar:
            print(" Вы засовываете в ткань марганцовку и сахар, начинаете растирать. Через две минуты начал появляться дым, ещё через пол минуты появился первый огонь. Вы трёте ещё несколько секунд, и подносите горящую ткань к пороху. Огонь начинает бежать по пороху, доходит до кучки в конце и ... БАМ! решётка отлетает, и вам открывается вид на ночной лес. Недолго думая вы пролезаете через углубление и вылезаете на свободу.")
            main_exit = True
            break
        else:
            print(" Не спорь с рассказчиком. Выбирай то что дают.")
    return a, b, c, d, powder_line, powder_poach, main_exit
def backtracking_2_1(backtracking_1, backtracking_3, backtracking_4):
    backtracking_1 = False
    backtracking_3 = False
    backtracking_4 = False
    return backtracking_1, backtracking_3, backtracking_4