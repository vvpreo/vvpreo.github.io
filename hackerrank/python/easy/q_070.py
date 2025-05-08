#! /usr/bin/python3
# https://www.hackerrank.com/challenges/detect-html-tags-attributes-and-attribute-values/problem?isFullScreen=true

import sys
from io import StringIO

sys.stdin = StringIO('''
9
<head>
<title>HTML</title>
</head>
<object type="application/x-flash" 
  data="your-file.swf" 
  width="0" height="0">
  <!-- <param name="movie" value="your-file.swf" /> -->
  <param name="quality" value="high"/>
</object>
'''.strip())

if __name__ == '__main__':
    from html.parser import HTMLParser

    N = int(input().strip())
    text = '\n'.join([input().strip() for _ in range(N)])


    class MyHTMLParser(HTMLParser):

        def handle_starttag(self, tag, attrs):
            print(tag)
            for attr in attrs:
                print("->", attr[0], ">", attr[1])

        # def handle_endtag(self, tag):
        #     print("End   :", tag)

        def handle_startendtag(self, tag, attrs):
            print(tag)
            for attr in attrs:
                print("->", attr[0], ">", attr[1])


    parser = MyHTMLParser()
    parser.feed(text)
