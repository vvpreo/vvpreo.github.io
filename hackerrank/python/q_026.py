#! /usr/bin/python3
# https://www.hackerrank.com/challenges/designer-door-mat/problem?isFullScreen=true

PATTERN = '.|.'


def doormat(rows_n: int, cols_m: int):
    draw_line = lambda s: print(s.center(cols_m, '-'))

    mid_row_index = (rows_n / 2 + 1 / 2) - 1
    for i_row in range(0, rows_n):
        if i_row < mid_row_index:
            draw_line(PATTERN * (1 + (i_row * 2)))
        elif i_row == mid_row_index:
            draw_line('WELCOME')
        else:
            p_count = 2 * (-i_row + rows_n) - 1
            draw_line(PATTERN * p_count)


if __name__ == '__main__':
    rows_n, cols_m = map(int, input().split())
    doormat(rows_n, cols_m)


def test_doormat():
    print()
    n = 7
    doormat(n, n * 3)
