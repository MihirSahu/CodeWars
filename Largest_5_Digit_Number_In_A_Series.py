def largest_five_digit_number(num):

    largest_number = 0

    for i in range(0, len(num) - 4):
        if int("".join(list(num)[i:i+5])) >= largest_number:
            largest_number = int("".join(list(num)[i:i+5]))
    return largest_number

print(largest_five_digit_number("1234567890"))
