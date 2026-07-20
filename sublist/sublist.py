"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 0
SUPERLIST = 1
EQUAL = 2
UNEQUAL = 3


def sublist(list_one: list, list_two):
    # if not list_one and not list_two:
    #     return EQUAL
    # if list_one and not list_two:
    #     return SUPERLIST
    # if not list_one and list_two:
    #     return SUBLIST

    if list_one == list_two:
        return EQUAL
    if len(list_one) == len(list_two):
        return UNEQUAL

    if len(list_one) > len(list_two):
        for index in range(len(list_one) - len(list_two) + 1):
            if list_one[index : index + len(list_two)] == list_two:
                return SUPERLIST
    else:
        for index in range(len(list_two) - len(list_one) + 1):
            if list_two[index : index + len(list_one)] == list_one:
                return SUBLIST

    return UNEQUAL
