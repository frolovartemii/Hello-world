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
