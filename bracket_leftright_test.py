from sympy import *

from process_latex import process_sympy

latex = "\\sin(\\theta)"
math = process_sympy(latex)
print("latex: %s to math: %s" %(latex,math))

latex = "\\sin\\left(\\theta\\right)"
math = process_sympy(latex)
print("latex: %s to math: %s" %(latex,math))

latex = "\\sin{\\theta}"
math = process_sympy(latex)
print("latex: %s to math: %s" %(latex,math))

latex = "\\sin\\left{\\theta\\right}"
math = process_sympy(latex)
print("latex: %s to math: %s" %(latex,math))

latex = "P(x)"
math = process_sympy(latex)
print("latex: %s to math: %s" %(latex,math))

latex = "P\\left(x\\right)"
math = process_sympy(latex)
print("latex: %s to math: %s" %(latex,math))
