from .context import assert_equal
import pytest
from sympy import Symbol, Mod

x = Symbol('x', real=True)
y = Symbol('y', real=True)


def test_mod_usual():
    assert_equal("128\\mod 3", Mod(128, 3))
    assert_equal("5\\mod 5", Mod(5, 5))
    assert_equal("3\\mod 2", Mod(3, 2))
    assert_equal("6109\\mod 28", Mod(6109, 28))
    assert_equal("4000000000\\mod 28791", Mod(4000000000, 28791))

def test_mod_E():
    pass

def test_mod_negative():
    pass

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