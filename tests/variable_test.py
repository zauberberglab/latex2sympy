from .context import assert_equal
import pytest
import hashlib
from sympy import Symbol

x = Symbol('x', real=True)

def test_variable():
	assert_equal("\\variable{x}", Symbol('x' + hashlib.md5('x'.encode()).hexdigest(), real=True))
def test_variable_letter_subscript():
	assert_equal("\\variable{x_y}", Symbol('x_y' + hashlib.md5('x_y'.encode()).hexdigest(), real=True))
def test_variable_digit_subscript():
	assert_equal("\\variable{x_1}", Symbol('x_1' + hashlib.md5('x_1'.encode()).hexdigest(), real=True))
def test_variable_in_expr():
	assert_equal("4\\cdot\\variable{x}", 4*Symbol('x' + hashlib.md5('x'.encode()).hexdigest(), real=True))
def test_variable_with_greek_letter_command():
	assert_equal("\\variable{\\alpha}\\alpha", Symbol('\\alpha' + hashlib.md5('\\alpha'.encode()).hexdigest(), real=True)*Symbol('alpha', real=True))
def test_variable_with_greek_letter_subscript():
	assert_equal("\\variable{\\alpha_\\beta}\\alpha", Symbol('\\alpha_\\beta' + hashlib.md5('\\alpha_\\beta'.encode()).hexdigest(), real=True)*Symbol('alpha', real=True))
def test_variable_complex_name():
	assert_equal("\\variable{x\\beta10_y\\alpha20}", Symbol('x\\beta10_y\\alpha20' + hashlib.md5('x\\beta10_y\\alpha20'.encode()).hexdigest(), real=True))
def test_variable_complex_expr():
	assert_equal("4\\cdot\\variable{value1}\\frac{\\variable{value_2}}{\\variable{a}}\\cdot x^2", 4*Symbol('value1' + hashlib.md5('value1'.encode()).hexdigest(), real=True)*Symbol('value_2' + hashlib.md5('value_2'.encode()).hexdigest(), real=True)/Symbol('a' + hashlib.md5('a'.encode()).hexdigest(), real=True)*x**2)