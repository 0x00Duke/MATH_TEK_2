##
## EPITECH PROJECT, 2021
## 205
## File description:
## ErrorCheck.py
##

from sys import argv as av
ac = len(av)

class ErrorCheck():
    def __init__(self):
        self.checkHelp()

    def usage(self):
        print("USAGE")
        print("\t./205IQ u s [IQ1] [IQ2]")
        print("\nDESCRIPTION")
        print("\tu\tmean")
        print("\ts\tstandard deviation")
        print("\tIQ1\tminimum IQ")
        print("\tIQ2\tmaximum IQ")
        exit(0)
    
    def checkIfNum(self, value):
        try:
            int(value)
        except ValueError:
            return False
        else:
            return True

    def checkHelp(self):
        if ac > 1 and av[1] in ["-h", "--help"]:
            self.usage()
        if ac not in [3, 4, 5]:
            exit(84)
        for n in range(1, ac):
            if not self.checkIfNum(av[n]):
                exit(84)
            if (n != 2 and (int(av[n]) < 0 or int(av[n]) > 200)) or (n == 2 and int(av[n]) < 0):
                exit(84)
        if ac == 5 and int(av[3]) >= int(av[4]):
            exit(84)
