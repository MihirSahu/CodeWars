#!/usr/bin/env python3

#Define a function that takes in two non-negative integers aaa and bbb and returns the last decimal digit of a^b
#Note that aaa and bbb may be very large!
#Examples
#last_digit(4, 1)                # returns 4
#last_digit(4, 2)                # returns 6
#last_digit(9, 7)                # returns 9
#last_digit(10, 10 ** 10)        # returns 0
#last_digit(2 ** 200, 2 ** 300)  # returns 6
#Remarks
#JavaScript, C++, R, PureScript
#Since these languages don't have native arbitrarily large integers, your arguments are going to be strings representing non-negative integers instead.


def last_digit(n1, n2):
    n1 = list(map(int, list(str(n1))))[-1]
    n2 = list(map(list(str(n2))))[-1]
    dict = {
        0: 0,
        1: 1,
        2: {2, 4, 8, 6},
        3: {3, 9, 7, 1},
        5: {0, 5},
        7: {7, 9, 3, 1}
    }

# Testing
print(last_digit(4, 2))

# Result: Failure. This kata depends more on the knowlegde of number theory than coding, and I don't feel like learning about that right now
# Optimal Solution. I feel stupid now.
# def last_digit(n1, n2):
#    return pow( n1, n2, 10 )

# This is pretty much exactly what I was trying to do but was just too lazy to finish
#rules = {
#    0: [0,0,0,0],
#    1: [1,1,1,1],
#    2: [2,4,8,6],
#    3: [3,9,7,1],
#    4: [4,6,4,6],
#    5: [5,5,5,5],
#    6: [6,6,6,6],
#    7: [7,9,3,1],
#    8: [8,4,2,6],
#    9: [9,1,9,1],
#}
#def last_digit(n1, n2):
#    ruler = rules[int(str(n1)[-1])]
#    return 1 if n2 == 0 else ruler[(n2 % 4) - 1]
