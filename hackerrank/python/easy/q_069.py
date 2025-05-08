#! /usr/bin/python3
# https://www.hackerrank.com/challenges/html-parser-part-1/problem?isFullScreen=true

import sys
from io import StringIO

sys.stdin = StringIO('''
4
<!--[if IE 9]>IE9-specific content
<![endif]-->
<div> Welcome to HackerRank</div>
<!--[if IE 9]>IE9-specific content<![endif]-->
'''.strip())

if __name__ == '__main__':
    from html.parser import HTMLParser

    N = int(input().strip())
    text = '\n'.join([input().strip() for _ in range(N)])


    class MyHTMLParser(HTMLParser):
        def handle_data(self, data):
            if data.strip():
                print(f">>> Data\n{data}")

        def handle_comment(self, data):
            if '\n' in data:
                print(f'>>> Multi-line Comment\n{data}')
            else:
                print(f'>>> Single-line Comment\n{data}')



    parser = MyHTMLParser()
    parser.feed(text)
