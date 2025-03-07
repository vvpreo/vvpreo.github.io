#! /usr/bin/python3
# https://www.hackerrank.com/challenges/find-a-string/problem?isFullScreen=true

def count_substring(string:str, sub_string:str):
    return sum(1 if string[i:].startswith(sub_string) else 0 for i in range(len(string)))


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)

