#! /usr/bin/python3
# https://www.hackerrank.com/challenges/polar-coordinates/problem?isFullScreen=true
import cmath
import math

if __name__ == '__main__':
    c = complex(input())
    print(math.sqrt(c.real ** 2 + c.imag ** 2))
    print(cmath.phase(c))
