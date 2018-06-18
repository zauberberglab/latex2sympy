from sympy import *
import sys
sys.path.append("..")
from process_latex import process_sympy

latex = "e^3"
math = process_sympy(latex)
print("latex: %s to math: %s" %(latex,math))

latex = "e^x"
math = process_sympy(latex)
print("latex: %s to math: %s" %(latex,math))

latex = "\\sin(x)*e^x"
math = process_sympy(latex)
print("latex: %s to math: %s" %(latex,math))

latex = "e^{(x+y)}"
math = process_sympy(latex)
print("latex: %s to math: %s" %(latex,math))

latex = "e"
math = process_sympy(latex)
print("latex: %s to math: %s" %(latex,math))

latex = '\\mathit{test}'
math = process_sympy(latex)
print("latex: %s to math: %s" %(latex,math))
