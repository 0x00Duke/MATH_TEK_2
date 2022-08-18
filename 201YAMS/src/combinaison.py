##
## EPITECH PROJECT, 2022
## yams
## File description:
## combinaison
##

from sys import argv as av
from math import *

NBDIES = 5

def getCoefficient(a, b):
    return factorial(a) / (factorial(b) * factorial(a-b))

def binomial(a, b):
    return (getCoefficient(a, b) * pow(1/6, b) * pow(5/6, (a - b)))

def getprobabilities(dies, combinaison, combinaisonOcc):
    result = 0
    occurrences = dies.count(int(combinaison[1]))
    if occurrences < combinaisonOcc:
        for x in range(combinaisonOcc - occurrences, NBDIES - occurrences + 1):
            result += binomial(NBDIES - occurrences, x)
    else:
        return 100
    return result * 100

def pair(dies, combinaison):
    print("Chances to get a %s pair: %0.2f%%" % (combinaison[1], getprobabilities(dies, combinaison, 2)))

def three(dies, combinaison):
    print("Chances to get a %s three-of-a-kind: %0.2f%%" % (combinaison[1], getprobabilities(dies, combinaison, 3)))

def four(dies, combinaison):
    print("Chances to get a %s four-of-a-kind: %0.2f%%" % (combinaison[1], getprobabilities(dies, combinaison, 4)))

def full(dies, combinaison):
    result = 1
    occurrencesA = dies.count(int(combinaison[1]))
    occurrencesB = dies.count(int(combinaison[2]))
    if (occurrencesA == 3 and occurrencesB == 2):
        print("Chances to get a %s full of %s: 100.00%%" % (combinaison[1], combinaison[2]))
        return
    occurrencesA = 3 if occurrencesA > 3 else occurrencesA
    occurrencesB = 2 if occurrencesB > 2 else occurrencesB

    result = getCoefficient(5 - occurrencesA - occurrencesB, 3 - occurrencesA) * pow(1/6, 5 - occurrencesA - occurrencesB)
    print ("Chances to get a %s full of %s: %0.2f%%" % (combinaison[1], combinaison[2], result * 100))

def allNumIn(dies, high):
    if high == 5:
        for x in range(1, 6):
            if dies.count(x) != 1:
                return False
        return True
    for x in range(2, 7):
        if dies.count(x) != 1:
            return False
    return True

def straight(dies, combinaison):
    res = 0
    if combinaison[1] == "5":
        if (allNumIn(dies, 5)):
            print("Chances to get a 5 straight: 100.00%")
            return
        for x in range(1,6):
            if x in dies:
                res += 1
    else:
        if (allNumIn(dies, 6)):
            print("Chances to get a 6 straight: 100.00%")
            return
        for x in range(2,7):
            if x in dies:
                res += 1
    print("Chances to get a %s straight: %0.2f%%" % (combinaison[1], (factorial(5 - res) / pow(6, 5 - res) * 100)))

def yams(dies, combinaison):
    print("Chances to get a %s yams: %0.2f%%" % (combinaison[1], getprobabilities(dies, combinaison, 5)))
