import random
import scene1
name = input("Введите имя персонажа: ")
print(f"Хм..{name}. Какое интересное имя, ладно, идём дальше.")
race = input("Выберите расу персонажа: \n 1 - Эльф \n 2 - Человек \n 3 - Вампир \n ваша раса - ")
if race == "1":
    race = "эльф"
elif race == "2":
    race = "человек"
elif race == "3":
    race = "вампир"
a = 0
b = 0
door_1 = False
hands = False
Key = False
Sight = False
exit_1 = False
print("""Вы открыли глаза. В нос ударил резкий трупный запах (вероятно он и стал причиной вашего пробуждения). Голова расскалывается от боли. 
Вы пытаетесь встать, но падаете.Ваши руки закованы за спиной в наручниках. С трудом вам удаётся встать.""")
if race == 1 or 2:
    while exit_1 == False:
        if b == 1:
            print("Что будете делать теперь? \n 1 - Голова раскалывается, почему бы не прилечь на это возвышение и не отдохнуть?\n 5 - Осмотреть труп.")
        if Sight == False:
            print(" 2 - Подождать, пока глаза привыкнут к темноте.")
        if hands == False:
            print(" 3 - Попытаться освободить руки.")
        if door_1 == False:
            print(" 4 - Осмотреть стены в поисках выхода.")
        if Key == False:
            print(" 5 - Осмотреть труп.")
        if door_1 == True:
            print(" 6 - осмотреть дверь.")
        if b == 0:
            b += 1
            a = input("""В комнате плохое освященние. Вы смутно видите границы комнаты, в середине комнаты находится небольшое каменное возвышение размером с человека, в углу вы замечаете труп (скорее всего, он и был причиной запаха). Что будете делать? \n 1 - Голова раскалывается, почему бы не прилечь на это возвышение и не отдохнуть? \n 2 - Подождать, пока глаза привыкнут к темноте.\n 3 - Попытаться освободить руки. \n 4 - Осмотреть стены в поисках выхода. \n 5 - Осмотреть труп.  """)
        else:
            a = input(" ")
        if a == 1:
            scene1.scene1__frame1()
        elif a == 2:
            scene1.scene1_frame2(Sight)
            Sight = scene1.scene1_frame2(Sight)
        elif a == 3:
            if Key:
                scene1.scene1_frame3(hands)
                hands = scene1.scene1_frame3(hands)
            else:
                print("Это железные наручники, у тебя сильно болит голова, интересно, а каким образом ты собрался их снять без ключа?")
        elif a == 4:
            scene1.scene1_frame4(hands, Sight, door_1)
            door_1 = scene1.scene1_frame4(hands, Sight, door_1)
        elif a == 5:
            scene1.scene1_frame5(Key)
            Key = scene1.scene1_frame5(Key)
        elif a == 6:
            scene1.scene1_frame6(hands, Key, exit_1)
            exit_1 = scene1.scene1_frame6(Key, exit_1)
