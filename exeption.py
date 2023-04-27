a = int(input("Введиде первое значение : "))
b = int(input("Введиде второе значение : "))

# Деление
try:
    result = int (a / b)
except ZeroDivisionError:
    result = 0
    print("Делить на ноль нельзя")
print("Результат деления: " + str(result))
# Сложение
result2 = int (a + b)
print("Результат сложения: " + str(result2))
# Вычитание
result3 = int (a - b)
print("Результат вычитания: " + str(result3))
# Умножение
result4 = int (a * b)
print("Результат умножения: " + str(result4))