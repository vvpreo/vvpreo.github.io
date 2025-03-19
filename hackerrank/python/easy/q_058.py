#! /usr/bin/python3
# https://www.hackerrank.com/challenges/introduction-to-regex/problem?isFullScreen=true
import sys
from io import StringIO

sys.stdin = StringIO('''
4
4.0O0
-1.00
+4.54
SomeRandomStuff
'''.strip())

import re

def time_decorator(func):
    def log(*args, **kwargs):
        import sys
        print(*args, file=sys.stderr, **kwargs)

    import time
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        execution_time = time.time() - start_time
        log(f"Function '{func.__name__}' took {execution_time:.4f} seconds to execute.")
        return result

    return wrapper


@time_decorator
def noreg(val: str):
    # print(val, '---', end=' ')
    if '.' in val:
        if val[-1] in '0123456789':
            try:
                val_num = float(val)
            except:
                pass
            else:
                return True
    return False


@time_decorator
def is_valid_float(s):
    pattern = r'^(?:\+|-)?(?:[1-9]\d*|0)(?:\.\d+)$|^(?:\+|-)?\.\d+$'
    return bool(re.match(pattern, s))


if __name__ == '__main__':
    T = int(input().strip())
    val: str

    for val in [input() for _ in range(T)]:
        print(noreg(val) and is_valid_float(val))
