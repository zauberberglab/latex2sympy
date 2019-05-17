import sys
sys.path.append("..")
from latex2sympy import process_sympy

latex = "\\sin\\left(x\\right)\\cdot x"
math = process_sympy(latex)
print("latex: %s to math: %s" %(latex,math))
