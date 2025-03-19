#! /usr/bin/python3
# https://www.hackerrank.com/challenges/any-or-all/problem?isFullScreen=true

import sys
from io import StringIO

sys.stdin = StringIO('''
5
12 9 61 5 14 
'''.strip())

if __name__ == '__main__':
    N = int(input().strip())
    integers = list(map(int, input().split()))
    all_positive = all([i >= 0 for i in integers])
    and_any_palindromic = all_positive and \
                          any([str(i) == ''.join(reversed(str(i))) for i in integers])
    print(and_any_palindromic)
