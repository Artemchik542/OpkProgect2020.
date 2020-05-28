"""
Более продвинутый калькулятор.
Состоит из 3 блоков:
    1) Парсинг строки на отдельные элементы и последующий перенос в список
    2) Перевод из инфиксной в посфиксную (ОПЗ) нотацию
    3) Решение програмой выражения

    Это нужно доделать
    + дописать константы и еще функции sin cos и тд
"""


import Parser
import Converter
import Solver


def main():

    is_debug = False
    debug = input('Включить отладку? (y/n), остальные символы выход из программы')
    if debug == 'y':
        is_debug = True
    elif debug == 'n':
        is_debug = False
    else:
        return 'Выход'

    try:
        while True:  # бесконечное вычисление выражений пока не будет какой-либо ошибки
            input_str = input('Введите выражение: ')
            parsed_list = Parser.main(input_str)  # парсинг строки
            if not parsed_list:  # возвращается пустым если ошибка
                raise IndexError
            converted_list = Converter.main(parsed_list)  # перевод в ОПЗ
            if is_debug:
                print(parsed_list)
                print(converted_list)
            print(Solver.main(converted_list))
    except ZeroDivisionError:
        return 'Делить на ноль нельзя'
    except IndexError:
        return 'Некорректный ввод'
    except FloatingPointError:
        return 'В числе больше чем одна точка'


if __name__ == "__main__":
    print(main())
