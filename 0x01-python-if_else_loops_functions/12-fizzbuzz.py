#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 != 0:
            print("FIzz ", end= '')
        elif i % 5 == 0 i % 3 != 0:
            print("Buzz ", end= '')
        else:
            print("{} ".format(i), end= '')
