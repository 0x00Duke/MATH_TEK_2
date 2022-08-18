##
## EPITECH PROJECT, 2021
## 207
## File description:
## ErrorCheck.py
##

from sys import argv as av

class ErrorCheck():
    def usage(self):
        print("USAGE\n")
        print("\t./207demography code [...]\n")
        print("DESCRIPTION")
        print("\tcode\tcountry code")

    def errorCheck(self):
        if "-h" in av or "--help" in av:
            self.usage()
            exit(0)
        if (len(av) < 2):
            exit(84)
