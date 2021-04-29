#!/usr/bin/env python3

# created by: Youngjun Kim
# created on: April 2021
# This program calculates total from adding two number

import math


def main():
    # This function calculates total from adding two number

    # input
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))

    # process
    total = first_number + second_number

    # output
    print("")
    print("Total is {0}.".format(total))
    print("")
    print("Done.")


if __name__ == "__main__":
    main()
