#! /usr/bin/python3
# https://www.hackerrank.com/challenges/map-and-lambda-expression/problem?isFullScreen=true
import sys
from io import StringIO

sys.stdin = StringIO('''
5
'''.strip())

# cube = lambda x: x ** 3


cube = lambda x: x


def fibonacci(n: int, v_prev=1, v_prev_prev=0):
    if n >= 1:
        yield v_prev_prev

    if n >= 2:
        yield v_prev

    if n > 2:
        yield v_prev
        v_prev_prev = v_prev
        for _ in range(2, n - 1):
            v_next = v_prev_prev + v_prev
            yield v_next
            v_prev_prev = v_prev
            v_prev = v_next


if __name__ == '__main__':
    for n in range(0, 16):
        n = int(n)
        f = list(map(cube, fibonacci(n)))
        print(f'{n:02}', '---', f'{len(f):02}', '---', f)
