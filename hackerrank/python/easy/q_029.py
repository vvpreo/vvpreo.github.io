#! /usr/bin/python3
# https://www.hackerrank.com/challenges/itertools-product/problem?isFullScreen=true

if __name__ == '__main__':
    A = [int(v) for v in input().split()]
    B = [int(v) for v in input().split()]

    from itertools import product

    AxB = product(A, B)
    for t in AxB:
        print(t, end=' ')
