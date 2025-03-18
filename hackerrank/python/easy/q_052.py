#! /usr/bin/python3
# https://www.hackerrank.com/challenges/py-check-strict-superset/problem?isFullScreen=true

import sys
from io import StringIO

sys.stdin = StringIO('''
1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
2
1 2 3 4 5
100 11 12
'''.strip())

if __name__ == '__main__':
    set_A = set(map(int, input().split()))
    answers = list()
    for _ in range(int(input())):
        set_B = set(map(int, input().split()))
        answers.append(set_B.issubset(set_A) and len(set_A) > len(set_B))

    print(all(answers))
