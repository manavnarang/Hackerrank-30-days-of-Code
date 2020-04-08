#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    str1 = ""
    arr = list(map(int, input().rstrip().split()))
    arr.reverse()
    for i in arr:
        str1 = str1 + str(i)  + " "
    print(str1)
