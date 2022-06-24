def random_game():
    import random
    print("Игра в удачу. Компьютер рандомно выбрал число от 1 до 100, твоя цель угадать его за 7 попытки. Компьютер будет давать тебе подсказки после неудачных попыток")
    secret_nummer = random.randint(1,100)
    user_nummer = int(input("Введи своё число "))
    tries = 6
    h = 0
    if user_nummer == secret_nummer:
        print(f"Победа! Правильный ответ {secret_nummer}.")
        tries -= 7
        h += 1
    elif user_nummer + 30 < secret_nummer:
        print("Ваше число намного меньше загаданного. У вас осталось 6 попыток")
    elif user_nummer < secret_nummer:
        print("Ваше число меньше загаданного. У вас осталось 6 попыток")
    elif user_nummer - 30 > secret_nummer:
        print("Ваше число намного больше загаданного. У вас осталось 6 попыток")
    elif user_nummer > secret_nummer:
        print("Ваше число больше загаданного. У вас осталось 6 попыток")
    while tries > -1:
        user_nummer = int(input("Введи своё число "))
        if user_nummer == secret_nummer:
            print(f"Победа! Правильный ответ {secret_nummer}.")
            h += 1
            break
        elif user_nummer < secret_nummer:
            print(f"Ваше число меньше загаданного. У вас осталось {tries} попыток")
        elif user_nummer > secret_nummer:
            print(f"Ваше число больше загаданного. У вас осталось {tries} попыток")
        tries -= 1
    if h == 0:
        print(f"Увы ты проиграл( Правильный ответ - {secret_nummer}.Попробуй ещё раз и у тебя точно получится!")
def mortal_combat():
    import random
    import time
    class Character:
        def __init__(self, name, ultimate):
            self.name = name
            self.mana = 0
            self.ultimate = ultimate
            self.health = 100
        def attack(self, enemy_name, enemy_health):
            a = random.randint(1,5)
            c = random.randint(1,10)
            enemy_health -= a
            self.mana += c
            # if self.mana == 50:
            #     if self.name == "Саб Зиро":
            #         g = random.randint(1,2)
            #         if g == 1:
            #             enemy_health -= 100
            #             print(" Саб Зиро начал замораживать конечности противника и отбивать их по очереди. В конце от противника осталось только тело.")
            #         if g == 2:
            #             enemy_health -= 100
            #         print(" Саб Зиро заморозил противнику ноги, потом руки и приморозил их к полу. После он призвал мамонта из льда, и тот растоптал врага.")
            #     if self.name == "Оборотень":
            #         g = random.randint(1,2)
            #         if g == 1:
            #             enemy_health -= 100
            #             print(" Оборотень набрасывается на противника и валит его на пол. Он воет призывая волков, даёт испить врагу свою кровь и позоляет волкам разорвать врага. Поссле того как волки закончили, один из волков падает на землю и начинает превращаться в противника. Теперь ваш противник ваш союзник.")
            #         if g == 2:
            #             enemy_health -= 100
            #             print(" Оборотень начинает выть призывая стаю волков, после бросается на противника и валит его на землю. Прибегают волки и вместе с оборотнем начинают пожирать противника.")
            #     if self.name == "Терминатор":
            #         g = random.randint(1,2)
            #         if g == 1:
            #             enemy_health -= 100
            #             print(" Терминатор призывает бак с лавой и стреляет дробовиком в противника, тот контузится. Терминатор хватает врага и засовывает рукой в бак с лавой. После того как противник расплавился, Терминатор вытащил железную руку и сделал палец вверх.")
            #         if g == 2:
            #             enemy_health -= 100
            #             print("")
                #     if self.name == "Демогорган":
                #         g = random.randint(1,2)
                #         if g == 1:
                #             print("")
                #         if g == 2:
                #             print("")
                #     if self.name == "Вампыр":
                #         g = random.randint(1,2)
                #         if g == 1:
                #             print("")
                #         if g == 2:
                #             print("")
                #     if self.name == "Леший":
                #         g = random.randint(1,2)
                #         if g == 1:
                #             print("")
                #         if g == 2:
                #             print("")
            print(f"{enemy_name} был ранен и потерял {a} здоровья.")
            return enemy_health
    Sub_zero = Character (name = "Саб Зиро", ultimate=["Охлаждение конечностей", "Заморозка"])
    Werewolf = Character ("Оборотень" ,ultimate=["разрыв на части", "Обращение"])
    Terminator = Character ("Терминатор", ["Отправление в лаву","Убийство из дробовика"])
    Demogorgen = Character ("Демогорган", ["Отправка на ту сторону", "Разжирание плоти"])
    Vampyr = Character ("Вампыр", ["Обращенние в подчинённого", "Высасывание крови"])
    Leshiy = Character ("Леший", ["Вечная связь","Животная атака"])
    def Fight():
        enemy_list=[Sub_zero,Werewolf,Terminator, Vampyr, Leshiy, Demogorgen]
        enemy_1 = random.choice(enemy_list)
        enemy_list.remove(enemy_1)
        enemy_2 = random.choice(enemy_list)
        print(f" {enemy_1.name} VS {enemy_2.name}")
        time.sleep(5)
        while enemy_1.health >= 0 and enemy_2.health >= 0:
            time.sleep(1)
            if random.randint(1,2) == 1:
                enemy_2.health=enemy_1.attack(enemy_2.name, enemy_2.health)
            else:
                print(f"{enemy_1.name} промахнулся.")
            if random.randint(1,2) ==1:
                enemy_1.health = enemy_2.attack(enemy_1.name, enemy_1.health)
            else:
                print(f"{enemy_2.name} промахнулся.")
            print(f"{enemy_1.health} - Здоровье {enemy_1.name}. {enemy_2.health} - Здоровье {enemy_2.name}.")
        if enemy_1.health < enemy_2.health:
            print(f"{enemy_2.name} WINS!")
        elif enemy_1.health > enemy_2.health:
            print(f"{enemy_1.name} WINS")
        else:
            print("DRAW!")
def crypt_password(password, Key):
    crypt = ""
    Key = 48
    for letter in password:
        crypt += chr(ord(letter)^Key)
    return crypt
def loading():
    from progress.bar import ShadyBar
    import time
    with ShadyBar('Загрузка', max=10) as ShadyBar:
        for i in range(10):
            # Do some work
            ShadyBar.next()
            time.sleep(1)
def sign_up():
    import random
    login = input(" Зарегистрируйте свой логин:  ")
    password = input(" Создайте свой пароль:  ")
    print(login, password)
    file_p = open("password_list.txt", mode="a",encoding="utf-8")
    file_l = open("login_list.txt", mode="a", encoding="utf-8")
    file_p.write(f"{crypt_password(password, key)} ")
    file_l.write(f"{crypt_password(login, key)} ")
    file_p.close()
    file_l.close()
def read_users_l():
    file = open("login_list.txt", mode="r", encoding= "utf-8")
    data = file.read()
    file.close()
    return data.split()
def read_users_p():
    file = open("password_list.txt", mode="r", encoding= "utf-8")
    data_p = file.read()
    file.close()
    return data_p.split()
def print_user(login):
    c = ""
    b = ""
    a = ""
    while a != "2":
        loading()
        print(" 1 - Написать что-нибудь в общий чат.")
        print(" 2 - Покинуть общий чат.")
        print(" 3 - Прочесть чат")
        print(" 4 - Поиграть в игру *Угадай число*.")
        print(" 5 - Поставить ставки в Мортал_Комбат.")
        a = input(">")
        if a == "1":
            c = input(" Что вы хотите написать в общий чат?\n")
            file_chat = open("Chat.txt", mode ="a", encoding="utf-8")
            file_chat.write(f"{login}: {c}\n")
            file_chat.close()
        elif a == "2":
            print(" Вы покидаете общий чат.")
            break
        elif a == "3":
            file_chat = open("Chat.txt", mode ="r", encoding="utf-8")
            b = file_chat.read()
            print(b)
        elif a == "4":
            random_game()
        elif a == "5":
            mortal_combat.Fight()
        else:
            print(" Команда не опознана.")
a = ""
b = ""
c = ""
key = 48
while a != "3":
    loading()
    a = input(" Что вы хотите сделать? \n 1 - Зарегестироваться.\n 2 - Войти. \n 3 - Выйти из приложения.\n> ")
    if a == "1":
        sign_up()
    elif a == "2":
        login = input("Добро пожаловать! Введите логин чтобы продолжить: ")
        data = read_users_l()
        data_p = read_users_p()
        login_1 = crypt_password(login, key)
        b = data.index(login_1)
        if login_1 in data:
            a = data.index(login_1)
            print(f"Логин опознан.\n Здравствуйте {login}! Введите пароль, чтобы мы удостоверились что это вы.")
            enter = input("> ")
            password_true = data_p[b]
            tries = 0
            password_1 = crypt_password(enter, key)
            if password_1 == password_true:
                print("Всё верно. Добро пожаловать!")
                print_user(login)
            if password_1 != password_true and  tries == 0:
                print("Пароль неверен. Пробуйте ещё раз.")
                tries += 1
                enter = input("Введите ваш пароль: ")
                password_1 = crypt_password(enter, 3)
            if password_1 == password_true and tries == 1:
                print("Всё верно. Добро пожаловать!")
                print_user(login)          
            elif password_1 != password_true and  tries == 1:
                print("Пароль неверен. Пробуйте ещё раз.")
                tries += 1
                enter = input("Введите ваш пароль: ")
                password_1 = crypt_password(enter, 3)
            if password_1 == password_true and tries == 2:
                print("Всё верно. Добро пожаловать!")
                print_user(login)
            elif password_1 != password_true and tries == 2:
                print("Пароль неверен. Вы использовали максимальное количество попыток. Попробуйте позже или обратитесь в службу поддержки при условии, что вы забыли пароль." )
                exit()
        else:
            print(f"Логин {login} не опознан")
    elif a == "3":
        print("Вы вышли из приложения.")
    else:
        print("Команда не опознана.")