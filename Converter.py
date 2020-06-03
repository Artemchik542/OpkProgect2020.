"""
Переводод выражения из инфиксной нотации в обратную польскую запись
"""

import math

OPERATORS = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}  # словарь из веса каждого оператора

CONSTANTS = {'pi': math.pi, 'e': math.e}  # предопределенные константы

PREF_MATH_FUNC = {'sin': math.sin, 'cos': math.cos, 'tg': math.tan,
                  'asin': math.asin, 'acos': math.acos, 'atg': math.atan,
                  'sqrt': math.sqrt, 'lg': math.log10, 'abs': math.fabs}  # математические функции


class Converter:
    exp = None  # входная, уже распарсеная строка
    stack = []  # буферный стек элементов
    output = []  # общий выход(итог) класса Converting в ОПЗ
    pos = 0  # указатель положения считывателя списка


def is_constant(a: str) -> bool:  # проверка на соответствие константы из словаря

    return a in CONSTANTS.keys()


def is_float(number: str) -> bool:  # проверка числа на тип float

    try:
        float(number)
        return True
    except ValueError:
        return False


def is_function(a: str) -> bool:  # проверка на соответствие функции из словаря

    return a in OPERATORS.keys()


def priority_function(a: str) -> int:  # возвращение приоритета функции

    if not is_function(a):
        raise Exception('Не найден оператор "{}"'.format(a))

    return OPERATORS[a]


def get_token(my_convert: Converter) -> str:

    if my_convert.pos < len(my_convert.exp):
        new_token = my_convert.exp[my_convert.pos]
        my_convert.pos += 1
    else:
        return ''

    return new_token


def main(expression: list) -> list:
    my_convert = Converter()
    my_convert.exp = expression
    token = get_token(my_convert)  # берем очередной токен (число полностью или знак)

    """Здесь применен алгоритм Эдсгера Дейкстра для перевода (сортировочная станция)"""

    while token:  # выполняем пока есть символы в строке

        if token.isdigit() or is_float(token):  # если число то прибавляем его к выходной строке
            my_convert.output.append(token)

        elif is_constant(token):  # если константа (аналог числа) то тоже к выходу
            my_convert.output.append(token)

        elif token in PREF_MATH_FUNC:  # помещаем префиксную функцию в стек
            my_convert.stack.append(token)

        elif token == '(':  # открывающую скобку сразу помещаем в стек
            my_convert.stack.append(token)

        elif token == ')':  # выпихиваем из стека все до открывающей скобки (ее саму в конце просто удаляем)
            # is_sp_func = False
            top_token = my_convert.stack.pop()
            # if top_token == '(':
            # is_sp_func = True
            while top_token != '(':
                my_convert.output.append(top_token)
                if my_convert.stack:
                    top_token = my_convert.stack.pop()
                else:
                    break
            if my_convert.stack and my_convert.stack[-1] in PREF_MATH_FUNC:  # обработка случая с постфиксными функциями
                token = my_convert.stack.pop()
                my_convert.output.append(token)

        elif token in OPERATORS:  # если бинарная операция, то

            while my_convert.stack[-1] in OPERATORS and \
                    priority_function(token) <= priority_function(my_convert.stack[-1]):
                my_convert.output.append(my_convert.stack.pop())
            my_convert.stack.append(token)
        token = get_token(my_convert)

    while my_convert.stack:  # допихиваем все что осталось в стеке в выход
        my_convert.output.append(my_convert.stack.pop())

    return my_convert.output
