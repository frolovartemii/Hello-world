import scene1
import scene2
import scene3
import scene4
from Controllers import *
name , race = scene1.race_name()
h = 0
intro2 = 0
intro3 = 0
intro4 = 0
if race == "человек" or "эльф":
    scene1.intro()
    while main_exit == False:
        if backtracking_1 == False:
            backtracking_2, backtracking_3, backtracking_4 = scene1.backtracking_1_1(backtracking_2, backtracking_3, backtracking_4)
            while exit_1 == False:
                choise = scene1.intro_frame_3(Sight, hands, door_1, Key, h, intro2, race)
                if choise == "1":
                    scene1.scene1__frame1()
                elif choise == "2" and Sight == False:
                    Sight = scene1.scene1_frame2(Sight)
                elif choise == "3" and hands == False:
                    if Key:
                        hands = scene1.scene1_frame3(hands)
                    else:
                        print("Это железные наручники, у тебя сильно болит голова, интересно, а каким образом ты собрался их снять без ключа?")
                elif choise == "4" and door_1 == False:
                    door_1 = scene1.scene1_frame4(hands, Sight, door_1)
                elif choise == "5" and Key == False:
                    Key = scene1.scene1_frame5(Key)
                elif choise == "6" and exit_1 == False and door_1 == True and h == 0:
                    exit_1 = scene1.scene1_frame6(Sight, hands, Key, exit_1)
                    h += 1
                elif choise == "7" and h == 1:
                    exit_1 = scene1.scene1_frame7(exit_1, race)
                elif choise == "8":
                    scene1.inventory_check(inventory,sunpriest_key, e, Key, hands, money, powder_poach, powder_case, Margancovka, sugar, poach, elf_claw, flour)
                else:
                    print("Неверно введено, попробуй ещё раз.")
        if backtracking_2 == False:
            backtracking_1, backtracking_3, backtracking_4 = scene2.backtracking_2_1(backtracking_1, backtracking_3, backtracking_4)
            while stair  == False:
                if intro2 == 0:
                    intro2 +=1
                    Sight = scene2.intro_2(Sight)
                choise = scene2.scene2_frame_1(first_hall, stair, body_1, hole, race, money, exit_1)
                if choise == "1" and first_hall == False:
                    first_hall = scene2.scene2_frame_2(race, name, first_hall)
                elif choise == "2"  and stair == False:
                    stair = scene2.scene2_frame_4(stair)
                elif choise == "3" and body_1 == False and first_hall and money == False:
                    money, body_1, body_1_money, powder_poach, sugar = scene2.scene2_frame_3(race, name, money, body_1, poach, body_1_money, powder_poach, sugar)
                elif choise == "4" and hole == False and first_hall:
                    a, b, c, d, powder_line, powder_poach, main_exit, Stels_exit, Margancovka = scene2.scene2_frame_6(a, b, c, d, race, powder_case, powder_poach, powder_line, Margancovka, sugar, main_exit, hands, Stels_exit)
                    if main_exit:
                        break
                elif choise == "5" and exit_1 == True:
                    exit_1, backtracking_2, backtracking_3, backtracking_4 = scene2.scene2_frame_5(race, exit_1, backtracking_2, backtracking_3, backtracking_4)
                    break
                elif choise == "6":
                    scene1.inventory_check(inventory,sunpriest_key, e, Key, hands, money, powder_poach, powder_case, Margancovka, sugar, poach, elf_claw, flour)
                else:
                    print("Неверно введено, попробуй ещё раз.")
            if main_exit:
                break
        if backtracking_3 == False:
            backtracking_1, backtracking_2, backtracking_4 = scene3.backtracking_3_1(backtracking_1, backtracking_2, backtracking_4)
            while rise == False:
                if intro3 == 0:
                    intro3 += 1
                    scene3.intro_3()
                choise = scene3.scene3_frame_1(second_hall, body_2, products_warehouse, arsenal, rise, stair, race)
                if choise == "1" and second_hall == False:
                    second_hall = scene3.scene3_frame_2()
                elif choise == "2" and second_hall == True:
                    elf_claw, body_2 = scene3.scene3_frame_3(name, race, elf_claw, body_2)
                elif choise == "3" and second_hall == True:
                    f, e, powder_case, powder_poach = scene3.scene3_frame_4(e, f, sunpriest_key, Key, race, poach, powder_case, powder_poach, sugar, money, powder_case_BOOM, hands)
                elif choise == "4" and second_hall == True:
                    g, flour, powder_poach, money, sugar = scene3.scene3_frame_5(g, flour, powder_poach, money, sugar, poach)
                elif choise == "5" and second_hall:
                    rise = scene3.scene3_frame_6(rise)
                elif choise == "6" and stair == True:
                    stair, backtracking_1, backtracking_3, backtracking_4 = scene3.scene3_frame_7(race, stair, backtracking_1, backtracking_3, backtracking_4)
                    break
                elif choise == "7":
                    scene1.inventory_check(inventory,sunpriest_key, e, Key, hands, money, powder_poach, powder_case, Margancovka, sugar, poach, elf_claw, flour)
                else:
                    print("Неверно введено, поробуйте ещё раз.")
        if backtracking_4 == False:
            while main_exit == False:
                if intro4 == 0:
                    intro4 += 1
                    scene4.intro(race, name)
                choise = scene4.scene4_frame_1(third_hall, rise, body_3, money)
                if choise == "1" and third_hall == False:
                    third_hall = scene4.scene4_frame_2(name)
                elif choise == "2" and rise == True:
                    rise, backtracking_1, backtracking_2, backtracking_4 = scene4.scene4_frame_3(rise, backtracking_1, backtracking_2, backtracking_4)
                    break
                elif choise == "3" and body_3 == False:
                    body_3, Margancovka, sunpriest_key, poach = scene4.scene4_frame_4(body_3, name, race, Margancovka, sunpriest_key, poach)
                elif choise == "3" and body_3 == True:
                    sugar, sugar_poach, main_exit, Stunning_exit = scene4.scene4_frame_5(name, sugar, sugar_poach, main_exit, powder_case_BOOM, Margancovka, Stunning_exit)
                elif choise == "4" and third_hall == True:
                    powder_case_BOOM, i, powder_case, sugar_hole, sugar = scene4.scene4_frame_6(i, powder_case, powder_case_BOOM, sugar_hole, sugar)
                elif choise == "5" and money == True and third_hall == True:
                    main_exit, Stunning_exit, Margancovka = scene4.scene4_frame_7(main_exit, sugar_poach, Stunning_exit)
                elif choise == "6" and money == True and third_hall == True:
                    main_exit, fight_exit, flour = scene4.scene_frame_8(sugar_hole, main_exit, elf_claw, flour)
                elif choise == "7":
                    scene1.inventory_check(inventory,sunpriest_key, e, Key, hands, money, powder_poach, powder_case, Margancovka, sugar, poach, elf_claw, flour)
                else:
                    print("Неверно введено, попробуй ещё раз.")
            if main_exit:
                break