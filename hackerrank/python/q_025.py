#! /usr/bin/python3
# https://www.hackerrank.com/challenges/text-wrap/problem?isFullScreen=true

def wrap(string, max_width):
    return '\n'.join([string[i:i+max_width] for i in range(0, len(string), max_width)])
