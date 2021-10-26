#!/usr/bin/env python3

def solution(string):
    string = list(string)
    string.reverse()
    return ''.join(string)

# Result: Success
# Optimal Solution
#def solution(str):
#  return str[::-1]
