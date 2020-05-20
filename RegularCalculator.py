"""
Более продвинутый калькулятор
Состоит из 3 блоков:
    1) Парсинг строки на отдельные элементы и последующий перенос в список
    2) Перевод из инфиксной в посфиксную (ОПЗ) нотацию
    3) Решение програмой выражения
"""


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


def isfloat(number: str) -> bool:  # проверка числа на тип float
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
        self.__exp = '(' + exp + ')'
        self.__pos = 0  # указатель положения считывателя строки

    def __read_number(self) -> str:  # вычленение следующего числа (и дробного и многозначного)
        res = ''  # результируещее число
        point = 0
        sign = self.__exp[self.__pos]
        polarity = False  # то проределен ли у числа знак + или -
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

    def make(self) -> list:
        listed_str = []
        token = self.__get_token()
        while token:
            listed_str.append(token)
            token = self.__get_token()

        return listed_str


"""
Переводод выражения из инфиксной нотации в обратную польскую запись
"""


class Converting:  # требуется доделать!
    def __init__(self, exp):
        self.__exp = exp.reverse()  # развернули список для удобства
        self.__prev_token = None  # предыдущий токен
        self.__operands = []  # Стек операндов (например, числа)
        self.__functions = []  # Стек операторов (функций, например +, *, и т.п.)
        self.__pos = 0  # указатель положения считывателя строки

    def __can_pop(self, item):  # проверка на возможность дельнейшего изьятия из списка
        if not self.__functions:  # проверка на не пустой список стека функций
            return False

        head = self.__functions[-1]  # элемент с конца списка
        if not is_function(head):
            return False

        p1 = priority_function(item)
        p2 = priority_function(head)

        return p1 <= p2

    def __get_token(self) -> str:  # изъятие следующего токена
        token = self.__exp.pop()
        self.__pos += 1

        return token

    def make(self):
        token = self.__get_token()  # берем очередной токен(число полностью или знак)

        while token:  # выполняем пока есть символы в строке
            if token.isspace():  # пропускаем пробельный символ
                pass

            elif token.isdigit() or isfloat(token):  # если число
                self.__operands.append(token)

            elif is_function(token):
                # Разруливаем ситуации, когда после первой скобки '(' идет знак + или -
                if self.__prev_token and self.__prev_token == '(' and (token == '+' or token == '-'):
                    self.__operands.append(0)

                # Мы можем вытолкнуть, если оператор c имеет меньший или равный приоритет, чем
                # оператор на вершине стека functions
                # Например, с='+', а head='*', тогда выполнится операция head
                while self.__can_pop(token):
                    self.__execute_function()

                self.__functions.append(token)

            elif token == '(':
                self.__functions.append(token)

            elif token == ')':
                # Выталкиваем все операторы (функции) до открывающей скобки
                while self.__functions and self.__functions[-1] != '(':
                    self.__execute_function()

                # Убираем последнюю скобку '('
                self.__functions.pop()

            # Запоминаем токен как предыдущий
            self.__prev_token = token

            # Получаем новый токен
            token = self.__get_token()

        if self.__functions or len(self.__operands) > 1:
            raise Exception('Неверное выражение: operands={}, functions={}'.format(self.__operands, self.__functions))

        # Единственным значением списка operands будет результат выражения
        return self.__operands[0]


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
    print(parsed_list)


if __name__ == "__main__":
    main()
