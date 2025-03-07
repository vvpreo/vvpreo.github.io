#! /usr/bin/python3
# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?isFullScreen=true

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(set(arr))

    print(sorted(arr, reverse=True)[1])
