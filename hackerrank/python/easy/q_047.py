#! /usr/bin/python3
# https://www.hackerrank.com/challenges/python-mod-divmod/problem?isFullScreen=true

if __name__ == '__main__':
    a = int(input().strip())
    b = int(input().strip())
    print(int(a / b))
    print(a % b)
    print(divmod(a, b))
