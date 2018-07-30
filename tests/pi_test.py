from sympy import *
import sys
sys.path.append("..")
from process_latex import process_sympy
print(acos(-1))
print(acos(0))
print(acos(1))

latex = "\\frac{\\pi}{3}"
math = process_sympy(latex)
print("latex: %s to math: %s to simplify: %s to evalf: %s" %(latex,math,simplify(math),math.evalf()))

latex = "\\arccos{\\cos{\\frac{\\pi}{3}}}"
math = process_sympy(latex)
print("latex: %s to math: %s to simplify: %s to evalf: %s" %(latex,math,simplify(math),math.evalf()))

latex = "\\arccos{-1}"
math = process_sympy(latex)
print("latex: %s to math: %s to simplify: %s to evalf: %s" %(latex,math,simplify(math),math.evalf()))
