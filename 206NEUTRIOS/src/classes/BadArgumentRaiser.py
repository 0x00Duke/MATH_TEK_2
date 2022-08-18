##
## EPITECH PROJECT, 2021
## B-MAT-400-BAR-4-1-206neutrinos-jose-antonio.rodriguez-assalone
## File description:
## BadArgumentRaiser.py
##

class   BadArgumentRaiser(Exception):
    def __init__(self, message, errors = "BadArgumentRaiser"):
        super().__init__(message)
        self.errors = errors
