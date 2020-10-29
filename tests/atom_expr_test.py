from .context import assert_equal
import pytest
from sympy import Symbol, Integer, Pow


def test_letter_with_supexpr():
    assert_equal("x^2", Pow(Symbol('x', real=True), Integer(2)))


def test_letter_with_subexpr():
    assert_equal("x_2", Symbol('x_2', real=True))


def test_letter_with_subexpr_before_supexpr():
    assert_equal("x_2^2", Pow(Symbol('x_2', real=True), Integer(2)))


def test_letter_with_supexpr_before_subexpr():
    assert_equal("x^2_2", Pow(Symbol('x_2', real=True), Integer(2)))


def test_greek_letter_with_supexpr_before_subexpr():
    assert_equal("\\lambda^2_2", Pow(Symbol('lambda_2', real=True), Integer(2)))
