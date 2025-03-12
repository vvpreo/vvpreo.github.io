#! /usr/bin/python3
# https://www.hackerrank.com/challenges/find-angle/problem?isFullScreen=true
import math

if __name__ == '__main__':
    AB = int(input())
    BC = int(input())

    AC = math.sqrt(AB ** 2 + BC ** 2)
    sin_c = AB / AC
    angle_c = math.degrees(math.asin(sin_c))
    angle_c = round(angle_c)
    print(f'{angle_c}\xb0')
