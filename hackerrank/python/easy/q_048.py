#! /usr/bin/python3
# https://www.hackerrank.com/challenges/python-power-mod-power/problem?isFullScreen=true

if __name__ == '__main__':
    a = int(input().strip())
    b = int(input().strip())
    m = int(input().strip())

    print(pow(a, b))
    print(pow(a, b, m))
