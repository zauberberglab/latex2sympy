from sympy import *
import sys
sys.path.append("..")
from process_latex import process_sympy

latex = "\\sin\\left(x\\right)\\cdot x"
math = process_sympy(latex)
print("latex: %s to math: %s" %(latex,math))
