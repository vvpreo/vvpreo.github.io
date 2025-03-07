#! /usr/bin/python3
# https://www.hackerrank.com/challenges/python-string-formatting/problem?isFullScreen=true

def print_formatted(_number):
    fillchars = len(str(bin(_number)[2:]))
    _fmt = lambda s: str(s).rjust(fillchars, ' ').upper()

    for n in range(1, _number + 1):
        print(_fmt(n), _fmt(str(oct(n)[2:])), _fmt(str(hex(n))[2:]), _fmt(str(bin(n)[2:])))


def test_formatted():
    print()
    print_formatted(63)
