"""
Тесты для основной программы RegularCalculator.py
"""

import Parser
import Converter
import Solver


def func(exp: str) -> float:  # функция СразуВсё!
    prs = Parser.main(exp)
    cnv = Converter.main(prs)
    ans = Solver.main(cnv)
    return ans


def tests():

    str1 = "2+2"
    str2 = "2*2-2"
    str3 = "((2+2)*2)^2"

    """ Проверка отдельно парсера (разделителя) """
    assert Parser.main(str1) == ['(', '2', '+', '2', ')'], "Простая ошибка парсинга"
    assert Parser.main(str2) == ['(', '2', '*', '2', '-', '2', ')'], "Сложная ошибка парсинга"
    assert Parser.main(str3) == ['(', '(', '(', '2', '+', '2', ')', '*', '2', ')', '^', '2', ')'], "Супер ошибка"
    p_str1 = Parser.main(str1)
    p_str2 = Parser.main(str2)
    p_str3 = Parser.main(str3)

    """ Проверка отдельно преобразовател в ОПЗ """
    assert Converter.main(p_str1) == ['2', '2', '+'], "Простая ошибка перевода"
    assert Converter.main(p_str2) == ['2', '2', '*', '2', '-'], "Сложная ошибка перевода"
    assert Converter.main(p_str3) == ['2', '2', '+', '2', '*', '2', '^'], "Супер ошибка"

    """ Проверка всей программы в совокупе """
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
