#! /usr/bin/python3
# https://www.hackerrank.com/challenges/validate-a-roman-number/problem?isFullScreen=true

import sys

regex_pattern = r"^(M|MM|MMM)?(C|CC|CCC|CD|D|DC|DCC|DCCC|CM)?(X|XX|XXX|XL|L|LX|LXX|LXXX|XC)?(I|II|III|IV|V|VI|VII|VIII|IX)?$"

i = 0


def solution(candidate: str):
    global i
    i += 1
    import re
    m = bool(re.match(regex_pattern, candidate))
    print(f'{i:04}', candidate, file=sys.stdout if m else sys.stderr)


if __name__ == '__main__':
    thousands = ["", "M", "MM", "MMM"]
    hundreds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

    for thousand in thousands:
        for hundred in hundreds:
            for ten in tens:
                for one in ones:
                    solution(thousand + hundred + ten + one)
