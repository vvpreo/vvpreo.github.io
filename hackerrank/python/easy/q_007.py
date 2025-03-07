#! /usr/bin/python3
# https://www.hackerrank.com/challenges/python-print/problem?isFullScreen=true

if __name__ == '__main__':
    n = int(input())
    print(''.join([str(i+1) for i in range(n)]))


