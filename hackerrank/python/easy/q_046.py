#! /usr/bin/python3
# https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem?isFullScreen=true
import sys
from io import StringIO
from typing import TextIO

sys.stdin = StringIO("""
9
1 2 3 4 5 6 7 8 9
10
pop
remove 9
discard 9
discard 8
remove 7
pop 
discard 6
remove 5
pop 
discard 5
""".strip())

if __name__ == '__main__':
    N = int(input())
    nums = set(map(int, input().strip().split()))
    M = int(input())
    OPS = [input().split() for _ in range(M)]
    OPS = [(i[0], list(map(int, i[1:]))) for i in OPS]

    for op, args in OPS:
        getattr(nums, op)(*args)

    print(sum(nums))
