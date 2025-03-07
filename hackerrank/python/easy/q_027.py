#! /usr/bin/python3
# https://www.hackerrank.com/challenges/alphabet-rangoli/problem?isFullScreen=true

from string import ascii_lowercase as alphabet


def print_rangoli(size):
    w = list(alphabet[:size][::-1])
    # print("BASE ", w)

    for cl_i in list(range(size)) + list(range(size - 2, -1, -1)):
        w_head = w[:cl_i]
        w_tail = w_head[::-1]
        ww = w_head + [w[cl_i]] + w_tail
        l_ww = '-'.join(ww)
        print(l_ww.center((size + size - 1) * 2 - 1, '-'))


def test_print_rangoli():
    print()
    for i in range(27):
        print(f'RANGOLI {i}')
        print_rangoli(i)
        print()


'''
#size 3

----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----


#size 10

------------------j------------------
----------------j-i-j----------------
--------------j-i-h-i-j--------------
------------j-i-h-g-h-i-j------------
----------j-i-h-g-f-g-h-i-j----------
--------j-i-h-g-f-e-f-g-h-i-j--------
------j-i-h-g-f-e-d-e-f-g-h-i-j------
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
------j-i-h-g-f-e-d-e-f-g-h-i-j------
--------j-i-h-g-f-e-f-g-h-i-j--------
----------j-i-h-g-f-g-h-i-j----------
------------j-i-h-g-h-i-j------------
--------------j-i-h-i-j--------------
----------------j-i-j----------------
------------------j------------------
'''
