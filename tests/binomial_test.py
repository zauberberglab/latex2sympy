from sympy import *
import sys
sys.path.append("..")
from process_latex import process_sympy

latex = "\\binom{16}{2}"
math = process_sympy(latex)
print("latex: %s to math: %s" %(latex,math))

latex = "\\binom{x}{y}"
math = process_sympy(latex)
print("latex: %s to math: %s" %(latex,math))

latex = "\\choose{x}{y}"
math = process_sympy(latex)
print("latex: %s to math: %s" %(latex,math))

latex = "\\choose{16}{2}"
math = process_sympy(latex)
print("latex: %s to math: %s" %(latex,math))
