from .context import assert_equal, _Mul, _Pow, _Div
import pytest
from sympy import pi, Symbol, acos, cos


def test_pi_frac():
    assert_equal("\\frac{\\pi}{3}", _Div(pi, 3))


def test_pi_nested():
    assert_equal("\\arccos{\\cos{\\frac{\\pi}{3}}}", acos(cos(_Div(pi, 3), evaluate=False), evaluate=False))


def test_pi_arccos():
    assert_equal("\\arccos{-1}", pi, symbolically=True)
