#! /usr/bin/python3
# https://www.hackerrank.com/challenges/np-array-mathematics/problem?isFullScreen=true

import numpy

numpy.set_printoptions(legacy='1.13')

if __name__ == '__main__':
    n, m = [int(v) for v in input().split()]

    arr_a = list()

    for lno in range(n):
        arr_a.append([int(v) for v in input().split()])

    arr_b = list()

    for lno in range(n):
        arr_b.append([int(v) for v in input().split()])

    b = numpy.array(arr_b)
    a = numpy.array(arr_a)

    print(a + b)
    print(a - b)
    print(a * b)
    print(numpy.floor_divide(a, b))
    print(a % b)
    print(a ** b)
