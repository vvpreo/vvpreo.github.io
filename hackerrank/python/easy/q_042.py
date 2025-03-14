#! /usr/bin/python3
# https://www.hackerrank.com/challenges/itertools-combinations/problem?isFullScreen=true
import itertools

if __name__ == '__main__':
    word, n = input().split()
    for i in range(1, int(n) + 1):
        combs = list()
        for combination in itertools.combinations(word, i):
            combs.append(''.join(sorted(combination)))

        for combination in sorted(combs):
            print(combination)
