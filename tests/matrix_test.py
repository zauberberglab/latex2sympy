from sympy import *
import sys
sys.path.append("..")
from process_latex import process_sympy

latex = "\\begin{matrix}1&2\\\\3&4\\end{matrix}"
math = process_sympy(latex)
print("latex: %s to math: %s" %(latex,math))

latex = "\\begin{matrix}1&2\\\\3&4\\\\5&6\\end{matrix}"
math = process_sympy(latex)
print("latex: %s to math: %s" %(latex,math))

latex = "\\begin{matrix}1&2&3\\\\4&5&6\\\\7&8&9\\end{matrix}"
math = process_sympy(latex)
print("latex: %s to math: %s" %(latex,math))
