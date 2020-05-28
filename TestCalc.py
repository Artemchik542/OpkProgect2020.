"""
Тесты для основной программы RegularCalculator.py
"""

import RegularCalculator


def func(exp):  # оченьжирняфункция/3
    prs = RegularCalculator.Parsing(exp).make()
    cnv = RegularCalculator.Converting(prs).make()
    ans = RegularCalculator.Solving(cnv).make()
    return ans


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
    c_str1 = RegularCalculator.Converting(p_str1).make()
    assert RegularCalculator.Solving(c_str1).make() == 4, ""
    assert func("2*2") == 4
    assert func("2+2+2+2+2") == 10
    assert func("(2+2)*2") == 8
    assert func("((2+2)*2)^2") == 64
    assert func("(1+1)^(2^(2+1))") == 256
    assert func("-2*(-2)") == 4
    assert func("-1.23456789+1.23456789") == 0
    assert func("2.5*2.0*1/5") == 1


def main():
    tests()


if __name__ == "__main__":
    main()
