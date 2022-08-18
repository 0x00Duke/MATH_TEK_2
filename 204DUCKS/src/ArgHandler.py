#!/usr/bin/env python3
##
## EPITECH PROJECT, 2021
## 204ducks
## File description:
## ArgHandler.py
##


class ArgHandler():

    def checkArgs(self, argv):

        def isNum(value):
            try:
                float(value)
            except:
                False
            else:
                return True

        if (len(argv) != 2):
            print("This program works with 2 arguments!\nFor more information execute ./202unsold -h")
            return 84
        elif not isNum(argv[1]):
            print("Value must be a float!\nFor more information execute ./202unsold -h")
            return 84
        elif (float(argv[1]) < 0. or float(argv[1]) > 2.5):
            print("Wrong value!\nFor more information execute ./202unsold -h")
            return 84
        else:
            return 0

    def helper(self, argv):

        if "-h" in argv or "--help" in argv:
            print("USAGE\n"
            "\t./204ducks a\n\n"
            "DESCRIPTION\n"
            "\ta\tconstant")
            return True
        return False