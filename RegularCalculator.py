"""
Более продвинутый калькулятор.
Состоит из 3 блоков:
    1) Парсинг строки на отдельные элементы и последующий перенос в список
    2) Перевод из инфиксной в посфиксную (ОПЗ) нотацию
    3) Решение програмой выражения

    Это нужно доделать:
    + обработка иксключений как: 1/0 ; lg(-1); sqrt(-1) и т.д.
"""


import Parser
import Converter
import Solver


def main():

    debug = input('Включить отладку? (y/n): ')
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
        print('Делить на ноль нельзя')
    except IndexError:
        print('Некорректный ввод')
    except FloatingPointError:
        print('В числе больше чем одна точка')
    except ValueError:
        print('Под log число <=0 или взят корень от отрицательного числа')


if __name__ == "__main__":
    main()
