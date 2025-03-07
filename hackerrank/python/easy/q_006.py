#! /usr/bin/python3
# https://www.hackerrank.com/challenges/write-a-function/problem?isFullScreen=true

def is_leap(year):
    leap = False

    r400 = year % 400 == 0
    r100 = year % 100 == 0
    r4 = year % 4 == 0

    return r400 or not r100 and r4


year = int(input())
print(is_leap(year))

