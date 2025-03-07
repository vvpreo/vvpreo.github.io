#! /usr/bin/python3
# https://www.hackerrank.com/challenges/capitalize/problem?isFullScreen=true

# Complete the solve function below.


def solve(s: str):
    first_letter = True

    letters = list()

    for l in s:
        if l == ' ':
            letters.append(l)
            first_letter = True
        elif first_letter:
            letters.append(l.upper())
            first_letter = False
        else:
            letters.append(l)

    return ''.join(letters)
