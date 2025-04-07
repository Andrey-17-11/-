ACTION_MENU = """
Введите действие:

Сложение: +
Вычитание: -
Умножение: *
Деление: /
Возведение в степень: ^
Корень: sqr
Остаток от деления: %

"""

CONTINUE_MENU = """
Что делаем дальше:

1 - Продолжить вычисление с предыдущим результатом
2 - Начать новое вычисление
3 - Просмотр истории операций
4 - Завершить работу программы

"""

def convert_to_int_possible(num):
    '''Преобразует число в int, если оно целое, иначе возвращает float'''
    if num % 1 == 0:
        return int(num)
    else:
        return num

def check_zero_division(num):
    '''Проверяет, является ли число нулём'''
    if num == 0:
        print(f'Ошибка: на ноль делить нельзя!')
        return True
    return False

def calculator(first_num):
    '''Производит вычисления +, -, *, /, ^, корень, остаток и возвращает результат'''
    action = input(f'{ACTION_MENU}\n>>> ')
    try:
        second_num = convert_to_int_possible(float(input('\n>>> Введите второе число: ')))
    except ValueError:
        print(f'Ошибка: введите число!')
        return first_num
    
    if action == '+':
        result = first_num + second_num
        print(f'Результат сложения {first_num} и {second_num}: {result}')

    elif action == '-':
        result = first_num - second_num
        print(f'Результат вычитания из {first_num} числа {second_num}: {result}')

    elif action == '*':
        result = first_num * second_num
        print(f'Результат умножения {first_num} на {second_num}: {result}')

    elif action == '/':
        if check_zero_division(second_num):
            return first_num
        result = first_num / second_num
        print(f'Результат деления {first_num} на {second_num}: {result}')

    elif action == '^':
        if first_num < 0 and isinstance(second_num, float) and not second_num.is_integer():
            print(f'Ошибка: нельзя возвести отрицательное число в дробную степень!')
            return first_num
        result = first_num ** second_num
        print(f'Результат возведения числа {first_num} в степень {second_num}: {result}')

    elif action == 'sqr':
        if second_num == 0:
            print(f'Ошибка: основание корня не может быть нулем!')
            return first_num
        if first_num < 0 and second_num % 2 == 0:
            print(f'Ошибка: нельзя извлечь корень четной степени из отрицательного числа!')
            return first_num
        result = first_num ** (1/second_num)
        if second_num % 2 == 0:
            print(f'Первый корень из числа {first_num} по основанию {second_num}: {result}\nВторой: -{result}')
        else:
            print(f'Корень из числа {first_num} по основанию {second_num}: {result}')

    elif action == '%':
        if check_zero_division(second_num):
            return first_num
        result = first_num % second_num
        print(f'Остаток от деления {first_num} на {second_num}: {result}')

    else:
        print('Ошибка: неизвестное действие!')
        return first_num
    history.append(f'{first_num} {action} {second_num} = {result}')
    return result


user_choice = '2'
history = []

while user_choice != '4':

    if user_choice == '1':
        first_num = result
        result = calculator(first_num)

    elif user_choice == '2':
        try:
            first_num = convert_to_int_possible(float(input('\n>>> Введите первое число: ')))
        except ValueError:
            print('Ошибка: введите число!')
            continue
        result = calculator(first_num)

    elif user_choice == '3':
        print('\nИстория операций:')
        for op in history:
            print(op)

    elif user_choice == '4':
        print(f'Работа программы завершена.')
        break

    user_choice = input(f'{CONTINUE_MENU}\n>>> ')
