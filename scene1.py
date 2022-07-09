from Controllers import *
def intro():
    print(""" Вы открыли глаза. В нос ударил резкий запах (вероятно он и стал причиной вашего пробуждения). Голова расскалывается от боли. 
Вы пытаетесь встать, но падаете.Ваши руки закованы за спиной в наручниках. С трудом вам удаётся встать.
В комнате плохое освященние. Вы смутно видите границы комнаты, в середине комнаты находится небольшое каменное возвышение размером Ненамного больше человека, в углу вы замечаете труп (скорее всего, он и был причиной запаха).""")
def intro_frame_3(Sight, hands, door_1, Key, h, intro2, race):
    print("Что будете делать теперь? \n 1 - Голова раскалывается, почему бы не прилечь на это возвышение и не отдохнуть?.")
    if Sight == False:
        print(" 2 - Подождать, пока глаза привыкнут к темноте.")
    if hands == False:
        print(" 3 - Попытаться освободить руки.")
    if door_1 == False:
        print(" 4 - Осмотреть стены в поисках выхода.")
    if Key == False:
        print(" 5 - Осмотреть труп.")
    if door_1 == True and h == 0:
        print(" 6 - изучить дверь.")
    if intro2 == 1:
        if race == "эльф":
            print(" 7 - вернуться в прощальный зал.")
        if race == "человек":
            print(" 7 - вернуться в зал.")
    print(" 8 - Показать инвентарь.")
    choise = input(">")
    return choise 
def race_name():
    name = input("Введите имя персонажа: ")
    race  = ""
    while race != "эльф" and race != "человек" and race != "вампир":
        race = input("Выберите расу персонажа: \n 1 - Эльф \n 2 - Человек \n ваша раса - ")
        if race == "1":
            race = "эльф"
        elif race == "2":
            race = "человек"
        else:
            print("Выбирай из того что дают, другого пока что не дано.")
    return name , race
def scene1__frame1():
    print("С такой болью трудно уснуть, но ещй сложнее проснуться. Вы ложитесь на каменную возвышыность и через некоторое время засыпаете. Увы больше вы не просыпаетесь \n КОНЕЦ!")
    exit()
def scene1_frame2(Sight):
    print(" Вы сели на возвышение и стали ждать. Через некоторое время ваши глаза привыкли к темноте. Вы хоть и не стали видеть всё, но видите гораздо лучше чем до этого.")
    Sight = True
    return Sight
def scene1_frame3(hands):
    hands = True
    print(" После трудных акробатических движений вы всё-таки сняли наручники. Вы наконец смогли потрогать рану на затылке. Посмотрев на руку вы видите кровь.")
    return hands
def scene1_frame4(hands, Sight, door_1):
    if hands == False and Sight == False:
        print(""" Практически ничего не видя, в наручниках, вы начинаете руками за спиной ощупывать все стены. Обойдя всю комнату вы не нашли ничего на подобие выхода.(Возможно осматривать стены вслепую и в наручниках не лучшая идея.""")
        door_1 = False
    if hands == True and Sight == False:
        print(" В темноте, но со свободными руками вы начинаете ощупывать стены. Идя по комнате вы нащупываете какое-то отверстие, сильно присмотревшись и ощупав эту стену, вы приходите к выводу, что это дверь.")
        door_1 = True
    if hands == False and Sight == True:
        print(" С закованными руками, но относительно неплохим зрением вы начинаете обходить комнату, осматривая стены. Во время этого обхода вы замечаете выделяющийся кусок стены, осмотрев его внимательнее вы окончательно приходите к выводу что это дверь.")
        door_1 = True
    if hands == True and Sight == True:
        print(" Со свободными руками и привыкшими глазами вы начинаете поиски выхода. Заметив выделяющийся кусок стены вы ощупываете его и понимаете что это дверь.")
        door_1 = True
    return door_1
def scene1_frame5(Key):
    print(" Подходя к трупу, вы воротите нос. Смердит он знатно. Приблизившись к нему вплотную вы видите изуродованное существо, кожа обгорела. расу. пол или возраст не определить.")
    f = 0
    b = input(" 1 - чтобы обыскать труп. \n>")
    while f < 1:
        if b == "1":
            f += 1
            print(" Вы обыскиваете его карманы. Ни оружия, ни чего-нибудь, что помогло бы вылечить рану, ни чего-нибудь, что помогло бы понять что произонло, зато кое-что лучше, ключ!")
            Key = True
        else:
            b = input(" У тебя всего один вариант, не спорь с рассказчиком. \n>")
    return Key
def scene1_frame6(Sight, hands, Key, exit_1):
    a = ""
    flag = False
    flag_1 = False
    while exit_1 == False:
        if Sight:
            print(" 1 - Осмотреть дверь.")
        if hands:
            print(" 2 - ощупать дверь.")
        if flag:
            print(" 3 - попытаться выбить дверь.")
        if flag_1 and Key:
            print(" 4 - попробовать вставить ключ в отверстие.")
        a = input(">")
        if a == "1" and Sight:
            print(" Дверь старая и, на взгляд, не очень крепкая.")
            flag = True
            Sight = False
        elif a == "2" and hands:
            print(" Ощупав дверь вы понимаете что в двери есть отверстие для ключа.")
            flag_1 = True
            hands = False
        elif a == "3" and flag:
            print(" Вы слегка отходите от двери и начинаете резко бежите на неё. БАХ! Дверь сдвинулась, но не сильно. Вы пробуете без разбега просто давить на дверь. Приложив усилия вам удаётся отодвинуть дверь и вы выходите в коридор. Рядом с вами большие камни (они и загораживали выход).")
            exit_1 = True
        elif a == "4" and flag_1:
            print(" Вы пробуете вставить ключ в замочную скважину, но ключ не вставляется. Вы силой пытаетесь его туда запихнуть и дверь слегка отодвигается. Если сильно приложится, то может она и откроется.")
            flag = True
            flag_1 = False
        else:
            print(" У тебя всего один вариант, не спорь с рассказчиком.")
    return exit_1
def scene1_frame7(exit_1, race):
    exit_1 = True
    if race == "человек":
        print(" Вы вернулись в зал.")
    if race == "эльф":
        print(" Вы вернулись в прощальный зал.")
    return exit_1
def backtracking_1_1(backtracking_2, backtracking_3, backtracking_4):
    backtracking_2 = False
    backtracking_3 = False
    backtracking_4 = False
    return backtracking_2, backtracking_3, backtracking_4
def inventory_check(inventory,sunpriest_key, e, Key, hands, money, powder_poach, powder_case, Margancovka, sugar, poach, elf_claw, flour):
    if sunpriest_key == True and "Ключ священника" not in inventory:
        inventory.append("Ключ священника")
    if e != 0 and "Ключ священника" in inventory:
        inventory.remove("Ключ священника")
    if Key == True and "Ключ трупа с обезображенным лицом" not in inventory:
        inventory.append("Ключ трупа с обезображенным лицом")
    if hands == True and "Ключ трупа с обезображенным лицом" in inventory:
        inventory.remove("Ключ трупа с обезображенным лицом")
    if money == True and "Мешочек с монетами" not in inventory:
        inventory.append("Мешочек с монетами")
    if money == False and "Мешочек с монетами" in inventory:
        inventory.remove("Мешочек с монетами")
    if powder_poach == True and "Мешочек с порохом" not in inventory:
        inventory.append("Мешочек с порохом")
    if powder_poach == False and "Мешочек с порохом" in inventory:
        inventory.remove("Мешочек с порохом")
    if powder_case == True and "Ящик с порохом" not in inventory:
        inventory.append("Ящик с порохом")
    if powder_case == False and "Ящик с порохом" in inventory:
        inventory.remove("Ящик с порохом")
    if Margancovka == True and "Марганцовка" not in inventory:
        inventory.append("Марганцовка")
    if sugar == True and "Мешочек с сахаром" not in inventory:
        inventory.append("Мешочек с сахаром")
    if sugar == False and "Мешочек с сахаром" in inventory:
        inventory.remove("Мешочек с сахаром")
    if poach == True and powder_poach == False and sugar == False and money == False and "Пустой мешочек" not in inventory:
        inventory.append("Пустой мешочек")
    if powder_poach == True or sugar == True or money == True and "Пустой мешочек" in inventory:
        inventory.remove("Пустой мешочек")
    if elf_claw == True and "Перчатки эльфа" not in inventory:
        inventory.append("Перчатки эльфа")
    if flour == True and "Мешочек с мукой" not in inventory:
        inventory.append("Мешочек с мукой")
    if len(inventory) > 0:
        print(inventory)
    else:
        print(" В вашем инвентаре ничего нет.")
    return inventory