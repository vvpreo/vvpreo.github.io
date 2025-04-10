#! /usr/bin/python3
# https://www.hackerrank.com/challenges/re-findall-re-finditer/problem?isFullScreen=true

import sys
from io import StringIO

sys.stdin = StringIO('''
rabcdeefgyYhFjkIoomnpOeorteeeeet
'''.strip())
sys.stdin = StringIO('''
match a single character not present in the list below
'''.strip())

consonants = 'qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM'
vowels = 'aeiouAEIOU'


def solution(chars: str):
    import re
    pattern = re.compile(f'(?<=[{consonants}])([{vowels}]+[{vowels}]+)(?=[{consonants}])')
    # print(pattern)
    if groups := re.findall(pattern, chars):
        for g in groups:
            print(g)
    else:
        print(-1)


if __name__ == '__main__':
    chars = input().strip()
    solution(chars)
