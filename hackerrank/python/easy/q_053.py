#! /usr/bin/python3
#

import sys
from io import StringIO

sys.stdin = StringIO('''
0 4 5
1 7 6
0 5 9
1 7 2
'''.strip())

import math


class Points(object):
    def __init__(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __sub__(self, other: 'Points') -> 'Points':
        return Points(self.x - other.x, self.y - other.y, self.z - other.z)

    def dot(self, other: 'Points'):
        return (self.x * other.x) + (self.y * other.y) + (self.z * other.z)

    def cross(self, no: 'Points'):
        # 23 32, 31 13, 12 21
        return Points(
            (self.y * no.z) - (self.z * no.y),
            (self.z * no.x) - (self.x * no.z),
            (self.x * no.y) - (self.y * no.x),
        )

    def absolute(self):
        return pow(((self.x ** 2) + ((self.y ** 2)) + (self.z ** 2)), 0.5)


if __name__ == '__main__':
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)

    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print("%.2f" % math.degrees(angle))
