#!/usr/bin/env python3

#Sum of Pairs
#Given a list of integers and a single sum value, return the first two values (parse from the left please) in order of appearance that add up to form the sum.
#
#sum_pairs([11, 3, 7, 5],         10)
##              ^--^      3 + 7 = 10
#== [3, 7]
#
#sum_pairs([4, 3, 2, 3, 4],         6)
##          ^-----^         4 + 2 = 6, indices: 0, 2 *
##             ^-----^      3 + 3 = 6, indices: 1, 3
##                ^-----^   2 + 4 = 6, indices: 2, 4
##  * entire pair is earlier, and therefore is the correct answer
#== [4, 2]
#
#sum_pairs([0, 0, -2, 3], 2)
##  there are no pairs of values that can be added to produce 2.
#== None/nil/undefined (Based on the language)
#
#sum_pairs([10, 5, 2, 3, 7, 5],         10)
##              ^-----------^   5 + 5 = 10, indices: 1, 5
##                    ^--^      3 + 7 = 10, indices: 3, 4 *
##  * entire pair is earlier, and therefore is the correct answer
#== [3, 7]
#Negative numbers and duplicate numbers can and will appear.
#
#NOTE: There will also be lists tested of lengths upwards of 10,000,000 elements. Be sure your code doesn't time out.


def sum_pairs(ints, s):
    output = []
    indexList = []
    val1 = 0
    val2 = 0

    for idx, i in enumerate(ints):
        val1 = i
        #print("Outer loop: " + str(i))
        for j in range(idx + 1, len(ints)):
            #print("Inner loop: " + str(ints[j]))
            #print("Sum: " + str(val1 + ints[j]))
            if val1 + ints[j] == s:
                val2 = ints[j]
                indexList.append(idx)
                indexList.append(j)
    if indexList == []:
        return None
    else:
        smallestIndex = 0
        for i in range(1, len(indexList), 2):
            if (i + 2 < len(indexList)):
                if indexList[i] < indexList[i + 2]:
                    smallestIndex = i
                else:
                    smallestIndex = i + 2
            else:
                output.append(ints[indexList[smallestIndex]])
                output.append(ints[indexList[smallestIndex - 1]])

    return output

# Testing
print(sum_pairs([10, 5, 2, 3, 7, 5], 10))


# Result: Success (kind of). The program outputs the right numbers, but a few are in the wrong order
# Optimal Solution
#def sum_pairs(lst, s):
#    cache = set()
#    for i in lst:
#        if s - i in cache:
#            return [s - i, i]
#        cache.add(i)
