def check(a,b):
    if a > b:
        print(a ,"Больше чем " , b)
    elif a < b:
        print(a, "меньше чем " , b )
    else:
        print(a, "равно ", b)

a = int(input("Введите число a = "))
b = int(input("Введите число b = "))
check(a,b)

