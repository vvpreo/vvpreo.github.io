#! /usr/bin/python3
# https://www.hackerrank.com/challenges/symmetric-difference/problem?isFullScreen=true

if __name__ == '__main__':
    N = int(input())
    N_SET = set(map(int, input().split()))

    M = int(input())
    M_SET = set(map(int, input().split()))

    diff_set = N_SET.difference(M_SET)
    diff_set.update(M_SET.difference(N_SET))

    for val in sorted(diff_set):
        print(val)
