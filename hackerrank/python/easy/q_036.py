#! /usr/bin/python3
# https://www.hackerrank.com/challenges/calendar-module/problem?isFullScreen=true
import calendar

if __name__ == '__main__':
    m, d, y = map(int, input().split())

    weekday_index = calendar.weekday(y, m, d)
    weekday_name = calendar.day_name[weekday_index]

    print(weekday_name.upper())


