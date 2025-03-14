#! /usr/bin/python3
# https://www.hackerrank.com/challenges/py-collections-deque/problem?isFullScreen=true
import collections

if __name__ == '__main__':
    N = int(input())
    q = collections.deque()
    for _args in [input().split() for _ in range(N)]:
        operation, args = [_args[0], [int(_args[1])] if len(_args) > 1 else []]
        getattr(q, operation)(*args)

    print(' '.join(map(str, q)))
