#! /usr/bin/python3
# https://www.hackerrank.com/challenges/the-minion-game/problem?isFullScreen=true
from pprint import pprint


def log(*args, **kwargs):
    import sys
    print(*args, file=sys.stderr, **kwargs)


def time_decorator(func):
    import time
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        execution_time = time.time() - start_time
        log(f"Function '{func.__name__}' took {execution_time:.4f} seconds to execute.")
        return result

    return wrapper

@time_decorator
def minion_game(string):
    score_stuart = 0
    score_kevin = 0

    for i in range(len(string)):
        if string[i] not in 'AEIOU':
            score_stuart += len(string) - i
        else:
            score_kevin += len(string) - i

    if score_stuart > score_kevin:
        print('Stuart', score_stuart)
    elif score_stuart < score_kevin:
        print('Kevin', score_kevin)
    else:
        print('Draw')


def test_game():
    print()
    minion_game('BANANA')


#################################################
#################################################
#################################################

