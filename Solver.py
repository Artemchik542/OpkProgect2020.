"""
Выполнение выражения в обратной польской записи и возвращение ответа
"""


OPERATORS = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}  # словарь из веса каждого оператора


class Solver:
    exp = None  # входная, переделанная строка в ОПЗ
    stack = []  # буферный стек элементов


def is_float(number: str) -> bool:  # проверка числа на тип float

    try:
        float(number)
        return True
    except ValueError:
        return False


def execute_function(my_solve: Solver, operand: str):

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
    my_solve.exp.reverse()
    while my_solve.exp:
        if is_float(my_solve.exp[-1]):
            my_solve.stack.append(my_solve.exp[-1])
            my_solve.exp.pop()
        elif my_solve.exp[-1] in OPERATORS:
            execute_function(my_solve, my_solve.exp[-1])
            my_solve.exp.pop()

    return my_solve.stack.pop()
