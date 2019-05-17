from sympy import *
import sys
sys.path.append("..")
from latex2sympy import process_sympy

x = Symbol('x', real=True);

# latex = "\\sinh(x)"
# math = process_sympy(latex)
# print("latex: %s to math: %s" %(latex,math))
#
# latex = "\\arcsinh(x)"
# math = process_sympy(latex)
# print("latex: %s to math: %s" %(latex,math))
#
# latex = "\\arsinh(x)"
# math = process_sympy(latex)
# print("latex: %s to math: %s" %(latex,math))

latex = "\\operatorname{arcsinh}\\left(1\\right)"
math = process_sympy(latex)
print("latex: %s to math: %s" %(latex,math))
