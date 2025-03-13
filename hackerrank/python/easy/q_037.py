#! /usr/bin/python3
# https://www.hackerrank.com/challenges/exceptions/problem?isFullScreen=true

if __name__ == '__main__':
    t = int(input())
    t_nums = [input().split(maxsplit=2) for _ in range(t)]

    for dividend, divisor in t_nums:
        try:
            print(int(dividend) // int(divisor))
        except (ZeroDivisionError,ValueError) as e:
            print(f'Error Code: {e}')

        # except ZeroDivisionError as e:
        #     print(f'Error Code: integer division or modulo by zero')
        # except ValueError as e:
        #     print(f'Error Code: {e}')
