def sum(a, b):
    return a + b

def sub(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return print("На 0 делить нельзя")
    return print(a, "/", b, "=", int(a / b))

a = int(input("Введиде первое значение : "))
b = int(input("Введиде второе значение : "))
op = input("Введите арифметическую операцию (+,-,*,/): ")

if op == "+":
    print(a, "+", b, "=", sum(a, b))
elif op == "-":
    print(a, "-", b, "=", sub(a, b ))
elif op == "*":
    print(a, "*", b, "=", int(multiply(a, b)))
elif op == "/":
    divide(a, b)
else:
    print("Не корректоное арифметическое значение")


# def test_method(a, b)
#     return print(a+b)
#
# print(test_method(1, 2))