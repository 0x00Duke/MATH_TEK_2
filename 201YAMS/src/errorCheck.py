##
## EPITECH PROJECT, 2022
## yams
## File description:
## errorCheck
##

from sys import argv as av

def errorCheck():
    if (len(av) != 7):
        return 84
    for i in range(1, 6):
        if not (av[i].isnumeric()) or not (0 <= int(av[i]) <= 6):
            return 84 
    c = av[6].split('_')
    if c[0] not in ["pair", "three", "four", "full", "straight", "yams"]:
        return 84
    if (c[0] == "full" and len(c) != 3):
        return 84
    if (c[0] == "full" and (not c[1].isnumeric() or not 1 <= int(c[1]) <= 6 or
        not c[2].isnumeric() or not 1 <= int(c[2]) <= 6 or int(c[1]) == int(c[2]))):
        return 84
    if (c[0] == "straight" and (not c[1].isnumeric() or int(c[1]) not in [5,6])):
        print("You can only have a straight ending by 5 or 6\n")
        return 84
    if (c[0] != "full" and len(c) != 2 or (not c[1].isnumeric() or not 1 <= int(c[1]) <= 6)):
        return 84
