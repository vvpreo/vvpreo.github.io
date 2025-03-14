#! /usr/bin/python3
# https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem?isFullScreen=true
import itertools

if __name__ == '__main__':
    word, n = input().split()
    combs = list()
    for combination in itertools.combinations_with_replacement(word, int(n)):
        combs.append(''.join(sorted(combination)))

    for combination in sorted(combs):
        print(combination)
