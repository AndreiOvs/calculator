import sys
import math

print('для каждого ')

# Функции для каждого действия
def integer_division(a, b):
    return a // b
3                            
def division(a, b):
    return a / b

def remainder(a, b):
    return a % b

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def power(a, b):
    return a ** b

def square_root(a):
    return a ** 0.5

def analyze_number(a):
    result = []

    # Проверяем, целое число или дробное
    if isinstance(a, float) and a.is_integer():
        a = int(a)  # Преобразуем в int, если это фактически целое число
    is_integer = '.' not in str(a)

    # 1) Количество разрядов
    if is_integer:
        result.append(f'1) Количество разрядов: {len(str(a))}')
    else:
        result.append(f'1) Количество разрядов: {len(str(a)) - 1}')

    # 2) Подсчет каждой цифры
    result.append(f'2) Количество цифр в числе:')
    digit_count = {str(i): str(a).count(str(i)) for i in range(10) if str(a).count(str(i)) > 0}
    for digit, count in digit_count.items():
        result.append(f'{digit} - {count} раз(a)')

    # 3) Проверка на четность, только если целое
    if is_integer:
        result.append(f'3) Четное' if int(a) % 2 == 0 else f'3) Нечетное')
    else:
        result.append('3) Число не является целым, поэтому нельзя определить четность')

    # 4) Сумма цифр
    digit_sum = sum(int(e) for e in str(a) if e.isdigit())
    result.append(f'4) Сумма цифр: {digit_sum}')

    # 5) Проверка на простоту, только если целое
    if is_integer and int(a) > 1:
        divisors = [i for i in range(2, int(a // 2) + 1) if int(a) % i == 0]
        if not divisors:
            result.append(f'5) Число {a} - простое')
        else:
            result.append(f'5) Число {a} - не является простым, делители: {divisors}')
    else:
        result.append(f'5) Число {a} - это не целое число или меньше 2, поэтому проверка на простоту невозможна')

    # 6) Проверка на полный квадрат
    if is_integer:
        square = math.isqrt(int(a))
        if square * square == int(a):
            result.append(f'6) {a} - полный квадрат числа {square}')
        else:
            result.append(f'6) {a} - не является полным квадратом')
    else:
        result.append(f'6) Число не является целым, поэтому нельзя проверить полный квадрат')

    # 7) Проверка на полный куб
    if is_integer:
        cube_root = round(int(a) ** (1 / 3))
        if cube_root ** 3 == int(a):
            result.append(f'7) {a} - полный куб числа {cube_root}')
        else:
            result.append(f'7) {a} - не является полным кубом')
    else:
        result.append(f'7) Число не является целым, поэтому нельзя проверить полный куб')

    return "\n".join(result)

def convert_to_decimal(a, base):
    return int(a, base)

# Основной блок программы
def calculator():
    print('Привет, эта программа считает, введенные тобой примеры!🧮')
    print('')
    print('1) Для ПЕРВОГО ТИПА ДЕЙСТВИЙ введи: сначала ДЕЙСТВИЕ, а затем ЧИСЛА,'\
          ' между которыми будет выполняться действие.')
    print('2) Для ВТОРОГО ТИПА ДЕЙСТВИЙ введи: сначала ДЕЙСТВИЕ, а потом ЧИСЛО,'\
          'с которым будет выполняться это действие.')
    print('3) Для ТРЕТЬЕГО ТИПА ДЕЙСТВИЙ введи: сначала ДЕЙСТВИЕ($), потом'\
          'число(в любой системе счисления), ну и систему счисления этого числа.')
    print('')

    g = 0
    while g == 0:
        c = input("Введите действие: ")

        if c in {'//', '/', '%', '+', '-', '*', '**'}:
            a = float(input("Введите первое число: "))
            b = float(input("Введите второе число: "))

            # Выполнение операции
            if c == '//':
                print(integer_division(a, b))
            elif c == '/':
                print(division(a, b))
            elif c == '%':
                print(remainder(a, b))
            elif c == '+':
                print(addition(a, b))
            elif c == '-':
                print(subtraction(a, b))
            elif c == '*':
                print(multiplication(a, b))
            elif c == '**':
                print(power(a, b))

        elif c == '&' or c == '@':
            a = float(input("Введите число: "))

            if c == '&':
                print(square_root(a))
            elif c == '@':
                print(analyze_number(a))

        elif c == '$':
            a = input("Введите число в указанной системе счисления: ")
            base = int(input("Введите систему счисления: "))
            print(convert_to_decimal(a, base))

        else:
            print('Error')
            sys.exit(0)

        print('')
        print('Хочешь еще что-нибудь решить?🙂')
        print('Если хочешь, то напиши - "Да", а если нет, то напиши - "Нет"')
        print('')
        m = input()
        if m.lower() in {'да', 'ДА'}:
            g = 0
        elif m.lower() in {'нет', 'НЕТ'}:
            print('ОК')
            g = 1
        else:
            print('Error')

# Запуск программы
calculator()