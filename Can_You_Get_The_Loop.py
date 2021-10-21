#You are given a node that is the beginning of a linked list. This list always contains a tail and a loop. Your objective is to determine the length of the loop.
#
#// Use the `getNext()` method to get the following node.
#nodePtr->getNext()
#
#Note: do NOT mutate the nodes!

def loop_size(node):
    nodes = []
    firstNode = ""
    lastNode = ""

    while node not in nodes:
        nodes.append(node)
        if node.next in nodes:
            firstNode = node.next
            lastNode = node
            break
        else:
            node = node.next

    return nodes.index(lastNode) - nodes.index(firstNode) + 1


# Result: Success (kind of). The basic tests were all passed successfully, indicating that the program works, but the 'attempt' after the basic tests timed out because there seems to be too many tests, as stated in the discussions for this kata
# Optimal Solution (This is basically what my code does, which is surprising because my code timed out)
#def loop_size(node):
#    turtle, rabbit = node.next, node.next.next
#
#    # Find a point in the loop.  Any point will do!
#    # Since the rabbit moves faster than the turtle
#    # and the kata guarantees a loop, the rabbit will
#    # eventually catch up with the turtle.
#    while turtle != rabbit:
#        turtle = turtle.next
#        rabbit = rabbit.next.next
#
#    # The turtle and rabbit are now on the same node,
#    # but we know that node is in a loop.  So now we
#    # keep the turtle motionless and move the rabbit
#    # until it finds the turtle again, counting the
#    # nodes the rabbit visits in the mean time.
#    count = 1
#    rabbit = rabbit.next
#    while turtle != rabbit:
#        count += 1
#        rabbit = rabbit.next
#
#    # voila
#    return count
