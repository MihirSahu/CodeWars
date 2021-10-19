#!/usr/bin/env python3

#In this kata you have to create all permutations of an input string and remove duplicates, if present. This means, you have to shuffle all letters from the input in all possible orders.

#Examples:
#permutations('a'); # ['a']
#permutations('ab'); # ['ab', 'ba']
#permutations('aabb'); # ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
#The order of the permutations doesn't matter.

import math

def calcPermutations(string):
    # Length of string
    stringLength = len(string)
    # Dict of each unique letter in the string and how many times it has been repeated
    uniqueLetterList = {}
    # Number of letters that have been repeated
    numRepeatedLetters = 0
    string = list(string)

    # Add values to uniqueLetterList depending on if letter is already on list or not
    for letter in string:
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

def permutations(string):
    permutationList = []
    numPermutations = calcPermutations(string)
    stringCopy = list(string)
    temp = []

    for idx, i in enumerate(stringCopy):
        temp = []
        for j in range(len(stringCopy)):
            temp = []
            for k in range(len(stringCopy)):
                temp.append()

    return permutationList

print(permutations('aabb'))



# Result: Failure
