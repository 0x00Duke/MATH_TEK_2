#!/usr/bin/env python3
##
## EPITECH PROJECT, 2021
## B-MAT-400-BAR-4-1-203hotline-leon.ducasse
## File description:
## errorCheck.py
##

from sys import argv as av

class ErrorCheck():
    def __init__(self):
        self.checkErrors()

    def usage(self):
        print("USAGE")
        print("\t./203hotline [n k | d]\n")
        print("DESCRIPTION")
        print("\tn\tn value for the computation of C(n, k)")
        print("\tk\tk value for the computation of C(n, k)")
        print("\td\taverage duration of calls (in seconds)")
        exit(84)

    def checkErrors(self):
        if (len(av) == 1 or av[1] in ["-h", "--help"]):
            self.usage()
        if (len(av) not in [2, 3]):
            print("Invalid number of arguments")
            exit(84)
        if (not av[1].isdigit() or (len(av) == 3 and not av[2].isdigit())):
            print("Arguments needs to be numbers")
            exit(84)
        if (int(av[1]) < 0 or (len(av) == 3 and int(av[2]) < 0)):
            print("Numbers need to be positive")
            exit(84)
        if (len(av) == 3 and int(av[1]) - int(av[2]) < 0):
            print("Invalid values n needs to be bigger or equal to k")
            exit(84)
