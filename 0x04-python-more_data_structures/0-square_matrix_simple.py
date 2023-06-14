#!/usr/bin/python3

def square_matrix_simple(matrix=[]):

    if matrix:
        inner_multiply = lambda i: i * i
        outer_multiply = lambda item: list(map(inner_multiply, item))
        multiply = list(map(outer_multiply, matrix))
        return matrix
    else:
        return matrix
