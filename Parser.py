"""
Класс Parsing для перевода строки выражения в удобный список
"""


import math

OPERATORS = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}  # словарь из веса каждого оператора

CONSTANTS = {'pi': math.pi, 'e': math.e}  # предопределенные константы

PREF_MATH_FUNC = {'sin': math.sin, 'cos': math.cos, 'tg': math.tan,
                  'asin': math.asin, 'acos': math.acos, 'atg': math.atan,
                  'sqrt': math.sqrt, 'lg': math.log10, 'abs': math.fabs}  # математические функции (префиксные)


class Parser:
    exp = None  # само наше выражение
    pos = 0  # указатель положения считывателя строки


def read_const_and_func(my_parse: Parser) -> str:  # выцепляем из строчки извесные подстрочки, если таковые имеются
    ans = ''
    check_str = ''
    count = my_parse.pos
    while len(check_str) < len(my_parse.exp) - my_parse.pos:
        check_str = check_str + my_parse.exp[count]
        if check_str in CONSTANTS or check_str in PREF_MATH_FUNC:
            my_parse.pos += len(check_str)
            ans = check_str
            break
        count += 1

    return ans


def is_function(a: str) -> bool:  # проверка на соответствие функции из словаря

    return a in OPERATORS.keys()


def read_number(my_parse: Parser) -> str:  # вычленение следующего числа (и дробного и многозначного)

    res = ''  # результируещее число
    point = 0
    sign = my_parse.exp[my_parse.pos]
    polarity = False  # то определен ли у числа знак + или -

    if sign.isdigit():
        polarity = True

    while sign.isdigit() or sign == '.' or sign == '-' or sign == '+':
        if polarity and is_function(my_parse.exp[my_parse.pos + 1]):
            res += sign
            my_parse.pos += 1
            break
        polarity = True

        if sign == '.':  # проверка на правильность записи float пользователем
            point += 1
            if point > 1:
                raise FloatingPointError
        res += sign
        my_parse.pos += 1

        sign = my_parse.exp[my_parse.pos]

    return res


def get_token(my_parse: Parser) -> str:  # считывание следующего элемента(токена)

    for i in range(my_parse.pos, len(my_parse.exp)):
        item = my_parse.exp[i]
        pref_item = my_parse.exp[i - 1]

        if item.isdigit() or pref_item == '(' and (item == '+' or item == '-'):  # если число (а также со знаком)
            return read_number(my_parse)
        elif item == '(' or item == ')' or is_function(item):  # если скобки или операнд
            my_parse.pos += 1
            return item
        else:  # все остальное из буковок (константы и функции)
            a = read_const_and_func(my_parse)
            if a != '':
                return a

    return ''


def main(expression: str) -> list:  # основа

    my_parse = Parser()
    my_parse.exp = '(' + expression + ')'
    my_parse.exp = my_parse.exp.replace(' ', '')  # убрали пробелы
    listed_str = []
    token = get_token(my_parse)

    while token:
        listed_str.append(token)
        token = get_token(my_parse)

    if listed_str.count('(') != listed_str.count(')'):  # проверка на равенство кол-ва скобок ( и )
        return []  # возвращает пустой список если не провильно

    return listed_str
