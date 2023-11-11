# Код с использованием циклов for и конструкции для обработки ошибок
# try-except - нашел в интернете
import sys # нашел в интернете

print('Привет, эта программа считает, введенные тобой примеры!🧮')
print('')
print('1) Для ПЕРВОГО ТИПА ДЕЙСТВИЙ введи: сначала ДЕЙСТВИЕ, а затем ЧИСЛА,'\
        ' между которыми будет выполняться действие.')
print('2) Для ВТОРОГО ТИПА ДЕЙСТВИЙ введи: сначала ДЕЙСТВИЕ, а потом ЧИСЛО,'\
        'с которым будет выполняться это действие.')
print('3) Для ТРЕТЬЕГО ТИПА ДЕЙСТВИЙ введи: сначала ДЕЙСТВИЕ($), потом'\
        'число(в любой системе счисления), ну и систему счисления этого числа.')
print('')
print('1) ПЕРВЫЙ ТИП ДЕЙСТВИЙ:')
print('')
print('// - целочисленное деление')
print('/ - деление')
print('% - взятие остатка')
print('+ - сложение')
print('- - разность')
print('* - умножение')
print('** - возведение в степепнь')
print('')
print('2) ВТОРОЙ ТИП ДЕЙСТВИЙ:')
print('')
print('& - квадратный корень числа')
print('@ - анализ числа')
print('')
print('3) ТРЕТИЙ ТИП ДЕЙСТВИЙ:')
print('')
print('$ - переводить из любой системы счисления в десятичную')
print('')

g = 0
while g == 0:
    c = input()

    if c == '//' or c == '/' or c == '%' or c == '+' or c =='-' or c == '*' or \
            c == '**':
        a = input()
        try: # нашел в интернете
            int(a)
            a = int(a)
        except: # нашел в интернете
            try: # нашел в интернете
                float(a)
                a = float(a)
            except:
                print('Error')
                sys.exit(0) # нашел в интернете

        b = input()
        try: # нашел в интернете
            int(b)
            b = int(b)
        except: # нашел в интернете
            try: # нашел в интернете
                float(b)
                b = float(b)
            except: # нашел в интернете
                print('Error')
                sys.exit(0) # нашел в интернете

        if c == '//':
            print(a // b)
        elif c =='/':
            print(a / b)
        elif c == '%':
            print(a % b)
        elif c == '+':
            print(a + b)
        elif c == '-':
            print(a - b)
        elif c == '*':
            print(a * b)
        elif c == '**':
            print(a ** b)


    elif c == '&' or c == '@': #1
        a = input()
        try: # нашел в интернете
            int(a)
            a = int(a)
        except: # нашел в интернете
            try: # нашел в интернете
                float(a)
                a = float(a)
            except:
                print('Error')
                sys.exit(0) # нашел в интернете

        if c == '&':
            print(a ** (0.5))
        elif c == '@':
            if '.' in str(a):
                print('1) Количество разрядов:', len(str(a)) - 1)
            elif '.' not in str(a):
                print('1) Количество разрядов:', len(str(a)))

            print('2) Количество цифр в числе:')
            for e in '0123456789':
                cnt = str(a).count(e); # count() - сколько раз символ попадается в строке
                if cnt != 0:
                    print(e, '-', cnt, 'раз(a)')

            if a % 2 == 0:
                print('3) Четное')
            else:
                print('3) Нечетное')

            sum = 0
            for e in str(a):
                if e >= '0' and e <='9':
                    sum = sum + int(e)
            print('4) Сумма цифр:', sum)

            print('5)')
            if '.' in str(a):
                print('Число', a, '- это вообще не целое число😐')
            else:
                a = int(a)
                k = 0
                for i in range(2, a // 2 + 1):
                    if a % i == 0:
                        print(i, 'является делителем', a)
                        k = k + 1
                if k == 0:
                    print('Число', a, '- простое')
                else:
                    print('Число', a, '- не является простым')

            f = a ** (0.5)
            if round(f) - f == 0:
                f = int(f)
                print('6)', a, '- полный квадрат числа', f)
            else:
                print('6)', a, '- не является полным квадратом')

            r = a ** (1 / 3)
            v = (int(r)) ** 3
            s = (int(r) + 1) ** 3
            if v == a:
                print('7)', a, '- полный куб числа', int(r))
            elif s == a:
                print('7)', a, '- полный куб числа', int(r) + 1)
            else:
                print('7)', a, 'не является полным кубом')
    elif c == '$':
        a = input()
        b = int(input())
        print(int(a, b))
    
    else: #1
        print('Error')
        sys.exit(0) # нашел в интернете
    print('')
    print('Хочешь еще что-нибудь решить?🙂')
    print('Если хочешь, то напиши - "Да", а если нет, то напиши - "Нет"')
    print('')
    m = input()
    if m == 'Да' or m == 'да' or m == 'ДА' or m == 'дА':
        g = 0
    elif m == 'Нет' or m == 'нет' or m == 'НЕТ' or m == 'нЕт' or m == 'неТ' or\
            m == 'НеТ' or m == 'НЕт' or m == 'нЕТ':
        print('ОК')
        g = 1
    else:
        print('Error')
