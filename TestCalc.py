"""
Тесты для основной программы RegularCalculator.py
"""

import RegularCalculator


def tests():
    str1 = "2+2"
    str2 = "-2-2"

    assert RegularCalculator.Parsing(str1).make() == ['(', '2', '+', '2', ')'], "Простая ошибка"
    assert RegularCalculator.Parsing(str2).make() == ['(', '-2', '-', '2', ')'], "Ошибка отрицательного числа"


def main():
    tests()


if __name__ == "__main__":
    main()
