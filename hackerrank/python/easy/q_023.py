#! /usr/bin/python3
# https://www.hackerrank.com/challenges/python-mutations/problem?isFullScreen=true

def mutate_string(string, position, character):
    return string[:position] + character + string[position + 1:]
