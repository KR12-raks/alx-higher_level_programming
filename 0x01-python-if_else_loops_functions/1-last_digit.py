#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

sign = -1 if number < 0 else 1
number_str = str(number)

if len(number_str) > 0:
        new_digit = int(number_str[-1]) * sign
    else:
            pass

        if new_digit > 5:
                print(f"Last digit of {number} is {new_digit} and is greater than 5")
            elif new_digit == 0:
                    print(f"Last digit of {number} is {new_digit} and is 0")
                elif new_digit < 6:
                        print(f"Last digit of {number} is {new_digit} and is less than 6 and not 0")
