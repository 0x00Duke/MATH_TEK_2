##
## EPITECH PROJECT, 2021
## B-MAT-400-BAR-4-1-209poll-jose-antonio.rodriguez-assalone
## File description:
## ErrorCheck.py
##

from sys import argv as av, stderr

class ErrorCheck():
    def __init__(self):
        self.errorCheck()

    def usage(self):
        print("\033[96mUSAGE")
        print("\033[92m\t./209poll pSize sSize p\n")
        print("\033[96mDESCRIPTION")
        print("\033[92m\tpSize\tsize of the population")
        print("\tsSize\tsize of the sample (supposed to be representative)")
        print("\tp\tpercentage of voting intentions for a specific candidate")

    def isInt(self, val):
        try:
            int(val)
        except ValueError:
            return False
        return True
    
    def isFloat(self, val):
        try:
            float(val)
        except ValueError:
            return False
        return True
    
    def errorCheck(self):
        if "-h" in av or "--help" in av:
            self.usage()
            exit(0)
        if (len(av) != 4):
            print("\033[91mWrong amount of parameters", file=stderr)
            exit(84)
        if not self.isInt(av[1]) or not self.isInt(av[2]) or not self.isFloat(av[3]):
            print("\033[91mpSize and sSize need to be integer and p needs to be a float", file=stderr)
            exit(84)
        if int(av[1]) < int(av[2]):
            print("\033[91mpSize needs to be bigger than sSize", file=stderr)
            exit(84)
        if int(av[1]) <= 0 or int(av[2]) <= 0:
            print("\033[91mpSize and sSize need to be positive", file=stderr)
            exit(84)
        if float(av[3]) < 0.0 or float(av[3]) > 100.0:
            print("\033[91mp needs to be between 0 and 100", file=stderr)
            exit(84)
