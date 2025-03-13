#! /usr/bin/python3
# https://www.hackerrank.com/challenges/py-collections-ordereddict/problem?isFullScreen=true
import collections

if __name__ == '__main__':
    N = int(input())
    Good = collections.namedtuple('Good', 'name paid')
    goods = [Good(*input().rsplit(maxsplit=1)) for _ in range(N)]
    report = collections.OrderedDict()

    for good in goods:
        paid_before = report.get(good.name, 0)
        report[good.name] = paid_before + int(good.paid)

    for good_name, paid in report.items():
        print(good_name, paid)
