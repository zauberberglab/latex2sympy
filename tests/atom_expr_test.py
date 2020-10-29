from .context import assert_equal
import pytest
from sympy import Symbol, Integer, Pow

# label, text, symbol_text
examples = [
    ('letter', 'x', 'x'),
    ('greek letter', '\\lambda', 'lambda'),
    ('accented letter', '\\overline{x}', 'xbar')
]


@pytest.mark.parametrize('label, text, symbol_text', examples)
def test_with_supexpr(label, text, symbol_text):
    assert_equal(text + "^2", Pow(Symbol(symbol_text, real=True), Integer(2)))


@pytest.mark.parametrize('label, text, symbol_text', examples)
def test_with_subexpr(label, text, symbol_text):
    assert_equal(text + "_2", Symbol(symbol_text + '_2', real=True))


@pytest.mark.parametrize('label, text, symbol_text', examples)
def test_with_subexpr_before_supexpr(label, text, symbol_text):
    assert_equal(text + "_2^2", Pow(Symbol(symbol_text + '_2', real=True), Integer(2)))


@pytest.mark.parametrize('label, text, symbol_text', examples)
def test_with_subexpr_before_supexpr_with_braces(label, text, symbol_text):
    assert_equal(text + "_{2}^{2}", Pow(Symbol(symbol_text + '_2', real=True), Integer(2)))


@pytest.mark.parametrize('label, text, symbol_text', examples)
def test_with_supexpr_before_subexpr(label, text, symbol_text):
    assert_equal(text + "^2_2", Pow(Symbol(symbol_text + '_2', real=True), Integer(2)))


@pytest.mark.parametrize('label, text, symbol_text', examples)
def test_with_supexpr_before_subexpr_with_braces(label, text, symbol_text):
    assert_equal(text + "^{2}_{2}", Pow(Symbol(symbol_text + '_2', real=True), Integer(2)))
