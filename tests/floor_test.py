from .context import assert_equal
import pytest
from sympy import Symbol, Rational, floor, sqrt, pi

x = Symbol('x', real=True)
y = Symbol('y', real=True)


def test_floor_usual():
    assert_equal("\\floor(1.1)", floor(1.1))
    assert_equal("\\floor(6.9)", floor(6.9))
    assert_equal("\\floor(3.5)", floor(3.5))
    assert_equal("\\floor(8)", floor(8))
    assert_equal("\\floor(0)", floor(0))
    assert_equal("\\floor(290348E32)", floor(Rational('290348E32')))
    assert_equal("\\floor(1237.293894239480234)", floor(Rational('1237.293894239480234')))
    assert_equal("\\floor(8623.4592104E-2)", floor(Rational('8623.4592104E-2')))
    assert_equal("\\floor(\\pi)", floor(pi))
    assert_equal("\\floor(\\sqrt{100})", floor(sqrt(100)))


def test_floor_negative():
    assert_equal("\\floor(-9.4)", floor(-9.4))
    assert_equal("\\floor(-35.9825)", floor(-35.9825))
    assert_equal("\\floor(-\\sqrt{5})", floor(-sqrt(5)))
    assert_equal("\\floor(-324E-3)", floor(Rational('-324E-3')))
    assert_equal("\\floor(-0.23)", floor(-0.23))


def test_floor_fraction():
    assert_equal("\\floor(1/2)", floor(Rational('1/2')))
    assert_equal("\\floor(6/2)", floor(Rational('6/2')))
    assert_equal("\\floor(9/5)", floor(Rational('9/5')))
    assert_equal("\\floor(-42/6)", floor(Rational('-42/6')))
    assert_equal("\\floor(-325/3)", floor(Rational('-325/3')))
    assert_equal("\\floor(\\pi/2)", floor(pi / 2))


def test_floor_expr():
    assert_equal("\\floor((1+6)/3)", floor(Rational(1 + 6, 3)))
    assert_equal("\\floor(1+6/3)", floor(1 + Rational('6/3')))
    assert_equal("\\floor(7*4/5) * 2", floor(7 * 4 / 5) * 2)
    assert_equal("38+\\floor(15-2.3)", 38 + floor(15 - Rational('2.3')))
    assert_equal("\\sqrt{\\floor(99.9999999999999)}", sqrt(floor(Rational('99.9999999999999'))))


def test_floor_symbol():
    assert_equal("\\floor(x)", floor(x), symbolically=True)
    assert_equal("\\floor(x + y)", floor(x + y), symbolically=True)
    assert_equal("\\floor(9x/4)", floor(9 * x / 4), symbolically=True)
    assert_equal("\\floor(y\\pi)", floor(y * pi), symbolically=True)
    assert_equal("\\floor(2y-y-y)", floor(2 * y - y - y), symbolically=True)
