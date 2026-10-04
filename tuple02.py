#!/usr/bin/env python3

import math


def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def main():
    p1 = (1, 2)
    p2 = (6, 5)

    p3 = (4, 4)
    p4 = (6, 6)
    
    print('A ket pont kozti tavolsag:', distance(p1, p2))
    print('A ket pont kozti tavolsag:', distance(p3, p4))

#############################################################################

if __name__ == "__main__":
    main()