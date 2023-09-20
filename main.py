import math

def plus(a, b):
    return a + b

def vichit(a, b):
    return a - b

def umnoj(a, b):
    return a * b

def delenie(a, b):
    if b != 0:
        return a / b
    else:
        return "Ошибка: деление на ноль"

def stepen(a, b):
    return a ** b

def koren(a):
    if a >= 0:
        return math.sqrt(a)
    else:
        return "Ошибка: невозможно извлечь квадратный корень из отрицательного числа"

def factorial(a):
    if a == 0 or a == 1:
        return 1
    elif a<0:
        print("Ошибка, введите положительное число")
    else:
        return a * factorial(a-1)

def sine(a):
    return math.sin(math.radians(a))

def cosine(a):
    return math.cos(math.radians(a))

def tangent(a):
    return math.tan(math.radians(a))

def provchisl(prompt):
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("Ошибка: введите число")

def provdeistv(prompt, valid_operators):
    while True:
        operator = input(prompt)
        if operator in valid_operators:
            return operator
        else:
            print("Ошибка: недопустимый оператор")

valid_operators = ['+', '-', '*', '/', '**', 'sqrt', '!', 'sin', 'cos', 'tan']

operator = provdeistv("Введите оператор (+, -, *, /, **, sqrt, !, sin, cos, tan): ", valid_operators)

if operator in ['+', '-', '*', '/', '**']:
    number1 = provchisl("Введите первое число: ")
    number2 = provchisl("Введите второе число: ")

    if operator == '+':
        result = plus(number1, number2)
    elif operator == '-':
        result = vichit(number1, number2)
    elif operator == '*':
        result = umnoj(number1, number2)
    elif operator == '/':
        result = delenie(number1, number2)
    elif operator == '**':
        result = stepen(number1, number2)

elif operator in ['sqrt', '!']:
    number = provchisl("Введите число: ")

    if operator == 'sqrt':
        result = koren(number)
    elif operator == '!':
        result = factorial(number)

elif operator in ['sin', 'cos', 'tan']:
    trigon = provchisl("Введите угол в градусах: ")

    if operator == 'sin':
        result = sine(trigon)
    elif operator == 'cos':
        result = cosine(trigon)
    elif operator == 'tan':
        result = tangent(trigon)

print("Результат:", result)
