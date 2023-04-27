var_1 = int(input('Введите первое число: '))
var_2 = input('Выберите действие: Сложение: +\n Вычитание -\nУмножение *\n Деление /\n')
var_3 = int(input(' Введите второе число: '))
try:
    result_9 = var_1 / var_3
except ZeroDivisionError:
    result_9 = 0
    print("На ноль делить нельзя")
if(var_2) == '+':
    result_1 = var_1 + var_3
    print(result_1)
    if(var_2) == '-':
        result_2 = var_1 - var_3
        print(result_2)
        if var_2 == '*':
            result_3 = var_1 * var_3
            print(result_3)
            if var_2 == '/':
                result_4 = var_1 / var_3
                print(result_4)