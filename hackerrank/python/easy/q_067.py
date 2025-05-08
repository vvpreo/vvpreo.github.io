#! /usr/bin/python3
# https://www.hackerrank.com/challenges/hex-color-code/problem?isFullScreen=true

import sys
from io import StringIO

sys.stdin = StringIO('''
  
5
.shadow {
   -moz-box-shadow:    inset 0 0 10px #000000;
   -webkit-box-shadow: inset 0 0 10px #000000;
   box-shadow:         inset 0 0 10px #0z00G0;
}
'''.strip())

if __name__ == '__main__':
    lines_count = int(input().strip())
    lines = [input().strip() for _ in range(lines_count)]
    lines = [line if not line.startswith("#") else line[1:] for line in lines]
    text = "\n".join(lines)

    rgbs = list()
    rgb_lines = text.split("#")
    for c in rgb_lines[1:]:
        c = c.split('\n')[0]
        try:
            if len(c) >= 6:
                val = int(c[0:6], 16)
                print(f'#{c[0:6]}')
            elif len(c) >= 3:
                val = int(c[0:3], 16)
                print(f'#{c[0:3]}')
            else:
                raise Exception("NOT MATCH")
        except Exception as e:
            print("ERR:", c, e, file=sys.stderr)