#! /usr/bin/python3
# https://www.hackerrank.com/challenges/validating-named-email-addresses/problem?isFullScreen=true

import sys
from io import StringIO

sys.stdin = StringIO('''
2  
DEXTER <dexter@hotmail.com>
VIRUS <virus!@variable.:p>
'''.strip())

if __name__ == '__main__':
    email_count = int(input().strip())
    to_validate = [input().strip() for _ in range(email_count)]

    import email.utils

    for email_candidate in to_validate:
        name, email_str = email.utils.parseaddr(email_candidate)
        # print(email_candidate, " --> ", name, email_str)
        if email_str != "":
            print(email.utils.formataddr((name, email_str)))


