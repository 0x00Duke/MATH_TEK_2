#!/usr/bin/env python3
##
## EPITECH PROJECT, 2021
## 204ducks
## File description:
## Calculations.py
##

from sys import argv
from math import exp, sqrt

class Calculations:

    def __init__(self):
        self._constant = float(argv[1])


    def probability(self, t, state=0):

        if state == 1:
            return (-self._constant * exp(-t) - (4 - 3 * self._constant) / 2 * exp(-2 * t) - (2 * self._constant - 4) / 4 * exp(-4 * t))
        else:
            return ((self._constant * exp(-t))
                    + ((4 - (3 * self._constant)) * exp(-2 * t))
                    + (((2 * self._constant) - 4) * exp(-4 * t)))


    def digitToTime(self, digit):

        minutes = int(digit)
        secondes = round((digit - int(digit)) * 60 + 0.5)
        return minutes, secondes


    def average(self):

        av = 0.

        for t in range (0, 10000):
            av += self.probability((t / 1000)) * (t / 1000) / 1000
        minutes, secondes = self.digitToTime(av)
        print("Average return time: {}m {}s".format(minutes, secondes))
        return av


    def standardDeviation(self, average):

        std = 0.

        for t in range (0, 100000):
            std += (((t / 1000) - average) ** 2) * self.probability((t / 1000)) / 1000
        std = round(sqrt(std), 3)
        print("Standard deviation: {}".format(std))


    def partialReturn(self, p):

        i = 1.0
        while (1):
            if (self.probability(i / 60, 1)) - (self.probability(0, 1)) >= p:
                break
            i += 0.01
        minutes = i % 60 /10
        units = i % 10
        total = i / 60
        print("Time after which {}% of the ducks are back: {}m {}{}s" .format(int(p*100), int(total), int(minutes), round(units)))


    def ducksOverTime(self, time, unit):

        res = (self.probability(time, 1) - self.probability(0, 1)) * 100 + 0.2
        print("Percentage of ducks back after {} {}: {:.1f}%".format(time, unit, (res - 0.2)))


    def run(self):
         
        av = self.average()
        self.standardDeviation(av)
        self.partialReturn(0.50)
        self.partialReturn(0.99)
        self.ducksOverTime(1, "minute")
        self.ducksOverTime(2, "minutes")
        exit(0)
