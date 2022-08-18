#!/usr/bin/env python3
##
## EPITECH PROJECT, 2021
## B-MAT-400-BAR-4-1-203hotline-leon.ducasse
## File description:
## BinomialFunc.py
##

from math import factorial

class Binomial():
    def coef(self, a, b):
        return (factorial(a) // (factorial(b) * factorial(a - b)))

    def binomial(self, a, b, c):
        return (self.coef(a, b) * pow(c, b) * pow((1 - c), (a - b)))
