from posixpath import split

def sign_up():
    login = input(" Зарегистрируйте свой логин:  ")
    password = input(" Создайте свой пароль:  ")

    file_p = open("password_list.txt", mode="a",encoding="utf-8")
    file_l = open("login_list.txt", mode="a", encoding="utf-8")
    file_p.write(f"{password}\n")
    file_l.write(f"{login}\n")



# file_p = open("password_list.txt", mode="r",encoding="utf-8")
# print(file_p.read().split())