#! /usr/bin/python3
# https://www.hackerrank.com/challenges/py-set-add/problem?isFullScreen=true

if __name__ == '__main__':
    N = int(input().strip())
    C = [input().strip() for _ in range(N)]
    print(len(set(C)))

