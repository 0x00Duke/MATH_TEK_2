##
## EPITECH PROJECT, 2021
## 205
## File description:
## 205IQ.py
##

from sys import argv as av
from math import exp, sqrt, pi

class IQ():
    def __init__(self):
        self._u = int(av[1])
        self._std = int(av[2])
        self._IQ1 = 0
        self._IQ2 = 0
        self._values = []

        if (len(av) > 3):
            self._IQ1 = int(av[3])
        if (len(av) > 4):
            self._IQ2 = int(av[4])
        
    def distribution(self, num):
        return (1 / (self._std * sqrt(2 * pi))) * exp(-(pow(num - self._u, 2) / (2 * self._std * self._std)))

    def getBound(self, min, max):
        res = 0
        n = min
        while (n < max):
            res += self.distribution(n)
            n += 0.01
        
        if min == 0:
            print("%.1f%% of people have an IQ inferior to %d" % (res, max))
        else:
            print("%.1f%% of people have an IQ between %d and %d" % (res, min, max))

    def printDensity(self):
        for n in range(201):
            print("%d %.5f" % (n, self._values[n]))
    
    def mainLoop(self):
        for n in range(201):
            self._values.append(self.distribution(n))
        if (self._IQ1 == 0 and self._IQ2 == 0):
            self.printDensity()
        elif (self._IQ2 == 0):
            self.getBound(0, self._IQ1)
        else:
            self.getBound(self._IQ1, self._IQ2)
