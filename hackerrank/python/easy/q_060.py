#! /usr/bin/python3
# https://www.hackerrank.com/challenges/re-split/problem?isFullScreen=true

import sys
from io import StringIO

sys.stdin = StringIO('''
100,000,000.000
'''.strip())

regex_pattern = r"[.,]"

if __name__ == '__main__':
    import re
    print("\n".join(re.split(regex_pattern, input())))