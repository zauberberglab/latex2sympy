from sympy import *
import sys
sys.path.append("..")
from process_latex import process_sympy

latex = "a+Ib"
math = process_sympy(latex)
print("latex: %s to math: %s to simplify: %s to evalf: %s" %(latex,math,simplify(math),math.evalf()))

latex = "e^{I\\cdot\\pi}"
math = process_sympy(latex)
print("latex: %s to math: %s to simplify: %s to evalf: %s" %(latex,math,simplify(math),math.evalf()))

latex = "\\sum_{i=0}^{n} i \\cdot x"
math = process_sympy(latex)
print("latex: %s to math: %s to simplify: %s to evalf: %s" %(latex,math,simplify(math),math.evalf()))
