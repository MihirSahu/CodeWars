#!/usr/bin/env python3

import math
import random

def is_prime(num):

    if num < 0:
        return False

    num = abs(num)

    numList = {
        0: False,
        1: False,
        2: True,
        3: True,
        4: False,
        5: True,
        6: False,
        7: True,
        8: False,
        9: False,
    }

    if num in numList.keys():
        return numList[num]

    else:
        for i in range(2, math.ceil(math.sqrt(num))):
            if num % i == 0:
                return False
        return True

# Testing
number = random.randrange(0, 100)
print(is_prime(number))
