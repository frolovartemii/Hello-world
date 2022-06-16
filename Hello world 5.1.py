h = 0
g = 0
lisst = []
def robot_jump():
    print("Робот прыгнул")
def robot_forward():
    print("Робот идёт вперёд.")
def robot_backward():
    print("Робот идёт назад.")
def robot_right():
    print("Робот идёт вправо.")
def robot_left():
    print("Робот идёт влево.")
def robot_take(item):
    global lisst
    if len(lisst) > 1:
        print(f"Нельзя взять {item}. Обе ваши руки заняты.")
    else:
        lisst.append(item)
        print(f"Робот взял {item}.")
def robot_put(item):
    global lisst
    if item in lisst:
        lisst.remove(item)
        print(f"Предмет {item} был убран из ваших рук.")
    else:
        print(f"Предмета {item} не находится в ваших руках.")
while True:
    key = input("Нажмите на клавишу " )
    if key == "a":
        h -= 1
        robot_left()
    elif key == "d":
        h += 1
        robot_right()
    elif key == "s":
        g -= 1
        robot_backward()
    elif key == "w":
        g += 1
        robot_forward()
    elif key == " ":
        robot_jump()
    elif key == "f":
        item = input("Что вы хотите дать роботу? ")
        robot_take(item)
    elif key == "q":
        item = input("Что вы хотите убрать из рук? ")
        robot_put(item)
    else:
        print("Команда не опознана")
    if h == 4:
        print("Вы врезались в правую стену. Пробуйте заново.")
        break
    if h == -4:
        print("Вы врезались в правую стену. Пробуйте заново.")
        break
    if g == -4:
        print("Вы врезались в заднюю стену. Пробуйте заново.")
        break
    if g == 4:
        print("Вы врезались в переднюю стену. Пробуйте заново.")
        break