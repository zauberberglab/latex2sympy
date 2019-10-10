from sympy import Symbol, sympify, simplify, Eq, factor, srepr, pi
from latex2sympy import process_sympy

# x = Symbol('x', real=True)

numeric_responses = ['1', '1.0', '-1', '-1.0', '.5', '-.5', '3x10^3', '3E3', '3,000x10^{-3}', '0.5E-1', '\\frac{1}{3}', '(5\\times 3)^3', '\\sin(1)']

for latex in numeric_responses:
    parsed = process_sympy(latex)
    print('latex: ', latex)
    print('sympy: ', parsed)
    print('is_number: ', parsed.is_number)
    print('is_Number: ', parsed.is_Number)
    print('srepr: ', srepr(parsed))
    print('-----------------------------------------------------')

# answer_sets = [
#     {'correct_answer': '(x-y)(x+2y)', 'student_answers': ['x^2+xy-2y^2', '(x-y)(x+2y)', '(x+2y)(x-y)', '(2y+x)(-y+x)']}
# ]

# for answer_set in answer_sets:
#     correct_answer = answer_set['correct_answer']
#     correct_answer_parsed = process_sympy(answer_set['correct_answer'])
#     for student_answer in answer_set['student_answers']:
#         student_answer_parsed = process_sympy(student_answer)
#         print('correct_answer (c): ', correct_answer)
#         print('student_answer (a): ', student_answer)
#         print('')
#         print('Expression Tree (srepr(c) == srepr(a)) =>', srepr(correct_answer_parsed) == srepr(student_answer_parsed))
#         print('Structural (c == a) =>', correct_answer_parsed == student_answer_parsed)
#         print('Numeric Substitution (c.equals(s)) =>', correct_answer_parsed.equals(student_answer_parsed))
#         print('Symbolic (simplify(c - s) == 0) =>', simplify(correct_answer_parsed - student_answer_parsed) == 0)
#         print('-----------------------------------------------------')

# answer = parsed.evalf()
# answer = parsed.evalf(subs={x: '1'})
# print('answer:', answer)
