import sys
sys.path.append("..")
from latex2sympy import process_sympy

latex = "\\int x dx"
math = process_sympy(latex)
print("latex: %s to math: %s" %(latex,math))

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

latex = "\\frac{1}{2}ab(a+b)"
math = process_sympy(latex)
print("latex: %s to math: %s" %(latex,math))
