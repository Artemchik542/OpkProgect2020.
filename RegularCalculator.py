"""
Более продвинутый калькулятор.
Состоит из 3 блоков:
    1) Парсинг строки на отдельные элементы и последующий перенос в список
    2) Перевод из инфиксной в посфиксную (ОПЗ) нотацию
    3) Решение програмой выражения
"""
import sys

OPERATORS = {  # словарь из веса каждого оператора
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2,
        '^': 3,
    }


"""
Общие функции для всего
"""


def is_function(a: str) -> bool:  # проверка на соответствие функции из словаря
    return a in OPERATORS.keys()


def priority_function(a: str) -> int:  # возвращение приоритета функции
    if not is_function(a):
        raise Exception('Не найден оператор "{}"'.format(a))

    return OPERATORS[a]


def is_float(number: str) -> bool:  # проверка числа на тип float
    try:
        float(number)
        return True
    except ValueError:
        return False


"""
Класс Parsing для перевода строки выражения в удобный список
"""


class Parsing:  # работает! (не трогать, пока что)
    def __init__(self, exp):
        self.__exp = '(' + exp + ')'  # само наше выражение
        self.__pos = 0  # указатель положения считывателя строки

    def __read_number(self) -> str:  # вычленение следующего числа (и дробного и многозначного)
        res = ''  # результируещее число
        point = 0
        sign = self.__exp[self.__pos]
        polarity = False  # то определен ли у числа знак + или -
        if sign.isdigit():
            polarity = True
        while sign.isdigit() or sign == '.' or sign == '-' or sign == '+':
            if polarity and is_function(self.__exp[self.__pos + 1]):
                res += sign
                self.__pos += 1
                break
            polarity = True

            if sign == '.':  # проверка на правильность записи float пользователем
                point += 1
                if point > 1:
                    raise Exception('Слишком много точек здесь (pos: %s)' % self.__pos)
            res += sign
            self.__pos += 1

            sign = self.__exp[self.__pos]

        return res

    def __get_token(self):  # считывание следующего элемента(токена)
        for i in range(self.__pos, len(self.__exp)):
            item = self.__exp[i]
            pref_item = self.__exp[i - 1]
            if item.isdigit() or pref_item == '(' and (item == '+' or item == '-'):  # обработка знака перед скобкой
                return self.__read_number()
            else:
                self.__pos += 1
                return item

        return None

    def make(self) -> list:  # главный метод Parsing
        self.__exp = self.__exp.replace(' ', '')  # убрали пробелы
        listed_str = []
        token = self.__get_token()
        while token:
            listed_str.append(token)
            token = self.__get_token()

        if listed_str.count('(') != listed_str.count(')'):  # проверка на равенство кол-ва скобок ( и )
            return []

        return listed_str


"""
Переводод выражения из инфиксной нотации в обратную польскую запись
"""


class Converting:  # работает, пока не трогать!
    def __init__(self, exp):
        self.__exp = exp  # входная, уже распарсеная строка
        self.__stack = []  # буферный стек элементов
        self.__output = []  # общий выход(итог) класса Converting в ОПЗ
        self.__pos = 0  # указатель положения считывателя списка

    def get_token(self):
        if self.__pos < len(self.__exp):
            new_token = self.__exp[self.__pos]
            self.__pos += 1
        else:
            return None

        return new_token

    def make(self) -> list:

        token = self.get_token()  # берем очередной токен (число полностью или знак)

        """Здесь применен алгоритм Эдсгера Дейкстра для перевода"""

        while token:  # выполняем пока есть символы в строке

            if token.isdigit() or is_float(token):  # если число то прибавляем его к выходной строке
                self.__output.append(token)

            elif token == '(':  # открывающую скобку сразу помещаем в стек
                self.__stack.append(token)

            elif token == ')':  # выпихиваем из стека все до открывающей скобки (ее саму в конце просто удаляем)
                top_token = self.__stack.pop()
                while top_token != '(':
                    self.__output.append(top_token)
                    if self.__stack:
                        top_token = self.__stack.pop()
                    else:
                        break
                # self.__stack.pop()  # удаление скобки

            elif token in OPERATORS:  # если бинарная операция, то

                while self.__stack[-1] in OPERATORS and priority_function(token) <= priority_function(self.__stack[-1]):
                    self.__output.append(self.__stack.pop())
                self.__stack.append(token)
            token = self.get_token()

        while self.__stack:  # допихиваем все что осталось в стеке в выход
            self.__output.append(self.__stack.pop())

        return self.__output


class Solving:  # тоже требуется доделать!
    def __execute_function(self):  # выполнение выражения
        if len(self.__operands) < 2:
            return

        a, b = self.__operands.pop(), self.__operands.pop()
        f = self.__functions.pop()

        if f == '+':  # можно вернуть запись через словарь
            self.__operands.append(b + a)
        elif f == '-':
            self.__operands.append(b - a)
        elif f == '*':
            self.__operands.append(b * a)
        elif f == '/':
            self.__operands.append(b / a)
        elif f == '^':
            self.__operands.append(b ** a)


def main():
    input_str = input('Введите выражение: ')
    parsed_list = Parsing(input_str).make()  # парсинг строки
    if not parsed_list:
        print("не соответствие скобок")
        sys.exit()
    print(parsed_list)
    converted_list = Converting(parsed_list).make()  # перевод в ОПЗ
    print(converted_list)


if __name__ == "__main__":
    main()
