#! /usr/bin/python3
# https://www.hackerrank.com/challenges/incorrect-regex/problem?isFullScreen=true
import re
import sys

if __name__ == '__main__':
    user_input = sys.stdin.read()

    for expression in user_input.split('\n')[1:]:
        try:
            re.compile(expression)
            print(True)
        except Exception:
            print(False)
