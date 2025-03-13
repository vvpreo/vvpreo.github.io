#! /usr/bin/python3
# https://www.hackerrank.com/challenges/py-collections-namedtuple/problem?isFullScreen=true
import collections

if __name__ == '__main__':
    N = int(input())
    Student = collections.namedtuple('Student', input())
    students = [Student(*input().split()) for _ in range(N)]
    print(round(sum([int(s.MARKS) for s in students]) / N, 2))
