#!/usr/bin/env python3

import string

def rot13(message):
    message = list(message)
    ascii_lowercase = list(string.ascii_lowercase)
    ascii_uppercase = list(string.ascii_uppercase)

    for idx, i in enumerate(message):
        if i in ascii_lowercase:
            #print(i)
            if ascii_lowercase.index(i) + 13 > 25:
                message[idx] = ascii_lowercase[ascii_lowercase.index(i) - 13]
                #print(ascii_lowercase[ascii_lowercase.index(i) - 13])
            else:
                message[idx] = ascii_lowercase[ascii_lowercase.index(i) + 13]
                #print(ascii_lowercase[ascii_lowercase.index(i) + 13])
        elif i in ascii_uppercase:
            #print(i)
            if ascii_uppercase.index(i) + 13 > 25:
                message[idx] = ascii_uppercase[ascii_uppercase.index(i) - 13]
                #print(ascii_uppercase[ascii_uppercase.index(i) - 13])
            else:
                message[idx] = ascii_uppercase[ascii_uppercase.index(i) + 13]
                #print(ascii_uppercase[ascii_uppercase.index(i) + 13])
    return "".join(message)


# Testing
print(rot13("EBG13 rknzcyr."))

# Result: Success
# Optimal Solution
#def rot13(message):
#  return message.encode('rot13')
