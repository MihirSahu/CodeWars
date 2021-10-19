#!/usr/bin/env python3

#The marketing team is spending way too much time typing in hashtags.
#Let's help them with our own Hashtag Generator!
#Here's the deal:
#   It must start with a hashtag (#).
#   All words must have their first letter capitalized, and all letters other than the first letter in the word in lowercase
#   If the final result is longer than 140 chars it must return false.
#   If the input or the result is an empty string it must return false.

#Examples
#" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
#"    Hello     World   "                  =>  "#HelloWorld"
#""                                        =>  false


def generate_hashtag(s):
    # Return False if length is 0 or more than 140 characters
    if len(s) == 0:
        return False
    elif len(s) > 140:
        return False

    # If valid input then do this
    else:
        # Strip front and back whitespaces and split string into a list
        s = list(s.strip())
        # Capitalize the first character
        s[0] = s[0].upper()
        temp = 1
        while (temp < len(s)) and (s[temp] != ' '):
            s[temp] = s[temp].lower()
            temp += 1

        for idx, i in enumerate(s):
            # Don't perform any actions on the first character
            if idx == 0:
                continue
            elif i == ' ':
                # If a whitespace is encountered then change the next character to uppercase
                s[idx + 1] = s[idx + 1].upper()
                # Then change all characters after that first character to lowercase until a whitespace is encountered
                if (idx + 2 < len(s)) and (s[idx + 2] != ' '):
                    idx2 = idx + 2
                    j = s[idx2]
                    while (j != ' ') and (idx2 < len(s)):
                        s[idx2] = j.lower()
                        idx2 += 1
                        if idx2 < len(s):
                            j = s[idx2]
                        else:
                            continue
        s = " ".join(s)
        s = s.replace(' ', '')
        return "#" + s


# Testing
s = "YjBrymuTWSr qyYdjprhJUH NTjChmuWQkr QSDiN mkfbx lbktOqjAiTC HrSzryxDaJX"
print(generate_hashtag(s))


# Result: Success

# Optimal Solution
# def generate_hashtag(s):
#    output = "#"
#
#    for word in s.split():
#        output += word.capitalize()
#
#    return False if (len(s) == 0 or len(output) > 140) else output
