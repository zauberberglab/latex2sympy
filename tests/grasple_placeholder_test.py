import sys
sys.path.append("..")
from latex2sympy import process_sympy

latex = "[!value!]"
math = process_sympy(latex)
print("latex: %s to math: %s" %(latex,math))

latex = "x^2"
math = process_sympy(latex)
print("latex: %s to math: %s" %(latex,math))

latex = "[!value1!]"
math = process_sympy(latex)
print("latex: %s to math: %s" %(latex,math))

latex = "[!value_1!]"
math = process_sympy(latex)
print("latex: %s to math: %s" %(latex,math))

latex = "4\\cdot[!value_1!]\\frac{[!value_2!]}{[!value3!]}"
latex = "4\\cdot[!value_1!]\\frac{[!value_2!]}{[!a!]}"
math = process_sympy(latex)
print("latex: %s to math: %s" %(latex,math))

latex = "4\\cdot[!value_1!]"
math = process_sympy(latex)
print("latex: %s to math: %s" %(latex,math))

latex = "4\\cdot[!a!]"
math = process_sympy(latex)
print("latex: %s to math: %s" %(latex,math))
