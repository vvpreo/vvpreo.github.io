#! /usr/bin/python3
# https://www.hackerrank.com/challenges/reduce-function/problem?isFullScreen=true

from fractions import Fraction
from functools import reduce

def product(fracs):
    t = reduce(
        lambda f1, f2: Fraction(
            numerator=f1.numerator * f2.numerator,
            denominator=f1.denominator * f2.denominator
        ),
        fracs)
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)

