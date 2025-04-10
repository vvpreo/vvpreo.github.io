#! /usr/bin/python3
# https://www.hackerrank.com/challenges/re-group-groups/problem?isFullScreen=true

import sys
from io import StringIO

sys.stdin = StringIO('''
..12345678910111213141516171820212223
'''.strip())
sys.stdin = StringIO('''
..12345
'''.strip())


def solution_1(chars: list[str]):
    prev_char = None
    for char in chars:
        if char == prev_char:
            print(char)
            break
        prev_char = char
    else:
        print(-1)

if __name__ == '__main__':
    chars = input().strip()
    chars = [c for c in chars if c.isalnum()]
    solution_1(chars)
