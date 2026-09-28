# 28.09.2026
import os

name = "Иван"
bulba = "В свободное время я играю на компе, слушаю музыку и иногда подучиваю python"

while True:
    print("1. Имя")
    print("2. Что делаю в свободное время")
    print("3. Выход")
    print("0. Выключи мне пк")
    vybor = input('Что хотите узнать? ')
    if vybor == "1":
        print("Меня зовут", name)
    elif vybor == "2":
        print(bulba)
    elif vybor == "0":
        print("Не, не хочу.")
        break
    elif vybor == "3":
        print("Пока")
        break

# bulba         