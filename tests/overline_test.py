import sys
sys.path.append("..")
from latex2sympy import process_sympy

latex = "\\frac{\\sin(x)}{\\overline{x}_n}"
math = process_sympy(latex)
print("latex: %s to math: %s" %(latex,math))
