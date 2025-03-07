#! /usr/bin/python3
# https://www.hackerrank.com/challenges/np-eye-and-identity/problem?isFullScreen=true

import numpy

numpy.set_printoptions(legacy='1.13')

if __name__ == '__main__':
    n, m = [int(v) for v in input().split()]
    print(numpy.eye(n, m))
