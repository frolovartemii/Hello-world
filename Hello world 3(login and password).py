
from random import randint
def crypt_password(password, Key):
    crypt = ""
    for letter in password:
        crypt += chr(ord(letter)^Key)
    return crypt
def sign_up():
    import random
    login = input(" Зарегистрируйте свой логин:  ")
    password = input(" Создайте свой пароль:  ")
    key = randint(1,1000)
    print(login, password)
    file_k = open("key_list.txt", mode="a", encoding="utf-8")
    file_p = open("password_list.txt", mode="a",encoding="utf-8")
    file_l = open("login_list.txt", mode="a", encoding="utf-8")
    file_p.write(f"{crypt_password(password, key)} ")
    file_l.write(f"{crypt_password(login, key)} ")
    file_k.write(f"{key} ")
    file_p.close()
    file_l.close()
    file_k.close()
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
def read_users_k():
    file = open("key_list.txt", mode="r", encoding="utf-8")
    data_k = file.read()
    file.close()
    return data_k.split()
a = ""
b = ""
while a != "3":
    a = input(" Что вы хотите сделать? \n 1 - Зарегестироваться.\n 2 - Войти. \n 3 - Выйти из приложения.\n> ")
    if a == "1":
        sign_up()
    elif a == "2":
        login = input("Добро пожаловать! Введите логин чтобы продолжить: ")
        data = read_users_l()
        data_p = read_users_p()
        data_k = read_users_k()
        b = data.index(login_l)
        key = data_k[b]
        login_1 = crypt_password(login, key)
        if login_1 in data:
            a = data.index(login_1)
            print(f"Логин опознан.\n Здравствуйте {login}! Введите пароль, чтобы мы удостоверились что это вы.")
            enter = input("> ")
            password_true = data_p[b]
            tries = 0
            password_1 = crypt_password(enter, key)
            if password_1 == password_true:
                print("Всё верно. Добро пожаловать!")
                exit()
            if password_1 != password_true and  tries == 0:
                print("Пароль неверен. Пробуйте ещё раз.")
                tries += 1
                enter = input("Введите ваш пароль: ")
                password_1 = crypt_password(enter, 3)
            if password_1 == password_true and tries == 1:
                print("Всё верно. Добро пожаловать!")
                exit()
            elif password_1 != password_true and  tries == 1:
                print("Пароль неверен. Пробуйте ещё раз.")
                tries += 1
                enter = input("Введите ваш пароль: ")
                password_1 = crypt_password(enter, 3)
            if password_1 == password_true and tries == 2:
                print("Всё верно. Добро пожаловать!")
                exit()
            elif password_1 != password_true and tries == 2:
                print("Пароль неверен.Вы использовали максимальное количество попыток. Попробуйте позже или обратитесь в службу поддержки при условии, что вы забыли пароль." )
                exit()
        else:
            print(f"Логин {login} не опознан")
    elif a == "3":
        print("Вы вышли из приложения.")
    else:
        print("Команда не опознана.")