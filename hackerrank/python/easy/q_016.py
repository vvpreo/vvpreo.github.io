#! /usr/bin/python3
# https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true

if __name__ == '__main__':
    N = int(input())

    l = list()

    for _ in range(N):
        arr = input().split(maxsplit=3)
        arr3 = [arr[i] if len(arr) > i else None for i in range(3)]
        arr3 = [int(v) if v and v.isnumeric() else v for v in arr3]
        cmd, arg1, arg2 = arr3

        if cmd == 'print':
            print(l)
        elif arg2 is not None:
            getattr(l, cmd)(arg1, arg2)
        elif arg1 is not None:
            getattr(l, cmd)(arg1)
        else:
            getattr(l, cmd)()
