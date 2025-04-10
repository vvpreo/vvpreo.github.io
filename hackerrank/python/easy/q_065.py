#! /usr/bin/python3
# https://www.hackerrank.com/challenges/validating-the-phone-number/problem?isFullScreen=true

import sys
from io import StringIO

sys.stdin = StringIO('''
2
9587456281
1252478965
'''.strip())

if __name__ == '__main__':
    N = int(input().strip())
    arr:list[str] = [input().strip() for _ in range(N)]

    for text in arr:
        if text.isnumeric():
            if len(text) == 10:
                if text[0] in ("789"):
                    print("YES")
                    continue
        print("NO")

