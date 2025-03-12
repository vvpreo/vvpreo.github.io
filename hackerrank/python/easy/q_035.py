#! /usr/bin/python3
# https://www.hackerrank.com/challenges/defaultdict-tutorial/problem?isFullScreen=true
import collections


def count_words(nwords: list[str], mwords):
    dd = collections.defaultdict(list)
    for i, wn in enumerate(nwords):
        dd[wn].append(i + 1)

    for wm in mwords:
        indexies = dd[wm]
        if indexies:
            print(' '.join(map(str, indexies)))
        else:
            print(-1)


if __name__ == '__main__':
    n, m = input().split()
    nwords = [input() for _ in range(int(n))]
    mwords = [input() for _ in range(int(m))]
    count_words(nwords, mwords)
