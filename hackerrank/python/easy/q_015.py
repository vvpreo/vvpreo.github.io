#! /usr/bin/python3
# https://www.hackerrank.com/challenges/text-alignment/problem?isFullScreen=true

thikness = int(input())
# thikness = 11
total_width = thikness * 6
plank_width = thikness * 5

H = 'H'
DELIM = ' '

if __name__ == '__main__':

    def is_thinkness_even():
        return thikness % 2 == 0


    def arrow(reversed: bool):
        r = list(range(0, thikness * 2, 2))
        indend = 0
        if reversed:
            r.reverse()
            indend = thikness * 4

        for i in r:
            j = i + 1
            print(
                DELIM * indend +
                (H * j).center(thikness * 2 - 1, DELIM).rstrip()
            )


    # Top arrow
    arrow(False)

    left_indend = int(thikness / 2)


    def straights():
        for _ in range(thikness if is_thinkness_even() else thikness + 1):
            gap = thikness * 3
            print(
                DELIM * left_indend +
                H * thikness +
                DELIM * gap +
                H * thikness
            )


    # Before Plank
    straights()

    # Plank
    plank_height = int(thikness / 2) if is_thinkness_even() else int((thikness + 1) / 2)
    for _ in range(plank_height):
        print(
            DELIM * left_indend +
            H * thikness * 5
        )

    # After Plank
    straights()

    # Bottom Arrow
    arrow(True)

'''
          H
         HHH
        HHHHH
       HHHHHHH
      HHHHHHHHH
     HHHHHHHHHHH
    HHHHHHHHHHHHH
   HHHHHHHHHHHHHHH
  HHHHHHHHHHHHHHHHH
 HHHHHHHHHHHHHHHHHHH
HHHHHHHHHHHHHHHHHHHHH
     HHHHHHHHHHH                                 HHHHHHHHHHH
     HHHHHHHHHHH                                 HHHHHHHHHHH
     HHHHHHHHHHH                                 HHHHHHHHHHH
     HHHHHHHHHHH                                 HHHHHHHHHHH
     HHHHHHHHHHH                                 HHHHHHHHHHH
     HHHHHHHHHHH                                 HHHHHHHHHHH
     HHHHHHHHHHH                                 HHHHHHHHHHH
     HHHHHHHHHHH                                 HHHHHHHHHHH
     HHHHHHHHHHH                                 HHHHHHHHHHH
     HHHHHHHHHHH                                 HHHHHHHHHHH
     HHHHHHHHHHH                                 HHHHHHHHHHH
     HHHHHHHHHHH                                 HHHHHHHHHHH
     HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
     HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
     HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
     HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
     HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
     HHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH
     HHHHHHHHHHH                                 HHHHHHHHHHH
     HHHHHHHHHHH                                 HHHHHHHHHHH
     HHHHHHHHHHH                                 HHHHHHHHHHH
     HHHHHHHHHHH                                 HHHHHHHHHHH
     HHHHHHHHHHH                                 HHHHHHHHHHH
     HHHHHHHHHHH                                 HHHHHHHHHHH
     HHHHHHHHHHH                                 HHHHHHHHHHH
     HHHHHHHHHHH                                 HHHHHHHHHHH
     HHHHHHHHHHH                                 HHHHHHHHHHH
     HHHHHHHHHHH                                 HHHHHHHHHHH
     HHHHHHHHHHH                                 HHHHHHHHHHH
     HHHHHHHHHHH                                 HHHHHHHHHHH
                                            HHHHHHHHHHHHHHHHHHHHH
                                             HHHHHHHHHHHHHHHHHHH
                                              HHHHHHHHHHHHHHHHH
                                               HHHHHHHHHHHHHHH
                                                HHHHHHHHHHHHH
                                                 HHHHHHHHHHH
                                                  HHHHHHHHH
                                                   HHHHHHH
                                                    HHHHH
                                                     HHH
                                                      H
'''
