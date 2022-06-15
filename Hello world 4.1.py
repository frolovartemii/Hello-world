g_1 = "Dead cells"
g_2 = "Hollow knight"
g_3 = "Elden ring"
g_4 = "God of war"
g_5 = "Resident Evil Village"
g_6 = "Cyberpunk 2077"
g_7 = "Dying Light 2: Stay Human"
g_11 = "The Witcher 3: Wild Hunt"
g_8 = "Horizon Zero Dawn"
g_9 = "Red Dead Redemption 2"
g_10 = "S.T.A.L.K.E.R. 2: Heart of Chornobyl"
available_games=[g_1, g_2, g_3, g_4, g_5, g_6, g_7, g_8, g_9, g_10, g_11]
flag = True
t = 0
game_list = []
wish_list = []
print("Добро пожаловать в Epic Games Stor!")
while flag:
    if t == 0: 
        t += 1
        answer = str(input("Выберите действие: \n 1 - Добавить игру в список желаемого \n 2 - Удалить игру из списка желаемого \n 3 - Купить игру \n 4 - Поиграть в игру \n 5 - Посмотреть ваши иргы \n 6 - Посмотреть список желаемого \n 7 - удалить игру \n 8 - Выйти из EGS \n Ваше действие - "))
        if answer == "1":
            game = input("Какую игру вы хотите внести в список: ")
            if game in available_games:
                wish_list.append(game)
                print(f"Игра {game} добавлена в ваш список желаемого.")
            else:
                print("Игра не опознона или отсутствует в EGS.")
        elif answer == "2":
            if len(wish_list) > 0:
                game = input("Какую игру вы хотите удалить из списка: ")
                if game in wish_list:
                    wish_list.remove(game)
                    print("Игра удалена из списка желаемого.")
                else:
                    print("Игра не опознона или отсутствует в списке желаемого.")
            else:
                print("Список желаемого пуст.")
        elif answer == "3":
            game = input("Какую игру вы хотите купить: ")
            if game in available_games:
                game_list.append(game)
                print(f"Игра {game} куплена.")
            else:
                print("Игра не опознона или отсутствует в EGS.")
        elif answer == "4":
            if len(game_list) > 0:
                game = input("В какую игру вы хотите поиграть: ")
                if game in game_list:
                    print(f"Игра {game} запущена.")
                else:
                    print("Игра не опознона, не куплена или отсутствует в EGS.")
            else:
                print("У вас пока нет игр")
        elif answer == "8":
            confirmation = input("Вы точно хотите выйти из EGS? ")
            if confirmation == "Да" or "да" or "Точно" or "точно" or "Конечно" or "конечно" or "Yes" or "yes":
                print("Вы покидаете EGS. До новых встреч!")
                break
            else:
                print("Ваш ответ не опознан.")
        elif answer == "6":
            if len(wish_list) == 0:
                print("Вы пока не добавляли игр в список желаемого.")
            else:
                print(f"Это ваш список желаемого {wish_list}")
        elif answer == "5":
            if len(game_list) == 0:
                print("У вас пока нет игр.")
            else:
                print(f"Это ваш список игр {game_list}")
        elif answer == "7":
            if len(game_list) > 0:
                game = input("Какую игру вы хотите удалить? ")
                if game in game_list:
                    game_list.remove(game)
                    print(f"Вы удалили {game}.")
                else:
                    print("Данная игра не куплена.")
            else:
                print("У вас нет купленных игр")
        else:
            print("Действие не опознано. Действия выражаются в цифрах от 1 до 7.")
    if t == 1:
        answer = str(input("Выберите ещё одно действие или покиньте магазин(7)"))
        if answer == "1":
            game = input("Какую игру вы хотите внести в список: ")
            if game in available_games:
                wish_list.append(game)
                print(f"Игра {game} добавлена в ваш список желаемого.")
            else:
                print("Игра не опознона или отсутствует в EGS.")
        elif answer == "2":
            if len(wish_list) > 0:
                game = input("Какую игру вы хотите удалить из списка: ")
                if game in wish_list:
                    wish_list.remove(game)
                    print("Игра удалена из списка желаемого.")
                else:
                    print("Игра не опознона или отсутствует в списке желаемого.")
            else:
                print("Список желаемого пуст.")
        elif answer == "3":
            game = input("Какую игру вы хотите купить: ")
            if game in available_games:
                game_list.append(game)
                print(f"Игра {game} куплена.")
            else:
                print("Игра не опознона или отсутствует в EGS.")
        elif answer == "4":
            if len(game_list) > 0:
                game = input("В какую игру вы хотите поиграть: ")
                if game in game_list:
                    print(f"Игра {game} запущена.")
                else:
                    print("Игра не опознона, не куплена или отсутствует в EGS.")
            else:
                print("У вас пока нет игр")
        elif answer == "8":
            confirmation = input("Вы точно хотите выйти из EGS? ")
            if confirmation == "Да" or "да" or "Точно" or "точно" or "Конечно" or "конечно" or "Yes" or "yes":
                print("Вы покидаете EGS. До новых встреч!")
                flag = False
            else:
                print("Ваш ответ не опознан.")
        elif answer == "6":
            if len(wish_list) == 0:
                print("Вы пока не добавляли игр в список желаемого.")
            else:
                print(f"Это ваш список желаемого {wish_list}")
        elif answer == "5":
            if len(game_list) == 0:
                print("У вас пока нет игр.")
            else:
                print(f"Это ваш список игр {game_list}")
        elif answer == "7":
            if len(game_list) > 0:
                game = input("Какую игру вы хотите удалить? ")
                if game in game_list:
                    game_list.remove(game)
                    print(f"Вы удалили {game}.")
                else:
                    print("Данная игра не куплена.")
            else:
                print("У вас нет купленных игр")
        else:
            print("Действие не опознано. Действия выражаются в цифрах от 1 до 7.")