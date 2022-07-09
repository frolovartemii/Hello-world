from Controllers_2 import *
import random
Stels_exit = True
Stunning_exit = False
fight_exit = False
name = "Регель"
race = "эльф"
inventory = []
Margancovka = False
flour = True
import time
import scene_2_0
import scene_2_1
import scene_2_2
import scene_2_3
import scene_2_4
import scene_2_5
import scene_2_6
import scene_2_7
def alarm_timer(fight_exit_time, alarm, name, bandits_leader):
        if fight_exit_time >= 1:
            fight_exit_time += 1
        if fight_exit_time == 5 and alarm == False:
            print(" Бандиты возле костра начали что-то громко обсуждать. Вы прислушиваетесь к их разговору: \n - Сколько уже можно бродить в этом патруле!?\n - Пошли проведаем их. Кёхин, ты одна остаёшся, мы скоро вернёмся. \n После этого вы видите как двое человек возле костра встают и уходят.")
        if fight_exit_time == 10 and alarm == False:
            if bandits_leader == False:
                print(f" Вы слышите какой-то звук, прислушиваетесь, это топот. Обернувшись на звук, вы видите как в лагерь возвращаются двое бандитов, которые ушли. Один подходит к повару и что-то ему говорит. Второй бежит в палатку и через некоторое время возвращается от туда с главарём бандитов. \n ({name}) - Чёрт! Они нашли трупы.")
            else:
                print(f" Вы слышите какой-то звук, прислушиваетесь, это топот. Обернувшись на звук, вы видите как в лагерь возвращаются двое бандитов, которые ушли. Один подходит к повару и что-то ему говорит. Второй бежит в палатку и через некоторое время выбегает оттуда крича: *ГЛАВАРЬ УБИТ!*. \n ({name}) - Чёрт! Они нашли трупы.")
            alarm = True
        return fight_exit_time, alarm
def alarm_1(bandits_leader):
    print(" В лагере поднята тревога!")
    if bandits_leader == False:
        print(" Разбойники разбудили главаря.")
    print(" Все разбойники собрались возле костра. Они не будут заниматься своими делами и обращать внимание на отвлекающие звуки, но будут внимательно следить за всем происходящим.")
def alarm_carma(bandits_leader,Cook,Hostler,Bandits_3,Messenger, fight_education): # Доделать!
    random_int = random.randint(1, 24)
    if random_int == 2 or random_int == 14 or random_int == 23:
        print(" Разбойники заметили вас!")
        if fight_education == False:
            print("")
            fight_education = True
        if Bandits_3 == False:
            print(" Первыми на вас напали трое простых разбойников.")
        else:
            if Hostler == False:
                print(" Первым на вас напал конюх.")
    return fight_education
def cooking_timer(cooking_time, intro_2, Cake, poison_food, Cook, Hostler, Bandits_3, Messenger, alarm, Stunning_exit, flour, camp_sugar):
    if alarm == False:
        cooking_time += 1
        if Stunning_exit == True and flour == True:
            print(" Вы слышите как один из разбойников говорит другому: *Раз уж у нас появилась мука, то я приготовлю вам торт, но мне нужен сахар. Так что сбегай пока за сахарной свёклой.*.")
            if cooking_time == 1:
                print(" Вы замечаете как один из разбойников возвращается в лагерь и ставит на кухне сахарные свёклы.")
        if cooking_time == 3:
            if intro_2 == False:
                print(" Вы слышите как один из разбойников возле костра сказал: *Я пойду готовить.*.")
            else:
                print(" Вы замечаете, что возле костра что-то происходит. Повар встаёт и говорит: *Я пойду готовить.*.")
        if Stunning_exit == True and flour == True and cooking_time == 4:
            print(" Вы замечаете как на кухне появился новый мешочек. Вероятно повар закончила приготовление сахара.")
            camp_sugar = True
        if cooking_time == 6:
            if Cake == True:
                print(" Вы слышите крики с кухни. * Я закончила, но торту надо настояться, кто поробует сожрать торт до нужного момента получит ложкой по макушке.")
            else:
                print(" Вы слышите крики с кухни. * Я закончила, но супу надо настояться, кто поробует сожрать суп до нужного момента получит ложкой по макушке.*")
        if cooking_time == 10:
            if Cake == True:
                print(" Вы замечаете как повар идёт на кухню и возвращается оттуда с тортом. Разбойники с радостью начинают пожирать лакомство.")
            else:
                print(" Вы замечаете как повар идёт на кухню и возвращается оттуда с супом. Голодные бандиты с радостью начинают поедать суп.")
            if poison_food == True:
                    print(" Вдруг, один из разбойников падает без сознания на землю. Остальные в ужасе посмотрели на упавшего. Ещё одного вдруг вырвало. Яд начал действовать. Спустя минуту мучений все разбойники были мертвы.")
                    Bandits_3 = True
                    Cook = True
                    Messenger = True
                    Hostler = True
    if alarm == True and cooking_time >= 2 and cooking_time <= 6:
        print(" Кухарка оставляет еду недоготовленной и присоеденяется к другим разбойникам возле костра.")
    return cooking_time, Bandits_3, Cook, Messenger, Hostler, camp_sugar
alarm_counter = False
intro_1 = False
intro_2 = False
intro_3 = False
intro_4 = False
intro_5 = False
intro_6 = False
intro_7 = False
intro_8 = False
intro_9 = False
intro_1_1 = False
intro_1_2 = False
cooking_time = -1
variation = ""
variant = ""
var = ""
if Stunning_exit == True:
    inventory.clear()
    print(" И после выхода вы резко теряете сознание от удара по затылку.")
    time.sleep(2)
    print(" Вы открываете глаза. Вас тащат за ноги. Вы замечаете какой-то свет впереди. Вы снова теряете сознание.")
    time.sleep(2)
    backtracking_2_1,backtracking_2_2,backtracking_2_3,backtracking_2_5,backtracking_2_6,backtracking_2_7,backtracking_2_8, backtracking_2_9, a = scene_2_4.stunning_intro(backtracking_2_1,backtracking_2_2,backtracking_2_3,backtracking_2_5,backtracking_2_6,backtracking_2_7,backtracking_2_8, backtracking_2_9, a)
elif Stels_exit == True or fight_exit == True:
    fight_exit_time, Bandits_3, fight_education = scene_2_0.frame_0(Stels_exit, fight_exit,fight_exit_time, Bandits_3, fight_education)
    backtracking_2_1,backtracking_2_7,backtracking_2_2,backtracking_2_4,backtracking_2_5,backtracking_2_6,backtracking_2_8,backtracking_2_3 = scene_2_0.go_enter(backtracking_2_1,backtracking_2_7,backtracking_2_2,backtracking_2_4,backtracking_2_5,backtracking_2_6,backtracking_2_8,backtracking_2_3)
while gate == False:
    if backtracking_2_4 == False:
        fight_exit_time, alarm = alarm_timer(fight_exit_time, alarm, name, bandits_leader)
        cooking_time, Bandits_3, Cook, Messenger, Hostler, camp_sugar = cooking_timer(cooking_time, intro_2, Cake, poison_food, Cook, Hostler, Bandits_3, Messenger, alarm, Stunning_exit, flour, camp_sugar)
        backtracking_2_1,backtracking_2_2,backtracking_2_3,backtracking_2_5,backtracking_2_6,backtracking_2_7, backtracking_2_8, backtracking_2_9 = scene_2_4.backtracking2_4_2(backtracking_2_1,backtracking_2_2,backtracking_2_3,backtracking_2_5,backtracking_2_6,backtracking_2_7, backtracking_2_8, backtracking_2_9, a)
        while backtracking_2_4 == False:
            if alarm == True and alarm_counter == False:
                alarm_1()
                alarm_counter = True
            if intro_4 == False:
                if a == True:
                    scene_2_4.scene_4_intro_1()
                    intro_4 = True
                elif a == False:
                    scene_2_4.scene_4_intro_2()
                    intro_4 = True
            if a == True:
                a = scene_2_4.scene_4_frame_1(a, name)
            elif a == False:
                choise = scene_2_4.scene_4_frame_2(intro_7, gallows_bodies, backtracking_2_1,backtracking_2_7,backtracking_2_2, shovel, body_write, gate_key)
                if choise == "1":
                    backtracking_2_2, backtracking_2_3, backtracking_2_4,backtracking_2_5,backtracking_2_6,backtracking_2_7,backtracking_2_8,backtracking_2_9 = scene_2_0.go_tent(backtracking_2_2, backtracking_2_3, backtracking_2_4,backtracking_2_5,backtracking_2_6,backtracking_2_7,backtracking_2_8,backtracking_2_9)
                elif choise == "2":
                    backtracking_2_1,backtracking_2_2,backtracking_2_3,backtracking_2_4,backtracking_2_5,backtracking_2_6,backtracking_2_8,backtracking_2_9 = scene_2_0.go_horsehouse(backtracking_2_1,backtracking_2_2,backtracking_2_3,backtracking_2_4,backtracking_2_5,backtracking_2_6,backtracking_2_8,backtracking_2_9)
                elif choise == "3":
                    backtracking_2_1,backtracking_2_7,backtracking_2_3,backtracking_2_4,backtracking_2_5,backtracking_2_6,backtracking_2_8,backtracking_2_9 = scene_2_0.go_bonfire(backtracking_2_1,backtracking_2_7,backtracking_2_3,backtracking_2_4,backtracking_2_5,backtracking_2_6,backtracking_2_8,backtracking_2_9)
                elif choise == "4"and gallows_bodies == False:
                    gallows_bodies, picklock = scene_2_4.scene_4_frame_3(gallows_bodies, name,  picklock)
                elif choise == "5" and body_write == True and shovel == True and gate_key == False:
                    gate_key = scene_2_4.scene_4_frame_4(gate_key)
                elif choise == "6":
                    inventory = scene_2_4.inventory_check(inventory, Margancovka, picklock, warehouse_lock, gate_key, gate)
                else:
                    print(" Введено неверно.")
    if backtracking_2_9 == False:
        fight_exit_time, alarm = alarm_timer(fight_exit_time, alarm, name, bandits_leader)
        cooking_time, Bandits_3, Cook, Messenger, Hostler, camp_sugar = cooking_timer(cooking_time, intro_2, Cake, poison_food, Cook, Hostler, Bandits_3, Messenger, alarm, Stunning_exit, flour, camp_sugar)
        backtracking_2_1,backtracking_2_2,backtracking_2_3,backtracking_2_5,backtracking_2_6,backtracking_2_7, backtracking_2_8, backtracking_2_4 = scene_2_0.frame_2(backtracking_2_1,backtracking_2_2,backtracking_2_3,backtracking_2_5,backtracking_2_6,backtracking_2_7, backtracking_2_8, backtracking_2_4, intro_9)
        while backtracking_2_9 == False:
            if alarm == True and alarm_counter == False:
                alarm_1()
                alarm_counter = True
            if intro_9 == False:
                scene_2_0.frame_intro(Stunning_exit)
                intro_9 = True
            choise = scene_2_0.frame_1()
            if choise == "1":
                backtracking_2_2, backtracking_2_3, backtracking_2_4,backtracking_2_5,backtracking_2_6,backtracking_2_7,backtracking_2_8,backtracking_2_9 = scene_2_0.go_tent(backtracking_2_2, backtracking_2_3, backtracking_2_4,backtracking_2_5,backtracking_2_6,backtracking_2_7,backtracking_2_8,backtracking_2_9)
            elif choise == "2":
                backtracking_2_1,backtracking_2_7,backtracking_2_3,backtracking_2_4,backtracking_2_5,backtracking_2_6,backtracking_2_8,backtracking_2_9 = scene_2_0.go_bonfire(backtracking_2_1,backtracking_2_7,backtracking_2_3,backtracking_2_4,backtracking_2_5,backtracking_2_6,backtracking_2_8,backtracking_2_9)
            elif choise == "3":
                backtracking_2_1,backtracking_2_7,backtracking_2_2,backtracking_2_4,backtracking_2_5,backtracking_2_6,backtracking_2_8,backtracking_2_9 = scene_2_0.go_kitchen(backtracking_2_1,backtracking_2_7,backtracking_2_2,backtracking_2_4,backtracking_2_5,backtracking_2_6,backtracking_2_8,backtracking_2_9)
            elif choise == "4":
                scene_2_0.forest_exit()
            else:
                print(" Введено неверно.")
    if backtracking_2_1 == False:
        fight_exit_time, alarm = alarm_timer(fight_exit_time, alarm, name, bandits_leader)
        cooking_time, Bandits_3, Cook, Messenger, Hostler, camp_sugar = cooking_timer(cooking_time, intro_2, Cake, poison_food, Cook, Hostler, Bandits_3, Messenger, alarm, Stunning_exit, flour, camp_sugar)
        backtracking_2_2,backtracking_2_3,backtracking_2_4,backtracking_2_5,backtracking_2_6,backtracking_2_7,backtracking_2_8,backtracking_2_9 = scene_2_1.frame_0(backtracking_2_2,backtracking_2_3,backtracking_2_4,backtracking_2_5,backtracking_2_6,backtracking_2_7,backtracking_2_8,backtracking_2_9)
        while backtracking_2_1 == False:
            if alarm == True and alarm_counter == False:
                alarm_1()
                alarm_counter = True
            if intro_1 == False:
                scene_2_1.intro()
                intro_1 = True
            choise = scene_2_1.frame_1(warning_body)
            if choise == "1":
                if intro_1_1 == False:
                    f = scene_2_1.intro_1()
                    intro_1_1 = True
                while backtracking_2_1 == False:
                    variation = scene_2_1.frame_4(dagger, bandits_leader, alarm, globus_sight,bandits_leader_body)
                    if variation == "1" and globus_sight == False:
                        globus_sight = scene_2_1.frame_7(globus_sight, name, race)
                    elif variation == "1" and globus_sight == True and alarm == False and bandits_leader == False:
                        sleep_sight = scene_2_1.frame_8(name, sleep_sight)
                        while backtracking_2_1 == False:
                            variant = scene_2_1.frame_9(memory, assasin)
                            if variant == "1" and assasin == False:
                                scene_2_1.frame_11(assasin)
                                break
                            elif variant == "2" and assasin == False and memory == False:
                                memory = scene_2_1.frame_12(memory, name)
                            elif variant == "3":
                                d, e, tavern, sleep_kill, bandits_leader = scene_2_1.frame_16(d, e, memory,tavern, name, assasin,sleep_kill, bandits_leader)
                                if sleep_kill == True:
                                    break
                            elif variant == "4" and assasin == False:
                                while backtracking_2_1 == False:
                                    var, c = scene_2_1.frame_13(c, tavern)
                                    if var == "1":
                                        print(" Вы вернулись к шару.")
                                        break
                                    elif var == "2" and tavern == True:
                                        assasin = scene_2_1.frame_15(assasin)
                                        break
                                    elif var == "3":
                                        voice = scene_2_1.frame_14(voice)
                                    else:
                                        print(" Введено неверно.")
                            else:
                                print(" Введено неверно.")
                        if sleep_kill == True:
                            time.sleep(1)
                            print(" Вы открываете глаза. Рядом с вами кровать и тумбочка с шаром. Вы смотрите на Громилу. Он мёртв. На лице гримаса ужаса.")
                            print(f"({name}) - Худшая смерть для худшего человека.")
                    elif variation == "2" and dagger == True and alarm == False and bandits_leader == False:
                        alarm, bandits_leader = scene_2_1.frame_5(alarm, bandits_leader)
                        backtracking_2_1,backtracking_2_7,backtracking_2_2,backtracking_2_4,backtracking_2_5,backtracking_2_6,backtracking_2_8,backtracking_2_3 = scene_2_0.go_enter(backtracking_2_1,backtracking_2_7,backtracking_2_2,backtracking_2_4,backtracking_2_5,backtracking_2_6,backtracking_2_8,backtracking_2_3)
                    elif variation == "3" and bandits_leader == True and bandits_leader_body == False:
                        bandits_leader_body, gate_key = scene_2_1.frame_6(name, bandits_leader_body, sleep_kill, gate_key)
                    elif variation == "4":
                        scene_2_1.frame_10()
                        break
                    elif variation == "5":
                        invetory = scene_2_4.inventory_check(inventory, Margancovka, picklock, warehouse_lock, gate_key, gate)
                    else:
                        print(" Введено неверно.")
            elif choise == "2":
                backtracking_2_1,backtracking_2_7,backtracking_2_3,backtracking_2_4,backtracking_2_5,backtracking_2_6,backtracking_2_8,backtracking_2_9 = scene_2_0.go_bonfire(backtracking_2_1,backtracking_2_7,backtracking_2_3,backtracking_2_4,backtracking_2_5,backtracking_2_6,backtracking_2_8,backtracking_2_9)
            elif choise == "3":
                backtracking_2_1,backtracking_2_7,backtracking_2_2,backtracking_2_4,backtracking_2_5,backtracking_2_6,backtracking_2_8,backtracking_2_3 = scene_2_0.go_enter(backtracking_2_1,backtracking_2_7,backtracking_2_2,backtracking_2_4,backtracking_2_5,backtracking_2_6,backtracking_2_8,backtracking_2_3)
            elif choise == "4":
                backtracking_2_1,backtracking_2_7,backtracking_2_2,backtracking_2_3,backtracking_2_5,backtracking_2_6,backtracking_2_8,backtracking_2_9 = scene_2_0.go_prison(backtracking_2_1,backtracking_2_7,backtracking_2_2,backtracking_2_3,backtracking_2_5,backtracking_2_6,backtracking_2_8,backtracking_2_9)
            elif choise == "5":
                backtracking_2_1,backtracking_2_7,backtracking_2_2,backtracking_2_4,backtracking_2_5,backtracking_2_6,backtracking_2_8,backtracking_2_9 = scene_2_0.go_kitchen(backtracking_2_1,backtracking_2_7,backtracking_2_2,backtracking_2_4,backtracking_2_5,backtracking_2_6,backtracking_2_8,backtracking_2_9)
            elif choise == "6" and warning_body == False:
                warning_body = scene_2_1.frame_2(name, warning_body, race)
            elif choise == "6" and warning_body == True:
                scene_2_1.frame_3()
            elif choise == "7":
                invertory = scene_2_4.inventory_check(inventory, Margancovka, picklock, warehouse_lock, gate_key, gate)
            else:
                print(" Введено неверно.")
    if backtracking_2_2 == False:
        fight_exit_time, alarm = alarm_timer(fight_exit_time, alarm, name, bandits_leader)
        cooking_time, Bandits_3, Cook, Messenger, Hostler, camp_sugar = cooking_timer(cooking_time, intro_2, Cake, poison_food, Cook, Hostler, Bandits_3, Messenger, alarm, Stunning_exit, flour, camp_sugar)
        while backtracking_2_2 == False:
            if alarm == True and alarm_counter == False:
                alarm_1()
                alarm_counter = True
            if intro_2 == False:
                scene_2_2.intro(alarm, Bandits_3, bandits_leader, Cook, Hostler, Messenger, cooking_time)
                intro_2 = True
            choise = scene_2_2.frame_1(Bandits_3, bandits_leader, Cook, Hostler, Messenger, geksogen, intro_7, intro_8)