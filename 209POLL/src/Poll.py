##
## EPITECH PROJECT, 2021
## B-MAT-400-BAR-4-1-209poll-jose-antonio.rodriguez-assalone
## File description:
## 209poll.py
##

from sys import argv as av
from math import sqrt

class Poll():
    def __init__(self):
        self._pSize = int(av[1])
        self._sSize = int(av[2])
        self._p = float(av[3])
        self._var = 0
    
    def displayInfo(self):
        print(f"Population size:\t{self._pSize}")
        print(f"Sample size:\t\t{self._sSize}")
        print("Voting intentions:\t%.2f%%" % self._p)
    
    def getVariance(self):
        var = (self._p * (100 - self._p)) / 10000
        emean = (self._pSize - self._sSize) / (self._pSize - 1)
        self._var = (var / self._sSize) * emean

        print("Variance:\t\t%.6f" % self._var)
    
    def getConfidence(self, coef, percent):
        conf = coef * sqrt(self._var) * 100
        lowConf = 0 if self._p - conf < 0 else self._p - conf
        highConf = 100 if self._p + conf > 100 else self._p + conf

        print("%d%% confidence interval: [%.2f%%; %.2f%%]" % (percent, lowConf, highConf))

    
    def run(self):
        self.displayInfo()
        self.getVariance()
        self.getConfidence(1.96, 95)
        self.getConfidence(2.58, 99)
