#Write a function that takes a number or a string and gives back the number of permutations without repetitions that can generated using all of its element.; more on permutations here.

#For example, starting with:
#1
#45
#115
#"abc"

#You could respectively generate:
#1
#45,54
#115,151,511
#"abc","acb","bac","bca","cab","cba"

#So you should have, in turn:
#perms(1)==1
#perms(45)==2
#perms(115)==3
#perms("abc")==6

import math

def perms(element):

    # Convert element to string
    element = str(element)

    # Length of string
    stringLength = len(element)
    # Dict of each unique letter in the string and how many times it has been repeated
    uniqueLetterList = {}
    # Number of letters that have been repeated
    numRepeatedLetters = 0
    element = list(element)

    # Add values to uniqueLetterList depending on if letter is already on list or not
    for letter in element:
        if letter in uniqueLetterList:
            uniqueLetterList.update({letter:uniqueLetterList[letter] + 1})
        else:
            uniqueLetterList.update({letter:1})

    # Update numRepeatedLetters based on if value of a key is greater than 1 (if greater than 1 then there was more than one instance of the letter)
    for item in uniqueLetterList:
        if uniqueLetterList.get(item) > 1:
            numRepeatedLetters += 1

    # Calculate how many permutations are possible with the given string
    permutations = 0
    numerator = math.factorial(stringLength)
    denominator = 1

    # Calculate denominator
    for item in uniqueLetterList:
        denominator = denominator * math.factorial(uniqueLetterList.get(item))

    return int(numerator/denominator)


# Testing
print(perms(115))


# Result: Success

# Optimal Solutions
# 1.
#from operator import mul
#from math import factorial
#from functools import reduce
#from collections import Counter
#
#def perms(inp):
#    return factorial(len(str(inp))) // reduce(mul, map(factorial, Counter(str(inp)).values()), 1)

# 2.
#from math import factorial
#def perms(e):
#    e = str(e)
#    n = factorial(len(e))
#    for i in (e.count(i) for i in set(e) if e.count(i)>1):
#        if i:
#            n = n / factorial(i)
#    return n
