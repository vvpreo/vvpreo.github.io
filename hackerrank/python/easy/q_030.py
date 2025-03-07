#! /usr/bin/python3
# https://www.hackerrank.com/challenges/itertools-permutations/problem?isFullScreen=true

if __name__ == '__main__':
    in_iter = iter(input().split())
    WORD, K = next(in_iter), int(next(in_iter))

    from itertools import permutations

    result = list(permutations(WORD, K))

    for t in sorted(result):
        print(''.join(t))
