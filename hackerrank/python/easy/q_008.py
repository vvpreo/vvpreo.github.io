#! /usr/bin/python3
# https://www.hackerrank.com/challenges/list-comprehensions/problem?isFullScreen=true

if __name__ == '__main__':
    x = int(input()) + 1
    y = int(input()) + 1
    z = int(input()) + 1
    n = int(input())

    all_dims = [[xi, yi, zi] for xi in range(x) for yi in range(y) for zi in range(z)]

    all_dims = [arr for arr in all_dims if sum(arr) != n]

    print(all_dims)
