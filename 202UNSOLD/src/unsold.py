#!/usr/bin/env python3
##
## EPITECH PROJECT, 2021
## B-MAT-400-BAR-4-1-202unsold-leon.ducasse
## File description:
## unsold.py
##

from sys import argv as av
from math import ceil

class Unsold():
    def __init__(self):
        self._a = int(av[1])
        self._b = int(av[2])
        self._table = {}
        self._x = []
        self._y = []
        self._z = {}

    def __print_expected_value_and_variance(self ,value, id, total):
        print('expected value of', id, end='')
        print("%.1f" % value)
        print('variance of', id, end='\t')
        print("%.1f" % total)
    
    def _formula(self, x, y):
        return (((self._a - (x * 10)) * (self._b - y)) / (
                    (5 * self._a - 150) * (5 * self._b - 150)))

    def __print_x_law(self):
        xlawres = 0
        ylawres = 0
        for y in range(1, 6):
            xlaw = 0
            for i in range(1, 6):
                xlaw = xlaw + self._table[i*10][y*10]
                xlawres = xlawres + self._table[i*10][y*10]
            print("%.3f" % xlaw, end='\t')
        for i in range(1, 6):
            xlaw = 0
            for y in range(1, 6):
                ylawres = ylawres + self._table[i * 10][y * 10]
        if ceil(xlawres) == 1 or ceil(ylawres) == 1:
            print("1.000")
        else:
            print("0.000")

    def __get_probability(self, y):
        row = {}
        law = 0
        for x in range(1, 6):
            first = self._formula(x, y)
            print("%.3f" % (first), end='\t')
            row[x*10] = first
            law = law + first
        print("%.3f" % law, end='')
        print('')
        return row

    def first_result(self):
        self.__printXLine()
        for i in range(1, 6):
            print('Y=', end='')
            print(i*10, end='\t')
            self._table[i*10] = self.__get_probability(i*10)
        print('X law', end='\t')
        self.__print_x_law()
    

    def __print_z_law_index(self):
        print('z', end='\t')
        for i in range(2, 11):
            print(i*10, end='')
            if (i + 1) < 11:
                print ("\t", end='')
                
        print('')
        print('p(Z=z)', end='\t')

    def second_result(self):
        self.__print_z_law_index()
        final_result = 0
        for i in range(2, 11):
            res = 0
            for y in range(1, 6):
                for x in range(1, 6):
                    if ((y*10 + x*10) == i*10 and i < 60):
                        res += (self._table[y*10][x*10] + self._table[x*10][y*10])
                        final_result += res
            print("%.3f" % (res / 2), end='')
            if (i + 1) < 11:
                print ("\t", end='')
        print('')

    def __get_z_law(self):
        zzlaw = {}
        zzlaw[20] = self._table[10][10]
        for i in range(3, 11):
            res = 0
            for y in range(1, 6):
                for x in range(1, 6):
                    if ((y*10 + x*10) == i*10 and i < 60):
                        res+=(self._table[y*10][x*10] + self._table[x*10][y*10])
            zzlaw[i*10] = res / 2
        return zzlaw

    def third_result(self):
        x = 0
        y = 0
        total = 0
        xlaw = {}
        ylaw = {}
        for i in range(1, 6):
            law = 0
            for a in range(1, 6):
                total=self._table[a*10][i*10]
                law+=total
                x+=total*i
            xlaw[i*10] = law   
        varx = 0
        for i in range(1, 6):
            varx+=(i * 10 - x*10 )**2 * xlaw[i*10]
        self.__print_expected_value_and_variance(x*10, 'X:\t', varx)
        total = 0
        law = 0
        for i in range(1, 6):
            law=0
            for a in range(1, 6):
                total=self._table[i * 10][a * 10]
                law+=total
                y+=total * i
            ylaw[i*10]=law
        vary = 0
        for i in range(1, 6):
            vary += (i * 10 - y * 10) ** 2 * ylaw[i * 10]
        self.__print_expected_value_and_variance(y*10, 'Y:\t', vary)
        varz=0
        zzlaw=self.__get_z_law()
        for i in range(2, 11):
            varz += (i * 10 - (x+y) * 10)**2 * zzlaw[i*10]
        self.__print_expected_value_and_variance((x + y) * 10, 'Z:\t', varz)

    def separator(self):
        print("----------------------------------------------------------------------------------")
    
    def __printXLine(self):
        print("\tX=10\tX=20\tX=30\tX=40\tX=50\tY law")

