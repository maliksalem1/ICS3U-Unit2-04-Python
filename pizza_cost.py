#!/usr/bin/env python3

# Created by: maliksalem1
# Created on: Sept 2022
# This program calculates the cost of a pizza with the diameter
# from the user

LABOR = 0.75
RENT = 1.00
COST_PER_INCH = 0.50
HST = 0.13

import constants


def main():
    # This function calculates the cost of pizza

    # Input
    diameter = int(input("Enter the diameter of the pizza would like " + "(inch): "))

    # Process
    sub_total = constants.LABOR + constants.RENT + (diameter * constants.COST_PER_INCH)
    total = sub_total + (sub_total * constants.HST)

    # Output
    print("The cost for a {0} inch pizza is ${1:,.2F}".format(diameter, total))
    print("\nDone.")


if __name__ == "__main__":
    main()
