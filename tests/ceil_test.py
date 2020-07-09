from .context import assert_equal
import pytest
from sympy import Symbol, Rational, ceiling, sqrt, pi

x = Symbol('x', real=True)
y = Symbol('y', real=True)


def test_ceil_usual():
    assert_equal("\\ceil(1.1)", ceiling(1.1))
    assert_equal("\\ceil(6.9)", ceiling(6.9))
    assert_equal("\\ceil(3.5)", ceiling(3.5))
    assert_equal("\\ceil(8)", ceiling(8))
    assert_equal("\\ceil(0)", ceiling(0))
    assert_equal("\\ceil(290348E32)", ceiling(Rational('290348E32')))
    assert_equal("\\ceil(1237.293894239480234)", ceiling(Rational('1237.293894239480234')))
    assert_equal("\\ceil(8623.4592104E-2)", ceiling(Rational('8623.4592104E-2')))
    assert_equal("\\ceil(\\pi)", ceiling(pi))
    assert_equal("\\ceil(\\sqrt{100})", ceiling(sqrt(100)))

    assert_equal("\\operatorname{ceil}(1.1)", ceiling(1.1))
    assert_equal("\\operatorname{ceil}(6.9)", ceiling(6.9))
    assert_equal("\\operatorname{ceil}(3.5)", ceiling(3.5))
    assert_equal("\\operatorname{ceil}(8)", ceiling(8))
    assert_equal("\\operatorname{ceil}(0)", ceiling(0))
    assert_equal("\\operatorname{ceil}(290348E32)", ceiling(Rational('290348E32')))
    assert_equal("\\operatorname{ceil}(1237.293894239480234)", ceiling(Rational('1237.293894239480234')))
    assert_equal("\\operatorname{ceil}(8623.4592104E-2)", ceiling(Rational('8623.4592104E-2')))
    assert_equal("\\operatorname{ceil}(\\pi)", ceiling(pi))
    assert_equal("\\operatorname{ceil}(\\sqrt{100})", ceiling(sqrt(100)))


def test_ceil_negative():
    assert_equal("\\ceil(-9.4)", ceiling(-9.4))
    assert_equal("\\ceil(-35.9825)", ceiling(-35.9825))
    assert_equal("\\ceil(-\\sqrt{5})", ceiling(-sqrt(5)))
    assert_equal("\\ceil(-324E-3)", ceiling(Rational('-324E-3')))
    assert_equal("\\ceil(-0.23)", ceiling(-0.23))

    assert_equal("\\operatorname{ceil}(-9.4)", ceiling(-9.4))
    assert_equal("\\operatorname{ceil}(-35.9825)", ceiling(-35.9825))
    assert_equal("\\operatorname{ceil}(-\\sqrt{5})", ceiling(-sqrt(5)))
    assert_equal("\\operatorname{ceil}(-324E-3)", ceiling(Rational('-324E-3')))
    assert_equal("\\operatorname{ceil}(-0.23)", ceiling(-0.23))


def test_ceil_fraction():
    assert_equal("\\ceil(1/2)", ceiling(Rational('1/2')))
    assert_equal("\\ceil(6/2)", ceiling(Rational('6/2')))
    assert_equal("\\ceil(9/5)", ceiling(Rational('9/5')))
    assert_equal("\\ceil(-42/6)", ceiling(Rational('-42/6')))
    assert_equal("\\ceil(-325/3)", ceiling(Rational('-325/3')))
    assert_equal("\\ceil(\\pi/2)", ceiling(pi / 2))

    assert_equal("\\operatorname{ceil}(1/2)", ceiling(Rational('1/2')))
    assert_equal("\\operatorname{ceil}(6/2)", ceiling(Rational('6/2')))
    assert_equal("\\operatorname{ceil}(9/5)", ceiling(Rational('9/5')))
    assert_equal("\\operatorname{ceil}(-42/6)", ceiling(Rational('-42/6')))
    assert_equal("\\operatorname{ceil}(-325/3)", ceiling(Rational('-325/3')))
    assert_equal("\\operatorname{ceil}(\\pi/2)", ceiling(pi / 2))


def test_ceil_expr():
    assert_equal("\\ceil((1+6)/3)", ceiling(Rational(1 + 6, 3)))
    assert_equal("\\ceil(1+6/3)", ceiling(1 + Rational('6/3')))
    assert_equal("\\ceil(7*4/5) * 2", ceiling(7 * 4 / 5) * 2)
    assert_equal("38+\\ceil(15-2.3)", 38 + ceiling(15 - Rational('2.3')))
    assert_equal("\\sqrt{\\ceil(99.9999999999999)}", sqrt(ceiling(Rational('99.9999999999999'))))

    assert_equal("\\operatorname{ceil}((1+6)/3)", ceiling(Rational(1 + 6, 3)))
    assert_equal("\\operatorname{ceil}(1+6/3)", ceiling(1 + Rational('6/3')))
    assert_equal("\\operatorname{ceil}(7*4/5) * 2", ceiling(7 * 4 / 5) * 2)
    assert_equal("38+\\operatorname{ceil}(15-2.3)", 38 + ceiling(15 - Rational('2.3')))
    assert_equal("\\sqrt{\\operatorname{ceil}(99.9999999999999)}", sqrt(ceiling(Rational('99.9999999999999'))))


def test_ceil_symbol():
    assert_equal("\\ceil(x)", ceiling(x), symbolically=True)
    assert_equal("\\ceil(x + y)", ceiling(x + y), symbolically=True)
    assert_equal("\\ceil(9x/4)", ceiling(9 * x / 4), symbolically=True)
    assert_equal("\\ceil(y\\pi)", ceiling(y * pi), symbolically=True)
    assert_equal("\\ceil(2y-y-y)", ceiling(2 * y - y - y), symbolically=True)

    assert_equal("\\operatorname{ceil}(x)", ceiling(x), symbolically=True)
    assert_equal("\\operatorname{ceil}(x + y)", ceiling(x + y), symbolically=True)
    assert_equal("\\operatorname{ceil}(9x/4)", ceiling(9 * x / 4), symbolically=True)
    assert_equal("\\operatorname{ceil}(y\\pi)", ceiling(y * pi), symbolically=True)
    assert_equal("\\operatorname{ceil}(2y-y-y)", ceiling(2 * y - y - y), symbolically=True)
