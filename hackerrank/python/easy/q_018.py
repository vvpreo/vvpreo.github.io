#! /usr/bin/python3
# https://www.hackerrank.com/challenges/np-zeros-and-ones/problem?isFullScreen=true

import numpy

if __name__ == '__main__':
    arr = [int(v) for v in input().split()]
    print(numpy.zeros(arr, dtype=int))
    print(numpy.ones(arr, dtype=int))
