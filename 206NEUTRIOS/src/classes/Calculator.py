##
## EPITECH PROJECT, 2021
## B-MAT-400-BAR-4-1-206neutrinos-jose-antonio.rodriguez-assalone
## File description:
## Calculator.py
##

from math import pow, sqrt
from src.classes.BadArgumentRaiser import BadArgumentRaiser

class   Calculator():

    def __init__(self, nb_values, arithmetic_mean, harmonic_mean, std_deviation):
    
        if nb_values < 0 or arithmetic_mean < 0 or harmonic_mean < 0 or std_deviation < 0:
            raise BadArgumentRaiser("All of my arguments positive shall be")
        self.nb_values = nb_values
        self.arithmetic_mean = arithmetic_mean
        self.harmonic_mean = harmonic_mean
        self.std_deviation = std_deviation
        self.root_mean = 0


    def set_nb_values(self):

        self.nb_values += 1


    def get_standard_deviation(self, i):

        self.std_deviation = sqrt((((pow(self.std_deviation, 2) + pow(self.arithmetic_mean, 2))
        * (self.nb_values - 1) + pow(i, 2)) / self.nb_values) - pow(((self.arithmetic_mean
        * (self.nb_values - 1)) + i) / self.nb_values, 2))


    def get_arithmetic_mean(self, i):

        self.arithmetic_mean = ((self.arithmetic_mean * (self.nb_values - 1)) + i) / self.nb_values


    def get_root_mean(self, i):

        self.root_mean = sqrt((((pow(self.std_deviation, 2) + pow(self.arithmetic_mean, 2))
        * (self.nb_values - 1)) + pow(i, 2)) / self.nb_values)


    def get_harmonic_mean(self, i):

        self.harmonic_mean = self.nb_values / (((1 / self.harmonic_mean) * (self.nb_values - 1)) + (1 / i))


    def print_results(self):

        print("\tNumber of values:\t%.0f" % self.nb_values)
        print("\tStandard deviation:\t%.2f" % self.std_deviation)
        print("\tArithmetic mean:\t%.2f" % self.arithmetic_mean)
        print("\tRoot mean square:\t%.2f" % self.root_mean)
        print("\tHarmonic mean:\t%.2f\n" % self.harmonic_mean)
