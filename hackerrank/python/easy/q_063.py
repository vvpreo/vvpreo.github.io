#! /usr/bin/python3
# https://www.hackerrank.com/challenges/re-start-re-end/problem?isFullScreen=true

import sys
from io import StringIO

sys.stdin = StringIO('''
aaadaa
aa
'''.strip())

if __name__ == '__main__':
    S = input().strip()
    SS = input().strip()

    matched = False
    for i in range(len(S)):
        if S[i:].startswith(SS):
            print((i, i + len(SS) - 1))
            matched = True
        if len(SS) == len(S[i:]):
            break
    if not matched:
        print((-1, -1))
