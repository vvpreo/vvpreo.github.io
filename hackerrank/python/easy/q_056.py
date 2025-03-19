#! /usr/bin/python3
# https://www.hackerrank.com/challenges/python-eval/problem?isFullScreen=true

import sys
from io import StringIO

sys.stdin = StringIO('''
print(2 + 3)
'''.strip())

if __name__ == '__main__':
    expression = input()
    eval(expression)
