##
## EPITECH PROJECT, 2022
## yams
## File description:
## yams
##

from src.combinaison import *

def myYams(dies, combinaison):
    ptrFunc = {
        "pair" : pair,
	    "three" : three,
	    "four" : four,
	    "full" : full,
	    "straight" : straight,
	    "yams" : yams
	}
    for func in ptrFunc:
        if func == combinaison[0]:
            return ptrFunc[func](dies, combinaison)
    return