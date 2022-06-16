login_1 = "tenakt"
login_2 = "banuk"
login_3 = "utaru"
login = input("Добро пожаловать! Введите логин чтобы продолжить: ")
while login != login_1 and login != login_2 and login != login_3:
    print(f"Логин {login} неизвестен.")
    login = input("Введите логин повторно: ")
if login == login_1:
    enter = input(f"Здравтсвуйте {login_1}! Введите пароль, чтобы мы удостоверились что это вы: ")
    password = "war"
    tries = 0
    if enter == password:
        print("Всё верно. Добро пожаловать!")
    if enter != password and  tries == 0:
        print("Пароль неверен. Пробуйте ещё раз.")
        tries += 1
        enter = input("Введите ваш пароль: ")
    if enter == password and tries == 1:
        print("Всё верно. Добро пожаловать!")
    elif enter != password and  tries == 1:
        print("Пароль неверен. Пробуйте ещё раз.")
        tries += 1
        enter = input("Введите ваш пароль: ")
    if enter == password and tries == 2:
        print("Всё верно. Добро пожаловать!")
    elif enter != password and tries == 2:
        print("Пароль неверен.Вы использовали максимальное количество попыток. Попробуйте позже или обратитесь в службу поддержки при условии, что вы забыли пароль." )
elif login == login_2:
    password = "earthquake"
    enter = input(f"Здравствуйте {login_2}!Введите ваш пароль, чтобы мы удостоверились что это вы: ")
    tries = 0
    if enter == password:
        print("Всё верно. Добро пожаловать!")
    if enter != password and  tries == 0:
        print("Пароль неверен. Пробуйте ещё раз.")
        tries += 1
        enter = input("Введите ваш пароль: ")
    if enter == password and tries == 1:
        print("Всё верно. Добро пожаловать!")
    elif enter != password and  tries == 1:
        print("Пароль неверен. Пробуйте ещё раз.")
        tries += 1
        enter = input("Введите ваш пароль: ")
    if enter == password and tries == 2:
        print("Всё верно. Добро пожаловать!")
    elif enter != password and tries == 2:
        print("Пароль неверен.Вы использовали максимальное количество попыток. Попробуйте позже или обратитесь в службу поддержки при условии, что вы забыли пароль." )
elif login == login_3:
    password = "nature"
    enter = input(f"Здравствуйте {login_3}! Введите пароль чтобы мы удостоверились что это вы: ")
    if enter == password:
        print("Всё верно. Добро пожаловать!")
    else:
        flag = False
        while enter != password:
            for i in range(2):
                enter = input("Пароль неверен. Пробуйте ещё раз: ")
                if enter == password:
                    break
                if i==1:
                    flag = True
            if flag:
                break
        if enter == password:
            print("Всё верно. Добро пожаловать!")
        else:
            print("Пароль неверен.Вы использовали максимальное количество попыток. Попробуйте позже или обратитесь в службу поддержки при условии, что вы забыли пароль.")