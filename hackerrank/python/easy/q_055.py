#! /usr/bin/python3
# https://www.hackerrank.com/challenges/input/problem?isFullScreen=true

import sys
from io import StringIO

sys.stdin = StringIO('''
1 4
x**3 + x**2 + x + 1
'''.strip())

if __name__ == '__main__':
    x, k = input().split()
    expression = input()
    expression = expression.replace('x', x)
    print(int(k) == eval(expression))
