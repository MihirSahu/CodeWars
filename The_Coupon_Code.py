#!/usr/bin/env python3

"""
Story
Your online store likes to give out coupons for special occasions. Some customers try to cheat the system by entering invalid codes or using expired coupons.

Task
Your mission:
Write a function called checkCoupon which verifies that a coupon code is valid and not expired.

A coupon is no more valid on the day AFTER the expiration date. All dates will be passed as strings in this format: "MONTH DATE, YEAR".

Examples:
checkCoupon("123", "123", "July 9, 2015", "July 9, 2015")  == True
checkCoupon("123", "123", "July 9, 2015", "July 2, 2015")  == False
"""

def check_coupon(entered_code, correct_code, current_date, expiration_date):
    if entered_code == correct_code:
        monthList = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        current_date = current_date.split(' ')
        expiration_date = expiration_date.split(' ')

        if int(current_date[2]) <= int(expiration_date[2]):
            if monthList.index(current_date[0]) < monthList.index(expiration_date[0]):
                return True
            if monthList.index(current_date[0]) == monthList.index(expiration_date[0]):
                if int(current_date[1][:-1]) <= int(expiration_date[1][:-1]):
                    return True
    return False

# Testing
print(check_coupon("123", "123", "July 9, 2015", "July 9, 2015")) #True
print(check_coupon("123", "123", "July 9, 2015", "July 2, 2015")) #False
print(check_coupon('123','123','September 5, 2014','October 1, 2014')) #True
print(check_coupon('123a','123','September 5, 2014','October 1, 2014')) #False
