#! /usr/bin/python3
# https://www.hackerrank.com/challenges/zipped/problem?isFullScreen=true

import sys
from io import StringIO

sys.stdin = StringIO('''
5 3
89 90 78 93 80
90 91 85 88 86  
91 92 83 89 90.5
'''.strip())

if __name__ == '__main__':
    STUDENTS, SUBJECTS = map(int, input().split())
    per_subjects = [tuple(map(float, input().split())) for _ in range(SUBJECTS)]
    per_students = list(zip(*per_subjects))
    for s in per_students:
        print(sum(s) / SUBJECTS)
