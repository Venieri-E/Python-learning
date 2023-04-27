var_1 = int(input()) # глобальная переменная
var_2 = int(input()) # глобальная переменная

def summ():
    result = var_1 + var_2
    print("сложение = " + str(result))

def sub():
    result = var_1 - var_2
    print("вычитание = " + str(result))

summ()
sub()