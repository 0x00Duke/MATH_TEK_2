#!/usr/bin/env python3
##
## EPITECH PROJECT, 2021
## B-MAT-400-BAR-4-1-202unsold-leon.ducasse
## File description:
## errorCheck.py
##

class ErrorCheck():
    def usage(self):
        print("USAGE")
        print("\t./202unsold a b\n")
        print("DESCRIPTION")
        print("\ta\tconstant computed from past results")
        print("\tb\tconstant computed from past results")

    def checkArg(self, av):
        if (len(av) != 3):
            self.usage()
            exit(84)
        if (not av[1].isdigit() or not av[2].isdigit()):
            self.usage()
            exit(84)
        if (int(av[1]) <= 50 or int(av[2]) <= 50):
            self.usage()
            exit(84)
    
    def helper(self, av):
        if (len(av) == 1 or av[1] == "-h"):
            self.usage()
            exit(84)
