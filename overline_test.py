from sympy import *

from process_latex import process_sympy

# latex = "\\overline{x}_n"
# latex = "\\sin(x) * \\overline{x} * \\theta"
latex = "\\frac{1}{\\overline{x}_n}"
math = process_sympy(latex)
print("latex: %s to math: %s" %(latex,math))
