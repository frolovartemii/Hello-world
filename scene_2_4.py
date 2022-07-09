from Controllers_2 import *
def stunning_intro(backtracking_2_1,backtracking_2_2,backtracking_2_3,backtracking_2_5,backtracking_2_6,backtracking_2_7,backtracking_2_8, backtracking_2_9,a):
    backtracking_2_1 = True
    backtracking_2_2 = True
    backtracking_2_3 = True
    backtracking_2_5 = True
    backtracking_2_6 = True
    backtracking_2_7 = True
    backtracking_2_8 = True
    backtracking_2_9 = True
    a = True 
    return backtracking_2_1,backtracking_2_2,backtracking_2_3,backtracking_2_5,backtracking_2_6,backtracking_2_7,backtracking_2_8, backtracking_2_9, a
def backtracking2_4_2(backtracking_2_1,backtracking_2_2,backtracking_2_3,backtracking_2_5,backtracking_2_6,backtracking_2_7,backtracking_2_8, backtracking_2_9, a):
    backtracking_2_1 = False
    backtracking_2_2 = False
    backtracking_2_3 = False
    backtracking_2_5 = False
    backtracking_2_6 = False
    backtracking_2_7 = False
    backtracking_2_8 = False
    backtracking_2_9 = False
    if a == False:
        print(" Вы подошли к живым виселицам.")
    return backtracking_2_1,backtracking_2_2,backtracking_2_3,backtracking_2_5,backtracking_2_6,backtracking_2_7, backtracking_2_8, backtracking_2_9
def scene_4_intro_1():
    print(" Вы приходите в себя. Голова ужасно болит. Вы начинаете соображать, осознаёте что весите вверх ногами. Осмотревшись вокруг, вы понимаете что находитесь в лагере, по периметру которого расположен высокий забор, вы видите рядом ещё две живых виселицы, с трупами на них, спереди, в нескольких десятках метров, вы видите костёр и людей возле костра, справа деревянную постройку, слева палатка, между костром и палаткой вы видите что-то похожее на кухню. за костром виден склад оружия, между костром и странной деревянной постройкой виден деревянный сарай.")
def scene_4_intro_2():
    print(" Вы видите перед собой три деревянных висилицы. На двух из них висят трупы, но подвешенные не за шею, а за ноги.")
def scene_4_frame_1(a, name, Margancovka):
    while a != True:
        while choise != "1":
            choise = input(" 1 - Подтянуться к ногам.")
            if choise == "1":
                choise = ""
                while choise != "1":
                    choise = input(" 1 - Попробовать развязать ноги.")
                    if choise == "1":
                        if Margancovka == True:
                            print(f" Вы подтягиваетесь к ногам и пытаетесь развязать верёвку, она завязанна крайне не качественно, и вы быстро её развязываете и падаете на землю. \n Вы встаёте и осматриваете свои карманы. Ничего не осталось, кроме марганцовки. ({name}) - Видимо, они даже не поняли, что это.")
                        else:
                            print(" Вы подтягиваетесь к ногам и пытаетесь развязать верёвку, она завязанна крайне не качественно, и вы быстро её развязываете и падаете на землю. \n Вы встаёте и осматриваете свои карманы. Ничего не осталось.")
                        a = True
                    else:
                        print(" Тут только один вариант.")
            else:
                print(" Тут только один вариант.")
    return a
def scene_4_frame_2(intro_7, gallows_bodies, backtracking_2_1,backtracking_2_7,backtracking_2_2, shovel, body_write, gate_key):
    b = ""
    print(" Что будете делать?")
    if backtracking_2_1 == False:
        print(" 1 - Подойти к палатке")
    if backtracking_2_7 == False:
        if intro_7 == False:
            print(" 2 - Подойти к деревянному сооружению.")
        elif intro_7 == True:
            print(" 2 - Подойти к конюшне.")
    if backtracking_2_2 == False:
        print(" 3 - Подойти к костру.")
    if gallows_bodies == False:
        print(" 4 - Осмотреть подвешенные тела.")
    if body_write == True and shovel == True and gate_key == False:
        print(" 5 - Выкопать ключ.")
    print(" 6 - Осмотреть инвентарь.")
    b = input(">")
    return b
def scene_4_frame_3(gallows_bodies, name, picklock):
    print(f" Вы осматриваете оба висящих тела. Оба трупа свежие, один человек, второе тело изуродовано. Осмотрев первый труп вы ничего не находите. Осматривая второй вы слышите странное лязганье. Вы прислушиваетесь и понимаете, что этот звук идёт из-зо рта у трупа. С отвращением вы открываете рот трупу и засовываете туда руку. Вы нащупываете  небольшой предмет. Вытащив и осмотрев его, вы понимаете, что это отмычка. \n ({name}) - Если бы он знал как будут избивать его лицо, то ни за что не положил бы отмычку в рот.")
    gallows_bodies = True
    picklock = True
    return gallows_bodies, picklock
def scene_4_frame_4(gate_key):
    print(" Вы начинаете копать в месте указаном в записке. В скором времени ваша лопата натыкается на что-то железное. Вы нашли ключ от ворот.")
    gate_key = True
    return gate_key
def inventory_check(inventory, Margancovka, picklock, warehouse_lock, gate_key, gate, Stunning_exit, elf_claw, bandits_leader_body, flour, camp_flour):
    if Margancovka == True and "Марганцовка" not in inventory:
        inventory.append("Марганцовка")
    if picklock == True and "Отмычка" not in inventory:
        inventory.append("Отмычка")
    if warehouse_lock == True and "Отмычка" in inventory:
        inventory.remove("Отмычка")
    if gate_key == True and "Ключ от ворот" not in inventory:
        inventory.append("Ключ от ворот")
    if gate == True and "Ключ от ворот" in inventory:
        inventory.remove("Ключ от ворот")
    if Stunning_exit == True:
        if elf_claw == True and bandits_leader_body == True and "Перчатки эльфа" not in inventory:
            inventory.append("Перчатки эльфа")
    elif Stunning_exit == False and elf_claw == True and "Перчатки эльфа" not in inventory:
        inventory.append("Перчатки эльфа")
    if flour == True and camp_flour == True and "Мука" not in inventory:
        inventory.append("Мука")
    print(inventory)
    return inventory