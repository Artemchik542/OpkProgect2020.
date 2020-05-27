"""
Тесты для основной программы RegularCalculator.py
"""

import RegularCalculator


def tests():
    str1 = "2+2"
    str2 = "2*2-2"
    str3 = "((2+2)*2)^2"
    assert RegularCalculator.Parsing(str1).make() == ['(', '2', '+', '2', ')'], "Простая ошибка парсинга"
    assert RegularCalculator.Parsing(str2).make() == ['(', '2', '*', '2', '-', '2', ')'], "Сложная ошибка парсинга"
    assert RegularCalculator.Parsing(str3).make() == ['(', '(', '(', '2', '+', '2', ')', '*', '2', ')', '^', '2', ')'], "Супер ошибка"
    p_str1 = RegularCalculator.Parsing(str1).make()
    p_str2 = RegularCalculator.Parsing(str2).make()
    p_str3 = RegularCalculator.Parsing(str3).make()
    assert RegularCalculator.Converting(p_str1).make() == ['2', '2', '+'], "Простая ошибка перевода"
    assert RegularCalculator.Converting(p_str2).make() == ['2', '2', '*', '2', '-'], "Сложная ошибка перевода"
    assert RegularCalculator.Converting(p_str3).make() == ['2', '2', '+', '2', '*', '2', '^'], "Супер ошибка"


def main():
    tests()


if __name__ == "__main__":
    main()
