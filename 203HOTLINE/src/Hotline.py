#!/usr/bin/env python3
##
## EPITECH PROJECT, 2021
## B-MAT-400-BAR-4-1-203hotline-leon.ducasse
## File description:
## Hotline.py
##

from sys import argv as av
from time import time
from .BinomialFunc import Binomial
from math import *

class Hotline():
    def __init__(self):
        self._bi = Binomial()
        if (len(av) == 3):
            self._n = int(av[1])
            self._k = int(av[2])
        else:
            self._d = int(av[1])
    
    def calculBinomial(self):
        res = self._bi.coef(self._n, self._k)
        print("%d-combinations of a set of size %d:\n%d" % (self._k, self._n, res))

    def calculDistribution(self):
        def calculOverload(myList) -> float:
            res = 0
            for i in range(26):
                res += myList[i]
            return (1 - res)
        
        def endPrinting(res, timer):
            if self._d > 320:
                print("\nOverload: 100%")
            else:
                print("\nOverload: {:.1f}%".format(calculOverload(res) * 100))
            print("Computation time: {:.2f}ms".format(((time() - timer) * 100)))
        
        def printNewLineOrTab(i):
            if (i+1) % 5 == 0:
                print()
            elif i != 50:
                print("\t", end='')

        def binomialDistribution():
            print("Binomial distribution:")
            timer = time()
            person = self._d / (3600 * 8)
            res = []
            for i in range (0, 51):
                res.append(self._bi.binomial(3500, i, person))
                print("{:d} -> {:.3f}".format(i, res[-1]), end='')
                printNewLineOrTab(i)
            endPrinting(res, timer)

        def poissonDistribution():
            print("\nPoisson distribution:")
            timer = time()
            person = 3500 * (self._d / (3600 * 8))
            res = []
            for i in range (0, 51):
                res.append(exp(-person) * pow(person, i) / factorial(i))
                print("{:d} -> {:0.3f}".format(i, res[-1]), end='')
                printNewLineOrTab(i)
            endPrinting(res, timer)
        
        binomialDistribution()
        poissonDistribution()

    def hotline(self):
        if (len(av) == 3):
            self.calculBinomial()
        else:
            self.calculDistribution()


