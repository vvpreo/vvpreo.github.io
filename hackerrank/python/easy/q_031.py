#! /usr/bin/python3
# https://www.hackerrank.com/challenges/collections-counter/problem?isFullScreen=true
from collections import Counter
from typing import List, Tuple


def print_money_earned(number_of_shoues: int, shue_sizes: List[int], amount_of_clients: int, bids: Tuple[int, int]):
    remains = shue_sizes
    money_earned = 0
    for size, price in bids:
        if size in remains:
            money_earned += price
            remains.remove(size)
    print(f'{money_earned}')


def print_money_earned2(number_of_shoues: int, shue_sizes: List[int], amount_of_clients: int, bids: Tuple[int, int]):
    remains = Counter(shue_sizes)
    money_earned = 0
    for size, price in bids:
        if size in remains and remains[size] != 0:
            money_earned += price
            remains[size] = remains[size] - 1
    print(f'{money_earned}')


if __name__ == '__main__':
    number_of_shoues = int(input())
    shue_sizes: List[int] = [int(x) for x in input().split()]
    amount_of_clients = int(input())
    bids: List[Tuple[int, int]] = [tuple(map(int, input().split(maxsplit=2))) for _ in range(amount_of_clients)]
    print_money_earned2(number_of_shoues, shue_sizes, amount_of_clients, bids)
