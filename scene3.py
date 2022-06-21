from Controllers import *
def intro_3():
    print(" Вы поднялись в такой же по размерам зал. Главный выход из зала завален камнями.")
def scene3_frame_1(second_hall, body_2, products_warehouse, arsenal, rise, stair, race):
    print("Что будете делать?")
    if second_hall == False:
        print(" 1 - Осмтореть зал.")
    if body_2 == False and second_hall == True:
        print(" 2 - осмотреть мёртвого эльфа.")
    if products_warehouse == False and second_hall == True:
        print(" 3 - Обыскать место хранения священного огня.")
    if arsenal == False and second_hall == True:
        print(" 4 - Обыскать хранилище продуктов.")
    if rise == False and second_hall == True:
        print(" 5 - Пойти в коридор.")
    if stair == True:
        if race == "человек":
            print(" 6 - Вернуться в прошлый зал.")
        if race == "эльф":
            print(" 6 - Вернуться в прощальный зал.")
    choise = input(">")
    return choise
def scene3_frame_2():
    print(" В середине зала лежит мёртвый эльф. По бокам зала распологаются две двери, одна с надписью *Хранилище еды*, другая *арсенал*.В конце зала находится выход в коридор.")
    second_hall = True
    return second_hall
def scene3_frame_3(name, race, elf_claw, body_2):
    print(f" Труп относительно свежий. Мужчина , эльф, возраст - молодой. Лицо и тело изуродовано когтями. На руках перчатки с когтями. \n ({name}) - Такие перчатки используют эльфы чтобы лазать по стенам.")
    if race == "эльф":
        print(" Эльф-разведчик, только они используют эти перчатки.")
    a = ""
    while a != "1":
        a = input(" 1 - Чтобы забрать перчатки. \n >")
        if a == "1":
            print(" Вы надели перчатки. Теперь у вас будет получаться цепляться за стены.")
            elf_claw = True
            body_2 = True
        else:
            print(" Не спорь с рассказчиком.")
    return elf_claw, body_2
def scene3_frame_4(e, f, sunpriest_key, Key, race, poach, powder_case, powder_poach, sugar, money, powder_case_BOOM, hands):
    a = ""
    b = ""
    c = ""
    f = 0
    e = 0
    while a != "2":
        print(" 1 - Oткрыть дверь.")
        print(" 2 - Отойти от места хранилища священного огня.")
        a = input(">")
        if a == "1":
            if sunpriest_key == False:
                print(" Дверь закрыта на ключ.")
                if Key == True:
                    while a != "1":
                        if race == "человек":
                            a = input(" 1 - Попробовать ключ из первой комнаты.")
                        if race == "эльф":
                            a = input(" 1 - Попробовать ключ из зала торжества.")
                        if a == "1":
                            print(" Ключ не подходит.")
                        else:
                            print(" Не спорь с рассказчиком.")
            if sunpriest_key == True:
                if e == 0:
                    print(" Дверь заперта.")
                    while b != "1":
                        b = input(" 1 - Использовать ключ священника.\n>")
                        if b == "1":
                            print(" Вы открываете дверь и попадаете в небольшое помещение. Единственное что здесь есть это небольшое каменное возвышение и ящик внушительных размеров лежащий на нём.")
                            e += 1
                        else:
                            print(" Выбирай 1.")
                if e == 1:
                    while c != "1":
                        print(" 1 - Выйти из места хранилища священного огня за дверь.")
                        if f == 0:
                            print(" 2 - Осмотреть ящик.")
                        if f == 1 and powder_case == False and powder_case_BOOM == False:
                            print(" 2 - Взять ящик с порохом.")
                            if poach == True and powder_case == False and powder_poach == False:
                                print(" 3 - Набрать порох в мешочек.")
                        if powder_case == True:
                            print(" 4 - поставить ящик обратно.")
                        c = input(">")
                        if c == "1":
                            print(" Вы вышли из места хранения священного огня за дверь.")
                            break
                        if c == "2" and f == 1 and hands == False:
                            print(" Каким образом ты собрался таскать громоздский ящик с руками в наручниках и за спиной?")
                        if c == "2" and f == 1 and hands == True:
                            if powder_poach == True:
                                print(" Вы высыпаете порох обратно в ящик.")
                                powder_poach = False
                            print(" Вы поднимаете ящик с порохом. Ящик громоздсикй, так что пролезет он не везде, таким объёмом можно подорвать даже повозку, и во время взаимодействия с другими местами или предметами вы будете ставить его рядом и поднимать по окончанию взаимодействия.")
                            powder_case = True
                        if c == "2" and f == 0:
                            print(" Вы подходите к ящику и поднимаете крышку. Внутри какой-то порошок. Осмотрев его внимаетльней вы приходите к вывод, что это порох. Порох это хорошо, но его нужно чем-то поджигать.")
                            f += 1
                        if c == "3" and f == 1 and powder_case == False and powder_poach == False:
                            if sugar == True:
                                print(" Вы высыпали сахар из мешочка обратно в кувшин.")
                                sugar = False
                            if money == True:
                                print(" Вы высыпали монеты из мешочка обратно возле трупа эльфа.")
                                money = False
                            print(" Вы набрали порох в мешочек. Что-то тяжёлое вы не сможете взорвать, зато сможете пролезть с мешочком в тесные пространства.")
                            powder_poach = True
                        if c == "4" and powder_case:
                            print(" Вы вернули ящик на место.")
                            powder_case = False
        if a == "2":
            print(" Вы отошли от места хранения священного огня.")
            break
    return f, e, powder_case, powder_poach
def scene3_frame_5(g, flour, powder_poach, money, sugar, poach):
    g = 0
    b = ""
    if g == 0:
        print(" Вы подошли к двери и попытались её открыть. Она не заперта. Вы вошли внутрь.")
        print(" В комнате полно сгнивших продуктов, из того, что не испортилось, остались сахар и мука. Сахар находится в большом кувшыне, мука в небольших мешочках.")
        g += 1
    while b != 1:
        print(" 1 - Выйти из хранилища продуктов.")
        if  flour == False:
            print(" 2 - Взять муку.")
        if poach == True and sugar == False:
            print(" 3 - Насыпать сахар в мешочек.")
        if flour == True:
            print(" 4 - Высыпать муку, чтобы забрать мешочек.")
        b = input(">")
        if b == "1":
            print(" Вы вышли из комнаты.")
            break
        if b == "2" and flour == False:
            print(" Вы взяли один из мешочков с мукой.")
            flour = True
        if b == "3" and sugar == False:
            if money == True:
                money = False
                print(" Вы отнесли монеты из мешочка обратно к мёртвому эльфу.")
            if powder_poach == True:
                print(" Вы отнесли порох обратно в пороховой ящик.")
                powder_poach = False
            print(" Вы набрали сахар в мешочек.")
            sugar = True
        if b == "4" and flour == True:
            print(" Вы высыпаете муку прямо себе под ноги из-за чего появляется облако мешающее осмотру. Пытаясь выйти, вы вспотыкаетесь и падаете, ударяясь головой о кувшин с сахаром. вы падаете на землю, кувшин трескается, и на вас льётся внушительный поток сахара. Так как всё это было крайне неожиданно, вы даже не успели вдохнуть с того момента как вспоткнулись, вы начинаете задыхаться и делаете вдох. Сахар продолжает течь на вашу голову, а из-за того что вы ещё и вдохнули, сахар блокировал ваш рот и нос. Корчась в муках и задыхаясь в сахаре, вы потихоньку теряете сознание и уходите во тьму... \n КОНЕЦ")
            exit()
    return g, flour, powder_poach, money, sugar
def scene3_frame_6(rise):
    rise = True
    print(" Вы пошли в коридор.")
    return rise
def scene3_frame_7(race, stair, backtracking_1, backtracking_3, backtracking_4):
    stair = False
    if race == "человек":
        print(" Вы вернулись в прошлый зал.")
    if race == "эльф":
        print(" Вы вернулись в прощальный зал")
    backtracking_1 = True
    backtracking_3 = True
    backtracking_4 = True
    return stair, backtracking_1, backtracking_3, backtracking_4
def backtracking_3_1(backtracking_1, backtracking_2, backtracking_4):
    backtracking_1 = False
    backtracking_2 = False
    backtracking_4 = False
    return backtracking_1, backtracking_2, backtracking_4