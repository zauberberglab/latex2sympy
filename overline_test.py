from sympy import *

from process_latex import process_sympy

latex = "\\frac{\\sin(x)}{\\overline{x}_n}"
math = process_sympy(latex)
print("latex: %s to math: %s" %(latex,math))
