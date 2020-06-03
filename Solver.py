"""
Выполнение выражения в обратной польской записи и возвращение ответа
"""

import math

OPERATORS = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}  # словарь из веса каждого оператора

CONSTANTS = {'pi': math.pi, 'e': math.e}  # предопределенные константы

PREF_MATH_FUNC = {'sin': math.sin, 'cos': math.cos, 'tg': math.tan,
                  'asin': math.asin, 'acos': math.acos, 'atg': math.atan,
                  'sqrt': math.sqrt, 'lg': math.log10, 'abs': math.fabs}  # математические функции


class Solver:
    exp = None  # входная, переделанная строка в ОПЗ
    stack = []  # буферный стек элементов


def is_float(number: str) -> bool:  # проверка числа на тип float

    try:
        float(number)
        return True
    except ValueError:
        return False


def execute_math_func(my_solve: Solver, func: str):  # исполнение особой мат. функии из словаря PREF_MATH_FUNC

    special_func = PREF_MATH_FUNC.get(func)
    a = float(my_solve.stack.pop())
    my_solve.stack.append(special_func(a))


def execute_operand_func(my_solve: Solver, operand: str):

    b = float(my_solve.stack.pop())
    a = float(my_solve.stack.pop())
    if operand == '+':
        my_solve.stack.append(a + b)
    elif operand == '-':
        my_solve.stack.append(a - b)
    elif operand == '*':
        my_solve.stack.append(a * b)
    elif operand == '/':
        my_solve.stack.append(a / b)
    elif operand == '^':
        my_solve.stack.append(a ** b)


def main(expression: list) -> float:
    my_solve = Solver()
    my_solve.exp = expression
    my_solve.exp.reverse()  # развернули для удобства
    while my_solve.exp:
        item = my_solve.exp.pop()  # последний элемент в развернутом списке (т.е. первый в начальном)
        if is_float(item):  # если любое число
            my_solve.stack.append(item)
        elif item in OPERATORS:
            execute_operand_func(my_solve, item)
        elif item in CONSTANTS:
            my_solve.stack.append(CONSTANTS.get(item))
        elif item in PREF_MATH_FUNC:
            execute_math_func(my_solve, item)

    return my_solve.stack.pop()  # ответ выражения - это последний элемент stack после работы solver'а
