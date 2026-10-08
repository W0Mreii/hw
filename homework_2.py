num = int(input("Введите первое число: "))
numb = int(input("Введите второе число: "))
vybor = input("Знак вычисления: ")

if vybor == "+":
    print(num + numb)
elif vybor == "-":
    print(num - numb)
elif vybor == "*":
    print(num * numb)
elif vybor == "/":
    print(num / numb)
