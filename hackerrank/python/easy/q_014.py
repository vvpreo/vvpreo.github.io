#! /usr/bin/python3
# https://www.hackerrank.com/challenges/string-validators/problem?isFullScreen=true

if __name__ == '__main__':
    ss = input()

    print(any(s.isalnum() for s in ss))
    print(any(s.isalpha() for s in ss))
    print(any(s.isnumeric() for s in ss))
    print(any(s.islower() for s in ss))
    print(any(s.isupper() for s in ss))
