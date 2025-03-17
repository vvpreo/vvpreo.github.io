#! /usr/bin/python3
# https://www.hackerrank.com/challenges/py-the-captains-room/problem?isFullScreen=true
import sys
from io import StringIO
sys.stdin = StringIO('''
5
1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2 
'''.strip())

import collections


if __name__ == '__main__':
    K = int(input())
    rooms = map(int, input().split())

    for room, i in collections.Counter(rooms).items():
        if i != K:
            print(room)
