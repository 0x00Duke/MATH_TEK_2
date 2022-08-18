##
## EPITECH PROJECT, 2021
## B-MAT-400-BAR-4-1-206neutrinos-jose-antonio.rodriguez-assalone
## File description:
## Program.py
##

from src.classes.Calculator import Calculator

class Program:
    def __init__(self, nb_values, arithmetic_mean, harmonic_mean, std_deviation):
        self.calculator = Calculator(nb_values, arithmetic_mean, harmonic_mean, std_deviation)


    def run(self):

        while (True):
            str = input("Enter next value: ")
            if str == "END":
                exit(0)
            i = int(str)
            self.calculator.set_nb_values()
            self.calculator.get_root_mean(i)
            self.calculator.get_standard_deviation(i)
            self.calculator.get_arithmetic_mean(i)
            self.calculator.get_harmonic_mean(i)
            self.calculator.print_results()
    

    def helper():

        print("USAGE\n\t./206neutrinos n a h sd\n\nDESCRIPTION\n\tn\tnumber of values")
        print("\ta\tarithmetic mean\n\th\tharmonic mean\n\tsd\tstandard deviation")
