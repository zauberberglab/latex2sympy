from .context import assert_equal
import pytest
from sympy import Symbol, Mod

x = Symbol('x', real=True)
y = Symbol('y', real=True)


def test_mod_usual():
    assert_equal("128\\mod 3", Mod(128, 3))
    assert_equal("7\\mod 128", Mod(7, 128))
    assert_equal("5\\mod 10", Mod(5, 10))
    assert_equal("5\\mod 5", Mod(5, 5))
    assert_equal("3\\mod 2", Mod(3, 2))
    assert_equal("6109\\mod 28", Mod(6109, 28))
    assert_equal("4000000000\\mod 28791", Mod(4000000000, 28791))
    assert_equal("128\\times 10^300\\mod 876123", Mod(128E300, 876123))


def test_mod_negative():
    assert_equal("-1\\mod 2", Mod(-1, 2))
    assert_equal("-3\\mod 3", Mod(-3, 3))
    assert_equal("-12\\mod -12", Mod(-12, -12))
    assert_equal("-128\\mod 4", Mod(-128, 4))
    assert_equal("9\\mod -213", Mod(9, -213))
    assert_equal("123123\\mod -541", Mod(123123, -541))
    assert_equal("-123123\\mod 541", Mod(-123123, 541))
    assert_equal("-97\\times 10^34\\mod 7", Mod(-97E34, 7))


def test_mod_fraction():
    pass

def test_mod_float():
    pass

def test_mod_bracket():
    pass

def test_mod_expr():
    pass

def test_mod_symbol():
    pass

def test_mod_symbol_expr():
    pass

# delete those below
'''
def test_exp_func():
    assert_equal("\\exp(3)", exp(3))


def test_exp_func_no_delim():
    assert_equal("\\exp3", exp(3))


def test_exp_command():
    assert_equal("\\exponentialE(3)", exp(3))


def test_exp_numeric():
    assert_equal("e^3", exp(3))


def test_exp_symbol():
    assert_equal("e^x", exp(x))


def test_exp_symbol_expr():
    assert_equal("e^{x+y}", exp(x + y))


def test_exp_symbol_expr_group():
    assert_equal("e^{(x+y)}", exp(x + y))


def test_exp_expr():
    assert_equal("\\sin(x)*e^x", sin(x) * exp(x))
'''