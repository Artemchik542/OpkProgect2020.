"""
Самый обыкновенный 'китайский калькулятор' (одно действие)
"""


def main():
    string = input()
    sign = ''
    list_num = []
    for i in range(len(string)):
        if ord("0") <= ord(string[i]) <= ord("9"):
            str_num = ""
            str_num += string[i]
            int_num = int(str_num)
            list_num.append(int_num)
        else:
            sign = string[i]
    if sign == '+':
        print(list_num[0] + list_num[1])
    if sign == '-':
        print(list_num[0] - list_num[1])
    if sign == '*':
        print(list_num[0] * list_num[1])
    if sign == '/':
        print(list_num[0] / list_num[1])


if __name__ == "__main__":
    main()
