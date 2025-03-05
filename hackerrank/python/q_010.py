#! /usr/bin/python3
# https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true

if __name__ == '__main__':
    data = [[input(), float(input())] for _ in range(int(input()))]
    second_lowest_score = sorted(set([s for n, s in data]))[1]
    data_ordered_by_names = sorted(data, key=lambda d: d[0])

    for name, score in data_ordered_by_names:
        if score == second_lowest_score:
            print(name)

