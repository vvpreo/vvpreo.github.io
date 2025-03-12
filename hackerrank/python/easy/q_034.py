#! /usr/bin/python3
# https://www.hackerrank.com/challenges/py-introduction-to-sets/problem?isFullScreen=true


def average(array):
    array_set = set(array)
    avg = sum(set(array_set)) / len(array_set)
    avg = round(avg, 3)
    return avg


def test():
    print()
    print(average([a for a in range(110)]))
