#! /usr/bin/python3
# https://www.hackerrank.com/challenges/py-check-subset/problem?isFullScreen=true

import sys
from io import StringIO

sys.stdin = StringIO('''
3
5
1 2 3 5 6
9
9 8 5 6 3 2 1 4 7
1
2
5
3 6 5 4 1
7
1 2 3 5 6 8 9
3
9 8 2
'''.strip())

if __name__ == '__main__':
    CASES = int(input())
    for case_no in range(CASES):
        _ = input().strip()
        set_A = set(map(int, input().strip().split()))
        _ = input().strip()
        set_B = set(map(int, input().strip().split()))
        print(set_A.issubset(set_B))
