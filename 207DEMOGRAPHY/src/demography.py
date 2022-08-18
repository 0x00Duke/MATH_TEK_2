##
# EPITECH PROJECT, 2021
# 207
# File description:
# demography.py
##

from math import sqrt
import csv
from sys import argv as av


class Demography():
    def __init__(self):
        self._countries = av[1:]
        self._values = []
        self._keys = []
        self._pop = []
        self._years = []
        self._popSum = 0
        self._yearsSum = 0
        self._popPow = 0
        self._yearsPow = 0
        self._xy = 0

    def getValues(self):
        file = open("./deps/207demography_data.csv", 'r')
        reader = csv.reader(file, delimiter=';')
        for n in reader:
            self._values.append(n)

    def getKeys(self):
        normalLen = 0

        for country in self._countries:
            for n in range(len(self._values)):
                if self._values[n][1] == country:
                    self._keys.append(n)
                    normalLen += 1
        if normalLen != len(self._countries):
            exit(84)

    def getPop(self):
        for n in range(2, len(self._values[1])):
            self._pop.append(0)
        for key in self._keys:
            x = 0
            for pop in range(2, len(self._values[key])):
                self._pop[x] += int(self._values[key][pop])
                x += 1
        for pop in self._pop:
            self._popSum += pop
            self._popPow += pop**2

    def getYears(self):
        for n in range(2, len(self._values[0])):
            self._years.append(int(self._values[0][n]))
        for year in self._years:
            self._yearsSum += year
            self._yearsPow += year**2

    def getXY(self):
        for n in range(len(self._pop)):
            self._xy += self._pop[n] * self._years[n]

    def printCoutries(self):
        print("Country: ", end="")
        for key in self._keys:
            print(self._values[key][0], end="")
            if key != self._keys[len(self._keys) - 1]:
                print(", ", end="")
        print()

    def printFit1(self):

        def printPos(a, b):
            print("   Y = {:.2f} X + ".format(a/1000000), end="")
            print("{:.2f}".format(b/1000000))

        def printNeg(a, b):
            print("   Y = {:.2f} X - ".format(a/1000000), end="")
            print("{:.2f}".format(abs(b/1000000)))

        def getMean(a, b):
            mean = 0
            for n in range(len(self._pop)):
                mean += ((self._years[n] * a + b) -
                         self._pop[n])**2 / len(self._pop)
            return mean

        a = (len(self._years) * self._xy - self._popSum * self._yearsSum) / \
            (len(self._years) * self._yearsPow - self._yearsSum ** 2)
        b = (self._popSum * self._yearsPow - self._yearsSum * self._xy) / \
            (len(self._years) * self._yearsPow - self._yearsSum ** 2)

        print("Fit1")
        printPos(a, b) if b >= 0 else printNeg(a, b)
        mean = getMean(a, b)
        print(
            "   Root-mean-square deviation: {:.2f}".format(sqrt(mean)/1000000))
        print("   Population in 2050: {:.2f}".format((2050 * a + b)/1000000))

    def printFit2(self):
        def printPos(a, b):
            print("   X = {:.2f} Y + ".format(a*1000000), end="")
            print("{:.2f}".format(b))

        def printNeg(a, b):
            print("   X = {:.2f} Y - ".format(a*1000000), end="")
            print("{:.2f}".format(abs(b)))

        def getMean(a, b):
            mean = 0
            for n in range(len(self._pop)):
                mean += ((self._years[n] - b) / a -
                         self._pop[n])**2 / len(self._pop)
            return mean

        a = (len(self._pop) * self._xy - self._yearsSum *
             self._popSum) / (len(self._pop) * self._popPow - self._popSum**2)
        b = (self._yearsSum * self._popPow - self._popSum *
             self._xy) / (len(self._pop) * self._popPow - self._popSum ** 2)

        print("Fit2")
        printPos(a, b) if b >= 0 else printNeg(a, b)
        mean = getMean(a, b)
        print(
            "   Root-mean-square deviation: {:.2f}".format(sqrt(mean)/1000000))
        print("   Population in 2050: {:.2f}".format((2050 - b) / a/1000000))

    def correlation(self):
        correlation = (len(self._pop) * self._xy) - \
            (self._yearsSum * self._popSum)
        correlation /= sqrt((len(self._years) * self._yearsPow - self._yearsSum**2)
                            * (len(self._pop) * self._popPow - self._popSum**2))
        print("Correlation: {:.4f}".format(correlation))

    def printing(self):
        self.printCoutries()
        self.printFit1()
        self.printFit2()

    def demography(self):
        self.getValues()
        self.getKeys()
        self.getPop()
        self.getYears()
        self.getXY()

        self.printing()
        self.correlation()
