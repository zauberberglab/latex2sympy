from sympy import simplify, srepr, Add, Mul, Pow
from latex2sympy.latex2sympy import process_sympy, Root
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# shorthand definitions


def _Add(a, b):
    return Add(a, b, evaluate=False)


def _Mul(a, b):
    return Mul(a, b, evaluate=False)


def _Pow(a, b):
    return Pow(a, b, evaluate=False)


def compare(actual, expected, symbolically=False):
    # if isinstance(expected, (list,)):
    #     check = expected == actual
    #     if check:
    #         value = 0
    #     else:
    #         value = 1
    # else:
    #     value = expected - actual
    #     value_simp = simplify(value)
    # assert actual == expected or value == 0 or value_simp == 0
    if symbolically:
        assert simplify(actual - expected) == 0
    else:
        actual_exp_tree = srepr(actual)
        expected_exp_tree = srepr(expected)
        assert actual_exp_tree == expected_exp_tree


def assert_equal(latex, expr, variable_values={}, symbolically=False):
    parsed = process_sympy(latex, variable_values)
    compare(parsed, expr, symbolically)
