#! /usr/bin/python3
# https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true

def swap_case(s):
    swapped = list()
    for letter in s:
        if not letter.isalpha():
            swapped.append(letter)
            continue

        if letter.isupper():
            swapped.append(letter.lower())
        else:
            swapped.append(letter.upper())
    return ''.join(swapped)

