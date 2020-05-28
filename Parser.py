"""
Класс Parsing для перевода строки выражения в удобный список
"""


OPERATORS = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}  # словарь из веса каждого оператора


class Parser:
    exp = None  # само наше выражение
    pos = 0  # указатель положения считывателя строки


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


def get_token(my_parse: Parser):  # считывание следующего элемента(токена)

    for i in range(my_parse.pos, len(my_parse.exp)):
        item = my_parse.exp[i]
        pref_item = my_parse.exp[i - 1]
        if item.isdigit() or pref_item == '(' and (item == '+' or item == '-'):  # обработка знака перед скобкой
            return read_number(my_parse)
        else:
            my_parse.pos += 1
            return item

    return None


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
